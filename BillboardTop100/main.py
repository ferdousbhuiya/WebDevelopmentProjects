from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import dotenv


#required_date = input("Which date do you want to travel? Type the date in 'YYYY-MM-DD' format: ")
required_date = '1995-06-10'
URL = f"https://www.billboard.com/charts/hot-100/{required_date}"
#print(URL)

response = requests.get(URL)
response.raise_for_status()  # This will raise an error if the request was unsuccessful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Use CSS selectors to find all song title elements
song_titles = soup.select('li ul li h3')
#print(song_titles)
# Extract the text from each song title element
songs = [song.getText().strip() for song in song_titles]
#print(songs)
# Print the song titles
for song in songs:
    print(song)

load =load_dotenv()
CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET =os.environ['SPOTIPY_CLIENT_SECRET']

scope = "playlist-modify-private"

REDIRECT_URI = "https://example.com/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="t",
        username='Md Ferdouse',
    )
)
user_id = sp.current_user()["id"]
print(user_id)


date = required_date
song_names = songs

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)