from flask import Flask, url_for, redirect, request, render_template, flash 
from flask import *
app = Flask(__name__)
app.secret_key = "abc"

@app.route("/", methods=["POST", "GET"])
@app.route("/home/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        song = request.form["nm"]
        return render_template('song_search.html', song=song)
    else:  
        return render_template('index.html')



@app.route("/<song_name>")
def song_list(song_name):
        return f"<h1>{song_name}</h1>"


@app.route("/playlists/", methods=["POST", "GET"])
def playlists():
    if request.method == 'POST':
        list_name =  request.form["playlist_name"]
        songs =  request.form["song_name"]
        flash("Your song has been added", "info")
        return render_template('playlists.html')
    else:
        return render_template('playlists.html')     


if __name__ == "__main__":
    app.run(debug=True) 

   