
import spotipy
from spotipy.oauth2 import SpotifyOAuth

id_spotify = os.environ['ID_SPOTIFY']
secret_spotify = os.environ['SECRET_SPOTIFY']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id_spotify,
                                               client_secret=secret_spotify,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-read-private playlist-modify-private"))

pls = sp.current_user_playlists(limit=50, offset=0)
for pl in pls['items']:
    print(pl['id'])
    print(pl['name'])
    if (pl['name'] == "What are songs that have a feature in it which you think might actually be better without it?"):
        print(True)
        sp.current_user_unfollow_playlist(pl['id'])
# print(pls['items'][0])
