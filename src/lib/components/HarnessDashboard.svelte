<script>
  /* eslint-disable svelte/no-at-html-tags -- Both markdown panels pass through DOMPurify in markdown(). */
  import { onMount } from 'svelte';
  import { marked } from 'marked';
  import DOMPurify from 'dompurify';
  /** @typedef {{id: string, run_id: string, step: string, status: string, detail: string, evidence: string, timestamp: string}} HarnessEvent */
  /** @typedef {{id: string, events: HarnessEvent[]}} Run */
  /** @type {Run[]} */
  let runs = $state([]);
  let selected = $state('');
  let overview = $state('');
  let issues = $state('');
  let failure = $state('');
  let updated = $state('');
  let loading = $state(true);
  const current = $derived(runs.find((run) => run.id === selected));
  /** @param {string} value */
  function markdown(value) {
    return value ? DOMPurify.sanitize(marked.parse(value, { async: false })) : '';
  }
  /** @param {Run} run */
  function status(run) {
    const latest = new Map(run.events.map((event) => [event.step, event]));
    if (latest.has('MARK_COMPLETE')) return 'Milestone complete';
    if (latest.has('ESCALATE')) return 'Needs attention';
    if (latest.has('RUN_INCOMPLETE')) return 'Incomplete';
    if (latest.has('RUN_COMPLETE'))
      return latest.get('REVIEW')?.status === 'failed'
        ? 'Milestone incomplete · retry available'
        : 'Run closed';
    if (run.id.startsWith('preflight-')) return 'Preflight evidence';
    return 'In progress';
  }
  async function load() {
    try {
      const responses = await Promise.all(
        ['runs', 'overview', 'issues'].map((part) => fetch(`/api/harness/${part}`))
      );
      for (const response of responses) {
        if (!response.ok)
          throw new Error(
            response.status === 401
              ? 'Session expired. Return to AICQ and sign in again.'
              : `Dashboard could not refresh (${response.status}).`
          );
      }
      const data = await responses[0].json();
      /** @type {Map<string, Run>} */
      // This local grouping map is replaced in one state assignment after parsing.
      // eslint-disable-next-line svelte/prefer-svelte-reactivity
      const groups = new Map();
      for (const record of Array.isArray(data) ? data : data.records || []) {
        try {
          const event = JSON.parse(record.note);
          if (!event.run_id || !event.step || !event.status || typeof event.evidence !== 'string')
            continue;
          if (!groups.has(event.run_id)) groups.set(event.run_id, { id: event.run_id, events: [] });
          groups
            .get(event.run_id)
            ?.events.push({ ...event, id: record.id, timestamp: record.recorded_at });
        } catch {
          /* Ignore unrelated or malformed annotations. */
        }
      }
      for (const run of groups.values())
        run.events.sort((a, b) => a.timestamp.localeCompare(b.timestamp));
      runs = [...groups.values()].sort((a, b) =>
        b.events[0].timestamp.localeCompare(a.events[0].timestamp)
      );
      if (!groups.has(selected)) selected = runs[0]?.id || '';
      overview = await responses[1].text();
      issues = await responses[2].text();
      updated = new Date().toLocaleTimeString();
      failure = '';
    } catch (error) {
      failure = error instanceof Error ? error.message : 'Dashboard could not refresh.';
    } finally {
      loading = false;
    }
  }
  onMount(() => {
    let active = true;
    /** @type {ReturnType<typeof setTimeout>} */
    let timer;
    async function refresh() {
      await load();
      if (active) timer = setTimeout(refresh, 5000);
    }
    refresh();
    return () => {
      active = false;
      clearTimeout(timer);
    };
  });
</script>

