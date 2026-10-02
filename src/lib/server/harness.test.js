import { describe, expect, it, vi } from 'vitest';

vi.mock('$env/dynamic/private', () => ({ env: { OWNER_USER_ID: 'owner' } }));
vi.mock('$env/dynamic/public', () => ({
  env: {
    PUBLIC_FULCRA_API_ENDPOINT: 'https://api.fulcradynamics.com/',
    PUBLIC_HARNESS_ANNOTATION_ID: 'MomentAnnotation/harness',
    PUBLIC_WORKSPACE_PATH: 'workspace/aicq'
  }
}));

import { getRuns, getWorkspaceText } from './harness.js';
import { GET as owner } from '../../routes/api/harness/owner/+server.js';
import { POST as saveSession } from '../../routes/api/auth/token/+server.js';

/** @param {string | undefined} token @param {ReturnType<typeof vi.fn>} fetcher */
function event(token, fetcher) {
  return /** @type {import('@sveltejs/kit').RequestEvent} */ (
    /** @type {unknown} */ ({
      cookies: { get: () => token, set: vi.fn() },
      fetch: fetcher,
      url: new URL(
        'http://127.0.0.1:6173/api/harness/runs?annotation_id=unrelated&workspace_path=private'
      ),
      request: new Request('http://127.0.0.1:6173/api/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ accessToken: token })
      })
    })
  );
}
/** @param {string} userid */
const info = (userid) =>
  new Response(
    JSON.stringify({
      userid,
      preferences: { timezone: 'America/New_York' },
      intercom_token: 'never-forward-this'
    })
  );

describe('owner dashboard access boundary', () => {
  it('blocks unauthenticated requests before accessing Fulcra data', async () => {
    const fetcher = vi.fn();
    await expect(getRuns(event(undefined, fetcher))).rejects.toMatchObject({ status: 401 });
    expect(fetcher).not.toHaveBeenCalled();
  });
  it('denies a verified non-owner on all private data routes', async () => {
    const fetcher = vi.fn(() => Promise.resolve(info('another-owner')));
    for (const action of [
      getRuns,
      /** @param {import('@sveltejs/kit').RequestEvent} e */ (e) =>
        getWorkspaceText(e, 'overview.md'),
      /** @param {import('@sveltejs/kit').RequestEvent} e */ (e) =>
        getWorkspaceText(e, 'outstanding-issues.md')
    ]) {
      await expect(action(event('valid-non-owner', fetcher))).rejects.toMatchObject({
        status: 403
      });
    }
    expect(fetcher.mock.calls).toHaveLength(3);
  });
  it('does not trust a forged owner claim or install an unvalidated session', async () => {
    const forged = 'header.eyJmdWxjcmFkeW5hbWljcy5jb20vdXNlcmlkIjoib3duZXIifQ.forged';
    const fetcher = vi.fn(() => Promise.resolve(new Response('', { status: 401 })));
    const requestEvent = event(forged, fetcher);
    await expect(getRuns(requestEvent)).rejects.toMatchObject({ status: 401 });
    await expect(owner(requestEvent)).rejects.toMatchObject({ status: 401 });
    await expect(saveSession(requestEvent)).rejects.toMatchObject({ status: 401 });
    expect(requestEvent.cookies.set).not.toHaveBeenCalled();
  });
  it('uses configured annotation scope even with arbitrary caller resource parameters', async () => {
    const fetcher = vi
      .fn()
      .mockResolvedValueOnce(info('owner'))
      .mockResolvedValueOnce(new Response('[]'));
    const response = await getRuns(event('valid-owner', fetcher));
    expect(response.status).toBe(200);
    expect(fetcher.mock.calls[1][0]).toContain('/event/MomentAnnotation%2Fharness?');
    expect(fetcher.mock.calls[1][0]).not.toContain('unrelated');
    expect(response.headers.get('cache-control')).toBe('no-store');
  });
  it('reports missing canonical files rather than showing successful empty panels', async () => {
    const fetcher = vi
      .fn()
      .mockResolvedValueOnce(info('owner'))
      .mockResolvedValueOnce(new Response('{"files":[]}'));
    await expect(
      getWorkspaceText(event('valid-owner', fetcher), 'overview.md')
    ).rejects.toMatchObject({ status: 404 });
    expect(fetcher.mock.calls[1][0]).toContain('path=%2Fworkspace%2Faicq');
  });
  it('keeps owner identity and upstream credentials out of the navigation result', async () => {
    const response = await owner(
      event(
        'valid-owner',
        vi.fn(() => Promise.resolve(info('owner')))
      )
    );
    expect(await response.json()).toEqual({ isOwner: true });
  });
});
