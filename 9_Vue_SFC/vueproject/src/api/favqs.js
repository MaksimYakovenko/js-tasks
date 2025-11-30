import axios from "axios";

const API_BASE_URL = "/api";

export async function fetchQuotes(page = 1) {
    console.log("REQUEST TO:", `${API_BASE_URL}/quotes?page=${page}`);

    const response = await axios.get(`${API_BASE_URL}/quotes`, {
        params: { page },
        headers: {
            Authorization: `Token token=8271105d42e221bc42de585e08a3c97c`,
        },
    });

    return response.data;
}

export async function fetchRandomQuote() {
    const response = await axios.get(`${API_BASE_URL}/qotd`, {
        headers: {
            Authorization: `Token token=8271105d42e221bc42de585e08a3c97c`,
        },
    });

    return response.data;
}
