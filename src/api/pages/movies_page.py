from src.api.pages.base_api import BaseAPI

class MoviesPage(BaseAPI):
    def get_popular_movies(self, page=1):
        return self._make_request("/movie/popular", params={"page": page})

    def get_movie_details(self, movie_id):
        return self._make_request(f"/movie/{movie_id}")

    def get_movie_credits(self, movie_id):
        return self._make_request(f"/movie/{movie_id}/credits")

    def get_movie_recommendations(self, movie_id):
        return self._make_request(f"/movie/{movie_id}/recommendations")

    def rate_movie(self, movie_id, rating):
        json_data = {"value": rating}
        return self._make_request(f"/movie/{movie_id}/rating", method="POST", json_data=json_data)

    def delete_movie_rating(self, movie_id):
        return self._make_request(f"/movie/{movie_id}/rating", method="DELETE")