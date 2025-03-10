from _storage.istorage import IStorage
import os
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            self._save_db({})


    def _load_db(self):
        """load data from json file"""
        with open(self.file_path, "r") as file:
            return json.load(file)


    def _save_db(self, movies):

        # Get the directory part of the path
        directory = os.path.dirname(self.file_path)

        # Only create directories if there's a non-empty directory path
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(self.file_path, "w") as new_file:
            json.dump(movies, new_file, indent=4)


    def list_movies(self):
        return self._load_db()


    def add_movie(self, title, year, rating):
        movies = self._load_db()
        movies[title] = {
            'year': year,
            'rating': rating
        }
        self._save_db(movies)


    def delete_movie(self, title):
        movies = self._load_db()
        if title in movies:
            del movies[title]
            self._save_db(movies)


    def update_movie(self, title, rating):
        movies = self._load_db()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_db(movies)