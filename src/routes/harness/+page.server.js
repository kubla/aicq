import { redirect } from '@sveltejs/kit';
import { requireOwner } from '$lib/server/harness.js';
/** @type {import('./$types').PageServerLoad} */
export async function load(event) {
  if (!event.cookies.get('fulcra_access_token')) redirect(303, '/');
  await requireOwner(event);
  return {};
}
