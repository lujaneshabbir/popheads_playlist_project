from flask import Flask, jsonify, request
from reddit import find_ID, display_url

app = Flask(__name__)

@app.route('/playlist_creator')
def get_url():
    find_ID(request.args.get("url"))
    x = display_url()
    return x ,200
