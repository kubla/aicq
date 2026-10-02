import { copyFile } from 'node:fs/promises';
await copyFile(new URL('../dist/index.html', import.meta.url), new URL('../../aicq_mcp/app.html', import.meta.url));
console.log('Compiled MCP App copied into the server package');
