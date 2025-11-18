from flask import Flask, redirect, url_for
import random
app = Flask(__name__)

@app.route("/")
def root():
    return random.element(redirect(url_for('ten','ninety')))

@app.route("/ninety")
def ninety():
    return "Try again for the surprise"

@app.route("/ten")
def ten():
    return ("<h1>SURPRISEEEEEEEE</h1>"
            '<p><a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1">Click here</a></p>'
    )