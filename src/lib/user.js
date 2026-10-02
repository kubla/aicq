import { env } from '$env/dynamic/public';
import { writable } from 'svelte/store';
import { Auth0DeviceFlow } from '$lib/auth0-device-flow.js';

// Verified display state only. Credentials remain in the HTTP-only cookie
// and temporary device-client memory; nothing is written to localStorage.
const store = writable({ init: false, authenticated: false });
/** @type {Auth0DeviceFlow | undefined} */
let auth0;
function client() {
  return (auth0 ??= new Auth0DeviceFlow({
    domain: env.PUBLIC_AUTH0_DOMAIN || '',
    clientId: env.PUBLIC_AUTH0_CLIENT_ID || '',
    audience: env.PUBLIC_FULCRA_API_ENDPOINT || ''
  }));
}
async function init() {
  client();
  let authenticated = false;
  try {
    const response = await fetch('/api/auth/check');
    if (response.ok) authenticated = (await response.json()).authenticated === true;
  } catch {
    /* Failed checks never establish authentication. */
  }
  store.set({ init: true, authenticated });
}
/** @param {Window | null} popup */
async function startLogin(popup) {
  const started = Date.now();
  if (popup && !popup.closed) popup.location.href = `https://${env.PUBLIC_AUTH0_DOMAIN}/v2/logout`;
  const info = await client().startDeviceFlow();
  if (popup && !popup.closed) {
    const remaining = 1200 - (Date.now() - started);
    if (remaining > 0) await new Promise((resolve) => setTimeout(resolve, remaining));
    if (!popup.closed) popup.location.href = info.verificationUri;
  }
  return info;
}
/** @param {string} deviceCode @param {number} interval */
async function completeLogin(deviceCode, interval) {
  await client().pollForToken(deviceCode, interval);
  const accessToken = await client().getTokenSilently();
  const saved = await fetch('/api/auth/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ accessToken })
  });
  if (!saved.ok) throw new Error('Could not establish a verified session');
  store.set({ init: true, authenticated: true });
}
async function logout() {
  const popup = window.open(
    `https://${env.PUBLIC_AUTH0_DOMAIN}/v2/logout`,
    'auth0-logout',
    'width=500,height=600'
  );
  const refreshToken = client().getRefreshToken();
  if (refreshToken) {
    try {
      await fetch('/api/auth/revoke', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refreshToken })
      });
    } catch {
      /* Local logout still proceeds if revocation is unavailable. */
    }
  }
  const cleared = await fetch('/api/auth/token', { method: 'DELETE' });
  if (!cleared.ok) throw new Error('Could not clear the session');
  await client().logout();
  store.set({ init: true, authenticated: false });
  if (popup)
    setTimeout(() => {
      if (!popup.closed) popup.close();
    }, 1500);
}
export const user = { subscribe: store.subscribe, init, startLogin, completeLogin, logout };
