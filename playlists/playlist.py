from flask import Flask, url_for, redirect, request, render_template, flash 
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "abc"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playlists.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

# class playlists(db.Model):
    # _id = db.Column("id", db.Integer, primary_key=True)
    # name = db.Column("name", db.String(100))
    # song = db.Column("song", db.String(100))
    
class play(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   song = db.Column(db.String(50))  
   def __init__(self, name, song):
        self.name = name
        self.song = song


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

        if list_name is not None:
            playlist_create = play(list_name, songs)

            db.session.add(playlist_create)
            db.session.commit()

            flash("Your song has been added", "info")
        return render_template('playlists.html')
    else:
        return render_template('playlists.html')     

@app.route("/view")
def view():
    return render_template("view.html", values=play.query.all() )


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True) 
   