# import application packages
import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
# app configration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home_page():
    return render_template("home.html")


# show All places in Hiking places page
@app.route("/all_places")
def all_places():
    places = mongo.db.places.find()
    return render_template("places.html", places=places)


# show All places in Hiking places page
@app.route("/all_hikers")
def all_hikers():
    hikers = mongo.db.users.find()
    return render_template("hikers.html", hikers=hikers)


# show Hiker profile page
@app.route("/hiker_profile")
def hiker_profile():
    return render_template("hiker_profile.html")


# make sure to debug= False before submit
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
