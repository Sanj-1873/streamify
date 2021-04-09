from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True) 