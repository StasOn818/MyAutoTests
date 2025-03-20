# tests/test_tmdb_api.py
import pytest
from src.api.pages.movies_page import MoviesPage
from src.api.pages.tv_page import TVPage
from src.api.pages.search_page import SearchPage
from src.api.config.settings import API_KEY, ACCESS_TOKEN
from src.logger import setup_logger

# Initialize logger for tests
logger = setup_logger("TMDb_Tests")

@pytest.fixture
def movies_page():
    return MoviesPage(api_key=API_KEY, access_token=ACCESS_TOKEN)

@pytest.fixture
def tv_page():
    return TVPage(api_key=API_KEY, access_token=ACCESS_TOKEN)

@pytest.fixture
def search_page():
    return SearchPage(api_key=API_KEY, access_token=ACCESS_TOKEN)

# Tests for MoviesPage
def test_get_popular_movies(movies_page):
    logger.info("Starting test: test_get_popular_movies")
    response = movies_page.get_popular_movies(page=1)
    assert "results" in response
    assert len(response["results"]) > 0
    assert "title" in response["results"][0]
    logger.info("Test test_get_popular_movies completed successfully")

def test_get_movie_details(movies_page):
    logger.info("Starting test: test_get_movie_details")
    movie_id = 157336  # "Interstellar"
    response = movies_page.get_movie_details(movie_id)
    assert response["id"] == movie_id
    assert response["title"] == "Interstellar"
    logger.info("Test test_get_movie_details completed successfully")

def test_rate_movie(movies_page):
    logger.info("Starting test: test_rate_movie")
    movie_id = 157336  # "Interstellar"
    rating = 8.5
    response = movies_page.rate_movie(movie_id, rating)
    assert response["success"] is True
    assert response["status_code"] == 1
    logger.info("Test test_rate_movie completed successfully")

def test_delete_movie_rating(movies_page):
    logger.info("Starting test: test_delete_movie_rating")
    movie_id = 157336  # "Interstellar"
    response = movies_page.delete_movie_rating(movie_id)
    assert response["success"] is True
    assert response["status_code"] == 13
    logger.info("Test test_delete_movie_rating completed successfully")

# Tests for TVPage
def test_get_popular_tv_shows(tv_page):
    logger.info("Starting test: test_get_popular_tv_shows")
    response = tv_page.get_popular_tv_shows(page=1)
    assert "results" in response
    assert len(response["results"]) > 0
    logger.info("Test test_get_popular_tv_shows completed successfully")

# Tests for SearchPage
def test_search_movie(search_page):
    logger.info("Starting test: test_search_movie")
    response = search_page.search_movie("Interstellar", year=2014)
    assert "results" in response
    assert any("Interstellar" in movie["title"] for movie in response["results"])
    logger.info("Test test_search_movie completed successfully")