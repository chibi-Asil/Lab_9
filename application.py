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
        birthday = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthday = birthday)

    else:

        # TODO: Display the entries in the database on index.html
        # name_print = name.query.all()
        return render_template("index.html")

# def add_name():
#     # Validate name
#     name = request.form.get("name")
#     month = request.form.get("month")
#     day = request.form.get("day")
#     if not name or not day or month not in MONTHS:
#         return render_template("failure.html")

#     # Remembering the name
#     db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

#     # Confirming the entry
#     return redirect("/birthday_names")

# @app.route("/birthday_names")
# def birthday_names():
#     birthday_names = db.execute("SELECT * FROM birthdays")
#     return render_template("birthday_names.html", birthday_names = birthday_names)
