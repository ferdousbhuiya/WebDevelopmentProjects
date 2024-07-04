from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

""" period_date = input("Which year do you want to travel to? Type the date in the this format YYYY-MM-DD: ") """
period_date = "1990-08-22" # Created this to avoid inputing each time I tested. Will be removed after the whole project is done.

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

URL = f"https://www.billboard.com/charts/hot-100/{period_date}/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

all_song_titles = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

all_songs = [song.getText().replace("\t", "").replace("\n", "") for song in all_song_titles]

scope = "user-library-read"

SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri='https://example.com',
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt",
    username='ferdousbhuiya.ihs@gmail.com',
    )
)

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

user = sp.current_user()
print(user["id"])