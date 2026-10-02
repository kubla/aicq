import { json } from '@sveltejs/kit';
import { getIdentity } from '$lib/server/session.js';
/** @type {import('./$types').RequestHandler} */
export async function GET({ cookies, fetch }) {
  return json(await getIdentity(cookies.get('fulcra_access_token'), fetch), {
    headers: { 'Cache-Control': 'no-store' }
  });
}
