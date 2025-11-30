<template>
  <div>
    <ul v-if="filteredItems.length > 0">
      <li
          v-for="entry in filteredItems"
          :key="entry.index"
      >
        <span :class="{ boughtClass: entry.item.bought }">
          <strong>{{ entry.item.name }}</strong>
          — {{ entry.item.price }} грн
          — статус:
          <span v-if="entry.item.bought">куплено</span>
          <span v-else>не куплено</span>
          <span v-if="entry.item.date">
            (дата: {{ entry.item.date }})
          </span>
        </span>

        <button @click="$emit('toggle-bought', entry.index)">
          {{ entry.item.bought ? 'Позначити як не куплено' : 'Позначити як куплено' }}
        </button>
        <button @click="$emit('remove-item', entry.index)">
          Видалити
        </button>
      </li>
    </ul>

    <p v-else>
      <span v-if="props.items.length === 0">
        Список порожній.
      </span>
      <span v-else>
        Немає покупок для відображення.
      </span>
    </p>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  items: {
    type: Array,
    required: true,
  },
  filter: {
    type: String,
    default: "all",
  },
});

const filteredItems = computed(() => {
  const withIndex = props.items.map((item, index) => ({ item, index }));

  if (props.filter === "bought") {
    return withIndex.filter((entry) => entry.item.bought);
  }
  if (props.filter === "notBought") {
    return withIndex.filter((entry) => !entry.item.bought);
  }
  return withIndex;
});
</script>

<style scoped>
.boughtClass {
  color: gray;
  text-decoration: line-through;
}
</style>
