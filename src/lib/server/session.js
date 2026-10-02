import { env } from '$env/dynamic/public';
import { error } from '@sveltejs/kit';

/** Validate the cookie against Fulcra rather than trusting decoded JWT claims.
 * @param {string | undefined} token
 * @param {typeof fetch} fetcher
 */
export async function getIdentity(token, fetcher = fetch) {
  if (!token) error(401, 'Sign in to continue');
  let response;
  try {
    response = await fetcher(`${env.PUBLIC_FULCRA_API_ENDPOINT}user/v1alpha1/info`, {
      headers: { Authorization: `Bearer ${token}` },
      signal: AbortSignal.timeout(10000)
    });
  } catch {
    error(502, 'Fulcra is unavailable; please try again');
  }
  if (response.status === 401 || response.status === 403)
    error(401, 'Session expired; sign in again');
  if (!response.ok) error(502, 'Could not verify the Fulcra account');
  const info = await response.json();
  if (typeof info.userid !== 'string') error(502, 'Fulcra did not return an account identity');
  return { userid: info.userid, status: info.status, timezone: info.preferences?.timezone };
}
