# Movie Collection App 
A simple application for managing your personal movie collection with data from the OMDb API.

## Description
This Movie Collection App allows you to build and maintain a database of your favorite movies. It fetches movie information from the OMDb API and stores it locally. The app offers multiple storage options and allows you to generate a beautiful HTML website to showcase your collection.

## Features
+ Search for movies using the OMDb API
+ Add movies to your personal collection
+ View your entire movie list
+ Delete movies from your collection
+ Update movie ratings
+ Generate a visual website to display your collection
+ Multiple storage options (JSON, CSV)

## Requirements

+ Python 3.6 or higher
+ Internet connection (for fetching data from the OMDb API)

### Required Python packages:
***requests***

## Installation

+ Clone this repository or download the source code
+ Install required packages:
+ Copypip install requests

+ Make sure you have a valid OMDb API key
+ Run the program:
+ Copy: *python movie_app.py*


## Usage
+ Main Menu:
When you run the program, you'll be presented with a menu of options:

+ Add Movie: Search for a movie by title and add it to your collection
+ Delete Movie: Remove a movie from your collection
+ Update Movie: Change a movie's rating
+ List Movies: View all movies in your collection
+ Generate Website: Create an HTML website to showcase your collection
+ Exit: Close the application


### File Structure

+ movie_app.py: Main application file
+ istorage.py: Interface defining storage requirements
+ storage_json.py: JSON-based storage implementation
+ storage_csv.py: CSV-based storage implementation
+ _static/index_template.html: Template for website generation
+ _static/style.css: Stylesheet for the generated website

## Storage Options
The app supports multiple storage backends:

+ JSON: Stores data in a readable JSON format
+ CSV: Stores data in CSV format

### API Integration
This app uses the OMDb API to fetch movie information. Each API request includes:

+ Movie title
+ Release year
+ Rating
+ Poster URL