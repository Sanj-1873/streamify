from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def home():
    return render_template('base.html', content=['song1', 'song2', 'song3'])

@app.route("/page2")
def page2():
    return render_template('test.html')


if __name__ == "__main__":
    app.run(debug=True) 