<script>
  import { onMount } from 'svelte';
  import * as THREE from 'three';

  let trades = [];

  onMount(async () => {
    const response = await fetch('http://localhost:8080/trades');
    trades = await response.json();
  });
</script>

<main>
  <h1>Trading Dashboard</h1>
  <div class="chart-container">
    <!-- 3D Chart will be rendered here -->
  </div>
  <div class="trades-list">
    {#each trades as trade}
      <div class="trade-item">
        <h2>{trade.symbol}</h2>
        <p>Status: {trade.status}</p>
        <p>Profit: {trade.signal_gained_profit}%</p>
      </div>
    {/each}
  </div>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    background-color: #1a1a1a;
    color: #fff;
  }
  
  .chart-container {
    width: 100%;
    height: 500px;
    background-color: #000;
    margin-bottom: 2rem;
  }
  
  .trades-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
    width: 100%;
  }
  
  .trade-item {
    background-color: #2a2a2a;
    padding: 1rem;
    border-radius: 0.5rem;
  }
</style>