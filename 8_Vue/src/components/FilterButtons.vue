<template>
  <div class="filters">
    <button
        :class="{ active: filter === 'all' }"
        @click="$emit('change-filter', 'all')"
    >
      Усі
    </button>
    <button
        :class="{ active: filter === 'bought' }"
        @click="$emit('change-filter', 'bought')"
    >
      Куплені
    </button>
    <button
        :class="{ active: filter === 'notBought' }"
        @click="$emit('change-filter', 'notBought')"
    >
      Не куплені
    </button>
  </div>
</template>

<style scoped>
button {
  margin-right: 8px;
}

.active {
  font-weight: bold;
  text-decoration: underline;
}
</style>
