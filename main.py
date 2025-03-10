from movie_app import MovieApp
from _storage.storage_csv import StorageCsv


def main():
    """Main function to start the application."""

    storage = StorageCsv('_data/movies.csv')
    movie_app = MovieApp(storage)
    movie_app.run()

    """for json:
    storage = StorageJson('_data/movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()"""

if __name__ == "__main__":
    main()
