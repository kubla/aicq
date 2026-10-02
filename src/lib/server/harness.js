import { env as privateEnv } from '$env/dynamic/private';
import { env } from '$env/dynamic/public';
import { error, json } from '@sveltejs/kit';
import { getIdentity } from './session.js';

/** @param {import('@sveltejs/kit').RequestEvent} event */
export async function requireOwner(event) {
  const token = event.cookies.get('fulcra_access_token');
  const identity = await getIdentity(token, event.fetch);
  if (!privateEnv.OWNER_USER_ID) error(503, 'Harness owner has not been configured');
  if (identity.userid !== privateEnv.OWNER_USER_ID)
    error(403, 'The development dashboard is owner-only');
  return token;
}

/** @param {import('@sveltejs/kit').RequestEvent} event */
export async function getRuns(event) {
  const token = await requireOwner(event);
  // Resource scope comes from configuration, never a caller-supplied query.
  const type = env.PUBLIC_HARNESS_ANNOTATION_ID;
  if (!type) error(503, 'Harness annotation has not been configured');
  const end = new Date();
  const start = new Date(end.getTime() - 30 * 86400000);
  const query = new URLSearchParams({
    start_time: start.toISOString(),
    end_time: end.toISOString()
  });
  const response = await event.fetch(
    `${env.PUBLIC_FULCRA_API_ENDPOINT}data/v1alpha1/event/${encodeURIComponent(type)}?${query}`,
    {
      headers: { Authorization: `Bearer ${token}` },
      signal: AbortSignal.timeout(10000)
    }
  );
  if (!response.ok)
    error(response.status === 401 ? 401 : 502, 'Could not load harness events from Fulcra');
  return json(await response.json(), { headers: { 'Cache-Control': 'no-store' } });
}

/** @param {import('@sveltejs/kit').RequestEvent} event
 * @param {string} name
 */
export async function getWorkspaceText(event, name) {
  const token = await requireOwner(event);
  const workspace = env.PUBLIC_WORKSPACE_PATH;
  if (!workspace) error(503, 'Workspace has not been configured');
  const endpoint = env.PUBLIC_FULCRA_API_ENDPOINT;
  const headers = { Authorization: `Bearer ${token}` };
  const folder = `/${workspace.replace(/^\/+|\/+$/g, '')}`;
  const listing = await event.fetch(`${endpoint}input/v1/file?path=${encodeURIComponent(folder)}`, {
    headers,
    signal: AbortSignal.timeout(10000)
  });
  if (!listing.ok) error(502, 'Could not load the canonical workspace');
  const data = await listing.json();
  const file = data.files?.find(
    /** @param {{name: string, id: string}} item */ (item) => item.name === name
  );
  if (!file) error(404, `Canonical ${name} is missing`);
  const download = await event.fetch(
    `${endpoint}input/v1/file/${encodeURIComponent(file.id)}/download`,
    { headers, signal: AbortSignal.timeout(10000) }
  );
  if (!download.ok) error(502, `Could not download ${name}`);
  return new Response(await download.text(), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' }
  });
}