<main class="dashboard">
  <header>
    <p class="eyebrow">AICQ / DEVELOPMENT</p>
    <h1>Harness Dashboard</h1>
    <p>Recorded runs and evaluation evidence from the canonical Fulcra workspace.</p>
  </header>
  {#if failure}<p role="alert" class="failure">{failure} Previous data may be stale.</p>{/if}
  {#if loading}<p role="status">Loading live harness records…</p>{/if}
  {#if updated}<p class="updated">Last refreshed {updated} · refreshes every 5 seconds</p>{/if}
  {#if overview}<section class="panel markdown">{@html markdown(overview)}</section>{/if}
  <div class="columns">
    <aside class="panel">
      <h2>Recent runs</h2>
      {#each runs as run (run.id)}<button
          class:active={selected === run.id}
          onclick={() => (selected = run.id)}
          ><span>{status(run)}</span><small>{run.id}</small><small
            >{new Date(run.events[0].timestamp).toLocaleString()}</small
          ></button
        >{/each}
      {#if !loading && runs.length === 0}<p>No recorded runs found.</p>{/if}
    </aside>
    <section class="panel events">
      <h2>Run evidence</h2>
      {#if current}<p class="run-id">{current.id}</p>
        <p class="run-status">{status(current)}</p>
        {#each current.events as event (event.id)}<article>
            <div class="event-heading">
              <h3>{event.step}</h3>
              <span class="badge {event.status}">{event.status}</span>
            </div>
            <small>{new Date(event.timestamp).toLocaleString()}</small>
            <p>{event.detail}</p>
            <details open>
              <summary>Evidence</summary>
              <p class="evidence">{event.evidence}</p>
            </details>
          </article>{/each}
      {/if}
    </section>
  </div>
  {#if issues}<section class="panel markdown">
      <h2>Outstanding issues</h2>
      {@html markdown(issues)}
    </section>{/if}
</main>

<style>
  .dashboard {
    max-width: 1200px;
    margin: auto;
    padding: 2rem 1rem;
    color: #e6eeee;
  }
  h1 {
    font-size: 2rem;
    margin: 0.3rem 0;
  }
  header p,
  .updated,
  small {
    color: #a3b6b9;
  }
  .eyebrow {
    letter-spacing: 0.14em;
    font-size: 0.75rem;
    color: #8becac;
  }
  .updated {
    font-size: 0.8rem;
    margin: 1rem 0;
  }
  .panel {
    background: #151e24;
    border: 1px solid #304048;
    border-radius: 12px;
    padding: 1.3rem;
    margin-bottom: 1rem;
    min-width: 0;
  }
  .columns {
    display: grid;
    grid-template-columns: 280px minmax(0, 1fr);
    gap: 1rem;
  }
  h2 {
    font-size: 1.15rem;
    margin-bottom: 1rem;
  }
  h3 {
    font-weight: 600;
  }
  button {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    width: 100%;
    text-align: left;
    padding: 0.9rem;
    border: 1px solid #304048;
    border-radius: 8px;
    margin-bottom: 0.7rem;
    cursor: pointer;
  }
  button.active {
    border-color: #8becac;
    background: #22332e;
  }
  small,
  .run-id {
    font-size: 0.75rem;
    overflow-wrap: anywhere;
  }
  article {
    border-top: 1px solid #304048;
    padding: 1rem 0;
  }
  .event-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }
  .badge {
    font-size: 0.75rem;
    border-radius: 4px;
    padding: 0.2rem 0.6rem;
    background: #303e48;
  }
  .completed {
    color: #8becac;
  }
  .failed,
  .failure {
    color: #ffb4ab;
  }
  .started {
    color: #f5d798;
  }
  article p {
    margin: 0.7rem 0;
  }
  summary {
    font-size: 0.8rem;
    color: #a3b6b9;
  }
  .evidence {
    font-size: 0.85rem;
    line-height: 1.6;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
  .run-status {
    color: #8becac;
  }
  .markdown :global(h1),
  .markdown :global(h2) {
    font-size: 1.15rem;
    margin-bottom: 0.7rem;
  }
  .markdown :global(p) {
    margin: 0.6rem 0;
  }
  .markdown :global(ul) {
    padding-left: 1.4rem;
    list-style: disc;
  }
  .markdown :global(a) {
    color: #8becac;
  }
  @media (max-width: 800px) {
    .columns {
      grid-template-columns: 1fr;
    }
  }
</style>
