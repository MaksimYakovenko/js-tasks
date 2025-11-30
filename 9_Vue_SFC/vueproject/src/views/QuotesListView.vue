<template>
  <div>
    <h2>Quotes list (page {{ page }})</h2>

    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else>
      <div class="quotes-grid">
        <article
            v-for="quote in quotes"
            :key="quote.id"
            class="quote-card"
        >
          <p class="quote-body">“{{ quote.body }}”</p>
          <p class="quote-author">— {{ quote.author || "Unknown" }}</p>
          <div v-if="quote.tags?.length" class="quote-tags">
            <span v-for="tag in quote.tags" :key="tag" class="tag">
              #{{ tag }}
            </span>
          </div>
        </article>
      </div>

      <div class="pagination">
        <button :disabled="page === 1 || loading" @click="goToPrevPage">
          Prev
        </button>
        <span>Page {{ page }}</span>
        <button :disabled="isLastPage || loading" @click="goToNextPage">
          Next
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { fetchQuotes } from "../api/favqs";

const quotes = ref([]);
const page = ref(1);
const isLastPage = ref(false);
const loading = ref(false);
const error = ref("");

async function loadQuotes() {
  loading.value = true;
  error.value = "";
  try {
    const data = await fetchQuotes(page.value);
    quotes.value = data.quotes;
    isLastPage.value = data.last_page;
  } catch (e) {
    console.error(e);
    error.value = "Failed to load quotes. Please try again.";
  } finally {
    loading.value = false;
  }
}

function goToPrevPage() {
  if (page.value > 1) {
    page.value -= 1;
    loadQuotes();
  }
}

function goToNextPage() {
  if (!isLastPage.value) {
    page.value += 1;
    loadQuotes();
  }
}

onMounted(() => {
  loadQuotes();
});
</script>

<style scoped>
.quotes-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}

.quote-card {
  border-radius: 8px;
  padding: 1rem;
  background: #f2f2f2;
}

.quote-body {
  font-size: 1rem;
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

.pagination {
  margin-top: 1.5rem;
  display: flex;
  gap: 1rem;
  align-items: center;
}
</style>
