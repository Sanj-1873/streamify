from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def home(name):
    return render_template('index.html', content=['song1', 'song2', 'song3'])



if __name__ == "__main__":
    app.run() 