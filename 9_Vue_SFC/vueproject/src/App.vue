<template>
  <div class="app">
    <header class="app-header">
      <h1>FavQs Quotes</h1>
      <nav class="nav">
        <RouterLink to="/">Quotes list</RouterLink>
        <RouterLink to="/random">Random quote</RouterLink>
      </nav>
    </header>

    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.app-header {
  background: #42b883;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav {
  display: flex;
  gap: 1rem;
}

.nav a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}

.nav a.router-link-active {
  text-decoration: underline;
}

.app-main {
  padding: 2rem;
}
</style>
