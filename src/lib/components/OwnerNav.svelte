<script>
  import { user } from '$lib/user';
  import { resolve } from '$app/paths';
  let isOwner = $state(false);
  $effect(() => {
    let cancelled = false;
    isOwner = false;
    if ($user.init && $user.authenticated) {
      fetch('/api/harness/owner')
        .then(async (response) => {
          const value = response.ok && (await response.json()).isOwner === true;
          if (!cancelled) isOwner = value;
        })
        .catch(() => {
          if (!cancelled) isOwner = false;
        });
    }
    return () => {
      cancelled = true;
    };
  });
</script>

{#if isOwner}
  <nav aria-label="Owner navigation" class="owner-nav">
    <a href={resolve('/')}>AICQ</a><a href={resolve('/harness')}>Harness Dashboard</a><span
      >Owner · Local development</span
    >
  </nav>
{/if}

<style>
  .owner-nav {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    border-bottom: 1px solid #303a40;
    padding: 1rem 1.5rem;
  }
  a {
    color: #8becac;
  }
  span {
    margin-left: auto;
    font-size: 0.8rem;
    color: #9aadb0;
  }
  @media (max-width: 600px) {
    .owner-nav {
      flex-wrap: wrap;
    }
    span {
      margin-left: 0;
    }
  }
</style>
