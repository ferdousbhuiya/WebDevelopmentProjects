import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the webpage
response = requests.get(URL)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the movie title elements
title_elements = soup.find_all(name='h3', class_='title')

# Extract movie names and ranks
movie_list = [title.get_text(strip=True) for title in title_elements]
print(movie_list)
# Process and print movie names and ranks
for movie in movie_list:
    # Split on the first occurrence of ") " to separate rank and movie name
    parts = movie.split(") ", 1)
    if len(parts) == 2:
        rank_number, movie_name = parts
        print(f"{rank_number},{movie_name}")
    else:
        # Handle cases where rank number is missing or not in expected format
        print(f"Rank number missing or unexpected format: {movie}")
