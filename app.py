from flask import Flask, jsonify, request
from reddit import find_ID

app = Flask(__name__)

@app.route('/playlist_creator')
def get_url():

    url_dict = {"url": find_ID(request.args.get("url"))}
    return jsonify(url_dict)
