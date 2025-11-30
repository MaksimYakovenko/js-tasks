import { createRouter, createWebHistory } from "vue-router";
import QuotesListView from "../views/QuotesListView.vue";
import RandomQuoteView from "../views/RandomQuoteView.vue";

const routes = [
    {
        path: "/",
        name: "quotes-list",
        component: QuotesListView,
    },
    {
        path: "/random",
        name: "random-quote",
        component: RandomQuoteView,
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;
