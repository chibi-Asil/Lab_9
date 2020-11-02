import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
# Lab 9: Birthdays
# https://cs50.harvard.edu/extension/2020/fall/labs/9/
# Create a web application to keep track of friends’ birthdays.


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        # When the / route is requested via GET, your web application should display, in a table, all of the people in your database along with their birthdays.
        # First, in application.py, add logic in your GET request handling to query the birthdays.db database for all birthdays. Pass all of that data to your index.html template.
        session["name"] = request.form.get("name")
        session["birthday"] = request.form.get("birthday")
        return render_template("index.html", name = request.form.get("name", "birthday"))
            birthdays = db.execute("SELECT name, month, day FROM birthdays;")
    return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        # Then, in application.py, add logic in your POST request handling to INSERT a new row into the birthdays table based on the data supplied by the user.
        birthdays = []
    return render_template("index.html", birthdays = birthdays)


