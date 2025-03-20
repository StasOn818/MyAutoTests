import requests
from src.api.config.settings import API_KEY, BASE_URL, DEFAULT_LANGUAGE, TIMEOUT

class TMDbClient:
    def __init__(self, api_key=API_KEY, base_url=BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint, method="GET", params=None):
        """Універсальна функція для надсилання запитів до API."""
        default_params = {"api_key": self.api_key, "language": DEFAULT_LANGUAGE}
        if params:
            default_params.update(params)

        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method, url, params=default_params, timeout=TIMEOUT
        )
        response.raise_for_status()  # Викликає виняток при помилці HTTP
        return response.json()

    def get_popular_movies(self, page=1):
        """Отримати список популярних фільмів."""
        return self._make_request("/movie/popular", params={"page": page})

    def search_movie(self, query, year=None):
        """Пошук фільму за назвою та (опціонально) роком."""
        params = {"query": query}
        if year:
            params["year"] = year
        return self._make_request("/search/movie", params=params)

    def get_movie_details(self, movie_id):
        """Отримати деталі фільму за його ID."""
        return self._make_request(f"/movie/{movie_id}")

    def get_movie_credits(self, movie_id):
        """Отримати акторів і команду фільму за його ID."""
        return self._make_request(f"/movie/{movie_id}/credits")

