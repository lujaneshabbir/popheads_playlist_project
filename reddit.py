import praw
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# AUTHENTICATION
print(os.environ['ID_REDDIT'])
id_reddit = os.environ['ID_REDDIT']
secret_reddit = os.environ['SECRET_REDDIT']
agent_reddit = os.environ['AGENT_REDDIT']

reddit = praw.Reddit(
    client_id= id_reddit,
    client_secret= secret_reddit,
    user_agent= agent_reddit)

def find_songs (submission):
    songs = []
    for comment in submission.comments[:100]:
        song_dash_artist = re.findall(r'[^ ]* - [^ ]*', comment.body, )
        songs = songs + song_dash_artist
        song_by_artist = re.findall(r'[^ ]* by [^ ]*', comment.body, )
        songs = songs + song_by_artist
    make_playlist(submission, songs)

def get_post(post_id):
    post = reddit.submission(id= post_id)
    find_songs(post)

def find_ID(url):
    if "/comments/" in url:
        ID = url.split('/comments/')
        if "/" in ID[1]:
            ID = ID[1].split('/')
    get_post(ID[0])
