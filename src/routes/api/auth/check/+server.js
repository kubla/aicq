import { json, isHttpError } from '@sveltejs/kit';
import { getIdentity } from '$lib/server/session.js';
/** @type {import('./$types').RequestHandler} */
export async function GET({ cookies, fetch }) {
  if (!cookies.get('fulcra_access_token')) return json({ authenticated: false });
  try {
    await getIdentity(cookies.get('fulcra_access_token'), fetch);
  } catch (err) {
    if (isHttpError(err) && err.status === 401) {
      cookies.delete('fulcra_access_token', { path: '/' });
      return json({ authenticated: false });
    }
    throw err;
  }
  return json({ authenticated: true }, { headers: { 'Cache-Control': 'no-store' } });
}
