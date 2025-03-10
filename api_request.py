import requests
import json

API_KEY = "f87536c"
REQ_URL_INFO = f"http://www.omdbapi.com/?apikey={API_KEY}&t="
REQ_URL_POSTER = f"http://img.omdbapi.com/?apikey={API_KEY}&t="



def get_movie_by_title(title):
    """Get movie information from OMDb API"""
    try:
        url = REQ_URL_INFO + title
        res = requests.get(url)
        # Check if the request was successful
        res.raise_for_status()

        movie_info = res.json()

        # Check if the movie was found
        if movie_info.get('Response') == 'False':
            print(f"Error: {movie_info.get('Error', 'Movie not found')}")
            return None, None, None, None

        title = movie_info['Title']
        year = movie_info['Year']
        rating = movie_info['Rated']
        poster = movie_info.get('Poster', 'N/A')

        return title, year, rating, poster

    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the OMDb API. Please check your internet connection.")
        return None, None, None, None

    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while connecting to the API: {e}")
        return None, None, None, None


