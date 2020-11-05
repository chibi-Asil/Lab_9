# Lab 9: Birthday
# https://cs50.harvard.edu/extension/2020/fall/labs/9/
import os

# from cs50 import SQL
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

class birthday():
    name = []
    months = [("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")]


# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = "sqlite:///birthdays.db"

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///birthdays.db")
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = name.query.filter_by(name = name).first
        month = month.query.filter_by(month = month).numeric
        day = day.query.filter_by(day = day).numeric
        return redirect("/", name = name, month = MONTH, day = day)
    else:
        # TODO: Display the entries in the database on index.html
        # name_print = name.query.all()
        return render_template("index.html")

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['name', 'month', 'day']

    if search.data['search'] == '':
        qry = db.query(birthdays)
        results = qry.all()

    if not results:
        flash("No results found!")
        return redirect('/')
    else:
        return render_template('information.html', table = table)

@app.route('/new_additions', methods = ["GET", "POST"])
def new_additions():
    form = new_birthdays(request.form)
    return render_template("new_additions.html", form = form)