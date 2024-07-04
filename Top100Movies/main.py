import os

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
rank_numbers = []
movie_names = []
for movie in movie_list:
    if ") " in movie:
        rank_number = movie.split(") ")[0]
        movie_name = movie.split(") ")[1]
        rank_numbers.append(rank_number)
        movie_names.append(movie_name)
        #print(f"{rank_number}, {movie_name}")
    elif ": " in movie:
        rank_number = movie.split(": ")[0]
        movie_name = movie.split(": ")[1]
        rank_numbers.append(rank_number)
        movie_names.append(movie_name)
        #print(f"{rank_number}, {movie_name}")
# print(rank_numbers)
# print(movie_names)

inverted_rank_number = rank_numbers[::-1]
print(inverted_rank_number)

# Write inverted rank numbers and movie names to a file in the specified format
with open("./movie_list.txt", "a", encoding='UTF-8') as file:
    for idx, x in enumerate(inverted_rank_number):
        file.write(f"{x}) {movie_names[idx]}\n")

print("Data written to movie_list.txt successfully.")
