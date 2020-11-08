# import application packages
import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
@app.route("/all_trails")
def all_trails():
    trails = mongo.db.trails.find()
    return render_template("all_trails.html", trails=trails)


# show All places in Hiking places page
@app.route("/all_hikers")
def all_hikers():
    hikers = mongo.db.users.find()
    return render_template("hikers.html", hikers=hikers)


# show Hiker profile page
@app.route("/hiker_profile")
def hiker_profile():
    return render_template("hiker_profile.html")


# show Place page
@app.route("/trail_page")
def trail_page():
    return render_template("trail_page.html")


# sign_up Function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if name / email already exists in database
        existing_name = mongo.db.users.find_one(
            {"name": request.form.get("name").lower()})
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_name:
            flash("Sorry , Name already exists")
            return render_template("thank_you.html")

        elif existing_email:
            flash("Sorry , Email already exists")
            return render_template("thank_you.html")
        # check if cpassword confirmation match
        elif request.form.get("password") != request.form.get("password2"):
            flash("Sorry , The password confirmation does not match")
            return render_template("thank_you.html")

        register = {
            "name": request.form.get("name").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
            # Confirm password code here
            }
    mongo.db.users.insert_one(register)
    # put the new user into 'session' cookie
    session["user"] = request.form.get("name").lower()
    flash("Registration Successful!")
    return render_template("thank_you.html")  # customize thanks page ??


# Edit Profile Function
@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if request.method == "POST":
        update = {
            "profile_name": request.form.get("profile_name"),
            "bio": request.form.get("hiker_bio"),
            "facebook_link": request.form.get("facebook_link"),
            "instagram_link": request.form.get("instagram_link"),
            "twitter_link": request.form.get("twitter_link"),
            }
    mongo.db.users.insert_one(update)
    return render_template("thank_you.html")


# make sure to debug= False before submit
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
