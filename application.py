# Lab 9: Birthday
# https://cs50.harvard.edu/extension/2020/fall/labs/9/
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

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
        name = name.query.filter_by(name = name).first
        month = month.query.filter_by(month = month).numeric
        day = day.query.filter_by(day = day).numeric
        return redirect("/", name = name, month = month, day = day)

    else:

        # TODO: Display the entries in the database on index.html
        if not request.form.get("name") or request.form.get("month") or request.form.get("day"):
            return render_template("index.html")


