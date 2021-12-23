
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fe523ddd3e48476590d0c807b42c2e22",
                                               client_secret="b82056b0fe45466cac6066c0eb5fd0f6",
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
