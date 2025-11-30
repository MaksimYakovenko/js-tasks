<template>
  <div>
    <h2>Random quote</h2>

    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else-if="quote" class="random-card">
      <p class="quote-body">“{{ quote.body }}”</p>
      <p class="quote-author">— {{ quote.author || "Unknown" }}</p>

      <div v-if="quote.tags?.length" class="quote-tags">
        <span v-for="tag in quote.tags" :key="tag" class="tag">
          #{{ tag }}
        </span>
      </div>
    </div>

    <button class="random-btn" :disabled="loading" @click="loadRandom">
      Random quote
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { fetchRandomQuote } from "../api/favqs";

const quote = ref(null);
const loading = ref(false);
const error = ref("");

async function loadRandom() {
  loading.value = true;
  error.value = "";
  try {
    const data = await fetchRandomQuote();
    // API повертає { quote: {...} }
    quote.value = data.quote;
  } catch (e) {
    console.error(e);
    error.value = "Failed to load random quote. Please try again.";
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  loadRandom();
});
</script>

<style scoped>
.random-card {
  margin-bottom: 1rem;
  padding: 1.5rem;
  border-radius: 8px;
  background: #f2f2f2;
}

.quote-body {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.quote-author {
  font-style: italic;
  margin-bottom: 0.5rem;
}

.quote-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.tag {
  font-size: 0.8rem;
  background: #e0e0e0;
  border-radius: 999px;
  padding: 0.1rem 0.5rem;
}

.random-btn {
  padding: 0.6rem 1.2rem;
  border-radius: 6px;
  border: none;
  background: #42b883;
  color: white;
  cursor: pointer;
  font-weight: 500;
}

.random-btn:disabled {
  opacity: 0.7;
  cursor: default;
}
</style>
