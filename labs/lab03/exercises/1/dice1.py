from flask import Flask
app = Flask(__name__)

@app.route("/")

def app():
    return "<html><h1>This is the Dice Web App</h1></html>"