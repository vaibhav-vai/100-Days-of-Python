from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "your-client-id"
client_secret = "your-client-secret"
redirect_uri = "your-redirect-uri"

date = input("Which year do you want to travel? Type the data in this format YYYY-MM-DD \n")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/138.0.0.0 Safari/537.36"}

url = "https://www.billboard.com/charts/hot-100/"+date+"/"

response = requests.get(url, headers=header)
billboard = response.text


soup = BeautifulSoup(billboard, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = redirect_uri,
        client_id = client_id,
        client_secret = client_secret,
        show_dialog = True,
        cache_path = "token.txt",
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
