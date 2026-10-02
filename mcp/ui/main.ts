import { App, applyDocumentTheme, applyHostStyleVariables } from '@modelcontextprotocol/ext-apps';
import { OpenAIExtensions } from '@openai/mcp-extensions/app';
import './style.css';

const app = new App({ name: 'AICQ', version: '0.1.0' });
new OpenAIExtensions(app);
const status = document.querySelector<HTMLElement>('#status')!;
const account = document.querySelector<HTMLElement>('#account')!;
const setup = document.querySelector<HTMLButtonElement>('#setup')!;
const refresh = document.querySelector<HTMLButtonElement>('#refresh')!;

function render(data: Record<string, unknown> | undefined) {
  if (!data || typeof data.owner_id !== 'string' || typeof data.agent_id !== 'string') {
    status.textContent = 'Account information was unavailable. Refresh to retry.';
    return;
  }
  document.querySelector('#owner')!.textContent = data.owner_id;
  document.querySelector('#agent')!.textContent = data.agent_id;
  account.hidden = false;
  setup.hidden = data.setup_complete === true;
  status.textContent =
    data.setup_complete === true
      ? 'Account linked. Your agent address is ready.'
      : 'Account linked. Finish setup to save your agent address.';
}
function theme() {
  const context = app.getHostContext();
  if (context?.theme) applyDocumentTheme(context.theme);
  if (context?.styles?.variables) applyHostStyleVariables(context.styles.variables);
}
async function call(name: string) {
  setup.disabled = refresh.disabled = true;
  try {
    const result = await app.callServerTool({ name, arguments: {} });
    if (result.isError) throw new Error('The account request failed. Reconnect or retry setup.');
    render(result.structuredContent);
  } catch (error) {
    status.textContent =
      error instanceof Error ? error.message : 'Could not load your account. Retry or reconnect.';
  } finally {
    setup.disabled = refresh.disabled = false;
  }
}
setup.addEventListener('click', () => void call('aicq_setup'));
refresh.addEventListener('click', () => void call('aicq_identity'));
app.ontoolresult = (result) => {
  if (result.isError) {
    status.textContent = 'Account request failed. Reconnect and retry.';
    return;
  }
  render(result.structuredContent);
};
app.addEventListener('hostcontextchanged', theme);
try {
  await app.connect();
  theme();
} catch {
  status.textContent =
    'Open AICQ in an MCP App host to link your account. Tools also work without this panel.';
}
