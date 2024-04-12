import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# AUTHENTICATION

print(os.environ['ID_SPOTIFY'])
print(os.environ['SECRET_SPOTIFY'])


id_spotify = os.environ['ID_SPOTIFY']
secret_spotify = os.environ['SECRET_SPOTIFY']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id_spotify,
                                               client_secret=secret_spotify,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-read-private playlist-modify-private"))

# FUNCTIONS
pl_created_url =''

def display_url():
    global pl_created_url
    return pl_created_url

def add_songs(pl_id, songs):
    id_list = []
    for index in range(len(songs)):
        if "https" not in songs[index]:
            if " -" in songs[index]:
                split = songs[index].split(' -')
            elif " by" in songs[index]:
                split = songs[index].split(' by')
        print(split)
        search_term = split[0] + split[1]
        result = sp.search(search_term, limit=1, offset=0, type='track', market=None)
        if result['tracks']['total'] > 0:
            id_list.append(result['tracks']['items'][0]['id'])
    id_list = set(id_list)
    id_list = list(id_list)
    sp.playlist_add_items(pl_id, id_list, position=None)

def make_playlist(submission, songs):
    if songs:
        pls = sp.current_user_playlists(limit=50, offset=0)
        pl_found = False
        new_pl = {"id": ""}
        for pl in pls['items']:
            if pl['name'] == submission.title:
                sp.current_user_unfollow_playlist(pl['id'])
        new_pl = sp.user_playlist_create("u95rrsg6w74lnq922m253zd5o", submission.title, False, False, "https://www.reddit.com" + submission.permalink)
        global pl_created_url
        pl_created_url = new_pl["external_urls"]['spotify']
        add_songs(new_pl['id'], songs)

