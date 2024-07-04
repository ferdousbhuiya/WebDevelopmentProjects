import os

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime as dt
from dotenv import load_dotenv

URL = "https://www.jiosaavn.com/artist/bangla-song-songs/Bo,tPkHNXCw_"

response = requests.get(URL)
response.raise_for_status()

re = response.text
#print(re)

soup = BeautifulSoup(re, "html.parser")
title = soup.select("figcaption h4 a")
songs = [title.getText().strip() for title in title]

# for i in songs:
#     index = songs.index(i)
#     print(f"index Number: {index} , {i}")
# #print(songs)

songs.pop(44) # there was a problem in song number 44

# for i in songs:
#     print(i)



load = load_dotenv()
SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

scope = "playlist-modify-private"

REDIRECT_URI = "https://example.com/"
print(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id= SPOTIFY_CLIENT_ID,
        client_secret= SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Md Ferdouse',
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_names = songs

song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song}")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"Bangla Songs for Jio Saavan", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

