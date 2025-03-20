from src.api.pages.base_api import BaseAPI

class TVPage(BaseAPI):
    def get_popular_tv_shows(self, page=1):
        return self._make_request("/tv/popular", params={"page": page})

    def get_tv_show_details(self, tv_id):
        return self._make_request(f"/tv/{tv_id}")