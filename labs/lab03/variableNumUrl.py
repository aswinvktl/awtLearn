from flask import Flask
app = Flask(__name__)

@app.route("/subtract/<int:first>/<int:second>")
def subtract(first,second):
    return str(second-first)