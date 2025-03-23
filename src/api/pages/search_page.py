from src.api.pages.base_api import BaseAPI
from src.api.config.settings import DEFAULT_LANGUAGE

class SearchPage(BaseAPI):
    def search_movie(self, query, year=None, language=DEFAULT_LANGUAGE):
        params = {"query": query, "language": language}
        if year:
            params["year"] = year
        return self._make_request("/search/movie", params=params)

    def search_tv(self, query, year=None, language=DEFAULT_LANGUAGE):
        params = {"query": query, "language": language}
        if year:
            params["year"] = year
        return self._make_request("/search/tv", params=params)