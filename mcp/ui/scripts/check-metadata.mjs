import { readFile } from 'node:fs/promises';
import {
  OpenAIUiToolMetadataSchema,
  OpenAIUiResourceMetadataSchema
} from '@openai/mcp-extensions/server';
const metadata = JSON.parse(
  await readFile(new URL('../../aicq_mcp/ui-metadata.json', import.meta.url), 'utf8')
);
for (const entry of ['global', 'thread'])
  OpenAIUiToolMetadataSchema.parse(metadata[entry]['openai/ui']);
OpenAIUiResourceMetadataSchema.parse(metadata.resource['openai/ui']);
console.log('Server UI metadata passed OpenAI SDK schema validation');
