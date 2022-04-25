import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "your client id here"
CLIENT_SECRET = "your client secret here"
PATH_TO_YOUR_FILES = "your path here"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                              redirect_uri="https://example.com/callback",
                              scope="playlist-modify-private", show_dialog=True,
                              cache_path=PATH_TO_YOUR_FILES + "/token.txt"))

user_id = sp.current_user()["id"]

# year = "2021-09-14"
# YYYY = "2021"
date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD ")
YYYY = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
top100_web_page = response.text

soup = BeautifulSoup(top100_web_page, "html.parser")

all_songs = soup.select("div ul li ul li h3")
songs_list = [" ".join(song.getText().split()) for song in all_songs]
song_uris = []
i = 0

with open(PATH_TO_YOUR_FILES + "/songs.txt", "w") as file:
    for song in songs_list:
        i += 1
        if i == 101:
            break
        file.write(song)
        file.write('\n')

        search_str = f"track:{song} year:{YYYY}"
        result = sp.search(q=search_str, type="track")

        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
