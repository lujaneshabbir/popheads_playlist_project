import praw
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from spacy import spacy

# AUTHENTICATION
reddit = praw.Reddit(
    client_id="1d4KhVfd5JlCuf6KPVXLdQ",
    client_secret="px2jh-SCDIhYN2md1RHqHf_dclSy5g",
    user_agent="spotify:tbc:v1.2.3 (by /u/barelylyndving)",)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fe523ddd3e48476590d0c807b42c2e22",
                                               client_secret="b82056b0fe45466cac6066c0eb5fd0f6",
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

def find_songs (submission):
    songs = []
    for comment in submission.comments[:100]:
        song_dash_artist = re.findall(r'[^ ]* - [^ ]*', comment.body, )
        songs = songs + song_dash_artist
        song_by_artist = re.findall(r'[^ ]* by [^ ]*', comment.body, )
        songs = songs + song_by_artist
    # print(songs)
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














# print(post.title)
# for comment in post.comments[:1000]:
    # print(comment.body, '\n')
    # print("( \" ", comment.body, "\" \n {\"entities\": , , LABEL})")


# MAIN
# for submission in reddit.subreddit("popheads").top(limit=0):
#     if submission.link_flair_text == "[DISCUSSION]":
#         if submission.title.find("What songs sound Christmas-y or wintery even though that's not what they were going for?") != -1:
#             print(submission.title, submission.link_flair_text)
             # for comment in submission.comments[:10]:
             #     print("( \" ", comment.body, "\" \n {\"entities\": , , LABEL})")
# for submission in reddit.subreddit("popheads").top(limit=0):
    # if submission.link_flair_text == "[DISCUSSION]":
    #     songs = []
    #     print(submission.title, submission.link_flair_text)
    #     print('________________________________________')
    #     submission.comments.replace_more(limit=0)
        # for comment in submission.comments[:100]:
        #     print("( \" ", comment.body, "\" \n {\"entities\": , , LABEL})")
            # print("_____")
            # songs_quote = re.findall(r'"(. *)"', comment.body);
            # song_dash_artist = re.findall(r'[^ ]* - [^ ]*', comment.body, )
            # songs = songs + song_dash_artist
            # # song_by_artist = re.findall(r'[^ ]* by [^ ]*', comment.body, )
            # songs = songs + song_by_artist
        # print(songs)
