import random
from api_request import get_movie_by_title

class MovieApp:
    def __init__(self, storage):
        """Initialize the movie application with a storage implementation.
        storage: An instance of a class implementing IStorage interface"""

        self.storage = storage
        self.commands = {
            1: self._list_movies,
            2: self._add_movie,
            3: self._delete_movie,
            4: self._update_movie,
            5: self._random_movie,
            6: self._search_movie,
            7: self._sort_movies_by_year,
            8: self._generate_website
        }


    def _list_movies(self):
        """List all movies in the database with their details."""
        movies = self.storage.list_movies()

        print(f"{len(movies)} movies in total")
        print("--------------------------")
        for movie, movie_dict in movies.items():
            print(f"{movie} ({movie_dict['year']}): {movie_dict['rating']}")


    def _add_movie(self):
        """Add a new movie to the database."""
        movies = self.storage.list_movies()
        while True:
            search_title = input("Enter movie name to search: ")
            if search_title:
                break
            else:
                print('Movie name must not be empty.')

        # Get movie data from API in file api_requests
        title, year, rating, poster = get_movie_by_title(search_title)

        if not title:
            print("Could not find movie information. Please try again.")
            return

        # Check if movie already exists
        if title in movies:
            print(f"Movie {title} already exists!")
            return

        # Confirm with user
        print(f"\nFound: {title}, ({year}) - Rated: {rating}")
        confirm = input("Add this movie to your collection? (y/n): ")

        if confirm.lower() != 'y':
            print("Movie not added.")
            return

        # Add movie to storage
        self.storage.add_movie(title, year, rating, poster)
        print(f"Movie: {title} successfully added")


    def _delete_movie(self):
        """Delete a movie from the database."""
        movies = self.storage.list_movies()

        name = input("Enter movie name to delete: ")
        if name not in movies:
            print(f"Movie: {name} doesn't exist!")
            return

        self.storage.delete_movie(name)
        print(f"Movie: {name} successfully deleted")


    def _update_movie(self):
        """Update a movie's rating in the database."""
        movies = self.storage.list_movies()

        name = input("Enter movie name: ")
        if name not in movies:
            print(f"Movie {name} doesn't exist!")
            return
        while True:
            try:
                rating = float(input("Enter new movie rating: "))
                break
            except ValueError:
                print('Please enter a valid rating')
        self.storage.update_movie(name, rating)
        print(f"Movie: {name} successfully updated")


    def _random_movie(self):
        """Select a random movie from the database."""
        movies = self.storage.list_movies()

        if not movies:
            print("No movies in database")
            return

        movie = random.choice(list(movies.keys()))
        print(f"Your movie for tonight: {movie}, it's rated {movies[movie]['rating']}")


    def _search_movie(self):
        """Search for a movie by name."""
        movies = self.storage.list_movies()

        query = input("Enter part of movie name: ")
        found = False
        for movie in movies:
            if query.lower() in movie.lower():
                print(f"{movie}, {movies[movie]['rating']}")
                found = True

        if not found:
            print("No movies found matching your search.")


    def _sort_movies_by_year(self):
        """Display movies sorted by release year."""
        movies = self.storage.list_movies()

        if not movies:
            print("No movies in database")
            return

        # Create a list of (title, year) tuples
        movie_year_pairs = [(title, data['year']) for title, data in movies.items()]

        # Sort the list by year (second element in each tuple)
        sorted_movies = sorted(movie_year_pairs, key=lambda x: x[1])

        print("Movies sorted by release year:")
        print("-" * 40)
        for title, year in sorted_movies:
            # Get the full movie data to display
            movie_data = movies[title]
            # Display movie info with title, year and rating
            print(f"{title} ({year}) - Rating: {movie_data['rating']}")


    def _filter_movies(self):
        """Filter movies by year range."""
        movies = self.storage.list_movies()

        if not movies:
            print("No movies in database")
            return

        # Get start year from the user
        while True:
            start_year_input = input("Enter start year (leave blank for no start year): ")
            if start_year_input == '':
                start_year = None
                break
            try:
                start_year = int(start_year_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")

        # Get end year from the user
        while True:
            end_year_input = input("Enter end year (leave blank for no end year): ")
            if end_year_input == '':
                end_year = None
                break
            try:
                end_year = int(end_year_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")

        filtered_movies = []
        for movie in movies.values():
            if (start_year is None or movie['year'] >= start_year) and \
                (end_year is None or movie['year'] <= end_year):
                filtered_movies.append(movie)

        if not filtered_movies:
            print("No movies match your filter criteria.")
            return

        for movie in filtered_movies:
            print(f"{movie['title']} ({movie['year']}): {movie['rating']}")


    def _generate_website(self):
        """Generate a website from the template file based on the movie collection in storage."""

        # Get movies from storage
        movies_dict = self.storage.list_movies()

        # Set the title for the website
        title = "My Movie Collection"

        # Read the template file from the _static folder
        try:
            with open('_static/index_template.html', 'r') as file:
                template = file.read()
        except FileNotFoundError:
            print("Error: _static/index_template.html not found")
            return False

        # Generate the movie grid
        movie_grid_html = ""
        for movie_title, movie_info in movies_dict.items():
            # Extract movie information
            year = movie_info.get('year', 'Unknown')
            poster = movie_info.get('poster', 'N/A')

            # Handle case where poster is 'N/A' or missing
            if poster == 'N/A' or not poster:
                poster = "https://via.placeholder.com/300x445.png?text=No+Poster+Available"

            # Create HTML for this movie
            movie_html = f"""
                <li>
                    <div class="movie">
                        <img class="movie-poster" src="{poster}" alt="{movie_title}"/>
                        <div class="movie-title">{movie_title}</div>
                        <div class="movie-year">{year}</div>
                    </div>
                </li>
                """
            movie_grid_html += movie_html

        # Replace the placeholders in the template
        html_content = template.replace('__TEMPLATE_TITLE__', title)
        html_content = html_content.replace('__TEMPLATE_MOVIE_GRID__', movie_grid_html)

        # Write the generated HTML to index.html
        try:
            with open('_static/index.html', 'w') as file:
                file.write(html_content)
            print("Website was generated successfully.")
            return True
        except Exception as e:
            print(f"Error generating website: {e}")
            return False


    def run(self):
            """Run the movie application."""
            print(" My Movies Database ".center(40, '*'))

            while True:
                print()
                print("Menu:")
                print("0. Exit")
                print("1. List movies")
                print("2. Add movie")
                print("3. Delete movie")
                print("4. Update movie")
                print("5. Random movie")
                print("6. Search movie")
                print("7. Sort movies by year")
                print("8. Generate Website")
                print()

                menu_keys = sorted(self.commands.keys())
                choice = input(f"Enter choice (0-{menu_keys[-1]}): ")
                if choice == '0':
                    print("Bye!")
                    return

                try:
                    command = self.commands[int(choice)]
                except (ValueError, KeyError):
                    print("Invalid choice")
                    continue

                print()
                command()
                input("\nPress enter to continue ")

