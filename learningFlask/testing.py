from flask import Flask, url_for, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlit:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = fb.Column("name", db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):

@app.route("/")
@app.route("/<name>")
def home():
    return render_template('base.html', content=['song1', 'song2', 'song3'])

@app.route("/page2")
def page2():
    return render_template('test.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True) 