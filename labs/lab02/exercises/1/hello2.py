# hello2.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def error():
    doerror()
    
