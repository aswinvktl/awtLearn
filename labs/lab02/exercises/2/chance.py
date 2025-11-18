from flask import Flask, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
def root():
    elemets = random.choices(['ten', 'ninety'], weights=[10,90], k=1)[0]
    return redirect(url_for(elemets))


@app.route("/ten")
def ten():
    return '<a href= https://www.youtube.com/watch?v=At8v_Yc044Y>SURPRISE</a>'


@app.route("/ninety")
def ninety():
    return '<a href="/">TRY AGAIN<a>'



