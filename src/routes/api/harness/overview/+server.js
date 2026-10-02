import { getWorkspaceText } from '$lib/server/harness.js';
/** @type {import('./$types').RequestHandler} */
export const GET = (event) => getWorkspaceText(event, 'overview.md');
