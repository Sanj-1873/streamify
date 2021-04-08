from flask import Flask, url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello! this is the main page <h1> HII</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run() 