<script>
  import './layout.css';
  import { onMount } from 'svelte';
  import { user } from '$lib/user';
  import OwnerNav from '$lib/components/OwnerNav.svelte';
  let { children } = $props();
  onMount(() => {
    user.init();
  });
</script>

<OwnerNav />
{@render children()}

<style>
  :global(body) {
    background: #0e151b;
    color: #e6eeee;
    min-height: 100vh;
  }
</style>
