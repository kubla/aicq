import { env } from '$env/dynamic/private';
import { json } from '@sveltejs/kit';
import { getIdentity } from '$lib/server/session.js';
/** @param {import('@sveltejs/kit').RequestEvent} event */
export async function GET({ cookies, fetch }) {
  const token = cookies.get('fulcra_access_token');
  if (!token) return json({ isOwner: false }, { headers: { 'Cache-Control': 'no-store' } });
  const identity = await getIdentity(token, fetch);
  return json(
    { isOwner: Boolean(env.OWNER_USER_ID && identity.userid === env.OWNER_USER_ID) },
    { headers: { 'Cache-Control': 'no-store' } }
  );
}
