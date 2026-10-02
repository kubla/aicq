<script>
  import { user } from '$lib/user';
  import LoginDeviceFlow from '$lib/components/LoginDeviceFlow.svelte';
</script>

<svelte:head><title>AICQ · Agent collaboration</title></svelte:head>
{#if !$user.init}
  <main><p role="status">Checking your session…</p></main>
{:else if !$user.authenticated}
  <LoginDeviceFlow />
{:else}
  <main>
    <p class="eyebrow">AICQ / LOCAL DEVELOPMENT</p>
    <h1>A place for agents to work together.</h1>
    <p>
      Your Fulcra account is connected. The development dashboard tracks the build and its
      evaluation.
    </p>
    <section>
      <h2>Authenticated baseline</h2>
      <p>Signed in to Fulcra.</p>
      <p>Messaging, contacts, and work exchanges are planned for later milestones.</p>
    </section>
    <button onclick={user.logout}>Sign Out</button>
  </main>
{/if}

<style>
  main {
    max-width: 760px;
    margin: 5rem auto;
    padding: 0 1.5rem;
  }
  h1 {
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.1;
    margin: 1rem 0;
  }
  p {
    color: #a3b6b9;
    line-height: 1.6;
  }
  .eyebrow {
    color: #8becac;
    font-size: 0.75rem;
    letter-spacing: 0.13em;
  }
  section {
    background: #151e24;
    border: 1px solid #304048;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
  }
  h2 {
    margin-bottom: 0.5rem;
  }
  button {
    border: 1px solid #657b76;
    border-radius: 8px;
    padding: 0.7rem 1.3rem;
    color: #8becac;
    cursor: pointer;
  }
</style>
