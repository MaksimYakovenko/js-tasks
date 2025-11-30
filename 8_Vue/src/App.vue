<template>
  <div class="app">
    <h1>Список покупок</h1>

    <AddItemForm @add-item="handleAddItem"/>

    <FilterButtons
        :filter="filter"
        @change-filter="filter = $event"
    />

    <ShoppingList
        :items="items"
        :filter="filter"
        @toggle-bought="handleToggleBought"
        @remove-item="handleRemoveItem"
    />

    <div class="total">
      Загальна сума куплених товарів:
      <strong>{{ totalBoughtSum }}</strong> грн
    </div>
  </div>
</template>

<script>
import AddItemForm from "./components/AddItemForm.vue";
import FilterButtons from "./components/FilterButtons.vue";
import ShoppingList from "./components/ShoppingList.vue";

export default {
  name: "App",
  components: {
    AddItemForm,
    FilterButtons,
    ShoppingList,
  },
  data() {
    return {
      filter: "all",
      items: [],
    };
  },
  computed: {
    totalBoughtSum() {
      return this.items
          .filter((item) => item.bought)
          .reduce((sum, item) => sum + (item.price || 0), 0);
    },
  },
  methods: {
    handleAddItem(payload) {
      const name = payload.name.trim();
      if (!name) return;

      this.items.push({
        name,
        price: Number(payload.price) || 0,
        bought: false,
        date: null,
      });
    },
    handleToggleBought(index) {
      const item = this.items[index];
      if (!item) return;

      item.bought = !item.bought;
      item.date = item.bought ? new Date().toLocaleString() : null;
    },
    handleRemoveItem(index) {
      this.items.splice(index, 1);
    },
  },
};
</script>

<style scoped>
.app {
  max-width: 600px;
  margin: 0 auto;
  font-family: sans-serif;
}

.form input {
  margin-right: 8px;
}

.filters button {
  margin-right: 8px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 8px;
}

li button {
  margin-left: 8px;
}

.total {
  margin-top: 16px;
}
</style>
