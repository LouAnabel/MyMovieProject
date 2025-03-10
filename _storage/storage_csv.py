from _storage.istorage import IStorage
import os
import csv


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            self._save_db({})

    def _load_db(self):
        """Load data from csv file into a dictionary"""
        movies = {}
        # Handle the case where the file might be empty
        if os.path.getsize(self.file_path) > 0:
            with open(self.file_path, "r", newline='') as file:
                reader = csv.reader(file)
                # Skip header row
                header = next(reader, None)
                if header:  # Only proceed if there's data
                    for row in reader:
                        if len(row) >= 4:  # Ensure row has enough columns
                            title, year, rating, poster = row[0], row[1], row[2], row[3]
                            movies[title] = {
                                'year': year,
                                'rating': rating,
                                'poster': poster
                            }
        return movies


    def _save_db(self, movies):
        """Save dictionary data to csv file"""
        # Get the directory part of the path
        directory = os.path.dirname(self.file_path)

        # Only create directories if there's a non-empty directory path
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(self.file_path, "w", newline='') as new_file:
            writer = csv.writer(new_file)
            # Write header
            writer.writerow(['title', 'year', 'rating', 'poster'])
            # Write data
            for title, data in movies.items():
                writer.writerow([
                    title,
                    data['year'],
                    data['rating'],
                    data['poster']
                ])


    def list_movies(self):
        return self._load_db()


    def add_movie(self, title, year, rating, poster):
        movies = self._load_db()
        movies[title] = {
            'year': year,
            'rating': rating,
            'poster': poster
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



