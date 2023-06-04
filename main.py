import requests
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "8f44976f0caa4efc995a208126d0901d"
CLIENT_KEY = "6cca3eee21a04ee2b947e3c4e2ecd12e"

date = input("Which year do you want to travel to?\nType the date in this format"
             "YYYY-MM-DD:")
date_entered = date.split("-")[0]

r = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
r.raise_for_status()
billboard = r.text

soup = BeautifulSoup(billboard, "html.parser")
songs_title = soup.select("li ul li h3")
songs_title = [song.getText().strip() for song in songs_title]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
songs_uri = []
for song in songs_title:
    search_song = sp.search(q=f"track:{song} year:{date_entered}", limit=1, type="track", market="US")
    print(search_song)
    try:
        uri = search_song["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        pass

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"Top-100🎧/{date}", public=False)
print(playlist)
# Adding songs  into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)

