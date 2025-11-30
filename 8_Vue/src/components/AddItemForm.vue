<template>
  <div class="form">
    <form @submit.prevent="onSubmit">
      <input
          v-model="name"
          type="text"
          placeholder="Назва товару"
      />
      <input
          v-model.number="price"
          type="number"
          min="0"
          placeholder="Вартість"
      />
      <button type="submit">Додати</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["add-item"]);

const name = ref("");
const price = ref(null);

const onSubmit = () => {
  const trimmed = name.value.trim();
  if (!trimmed) return;

  emit("add-item", {
    name: trimmed,
    price: Number(price.value) || 0,
  });

  name.value = "";
  price.value = null;
};
</script>

<style scoped>
form input {
  margin-right: 8px;
}
</style>
