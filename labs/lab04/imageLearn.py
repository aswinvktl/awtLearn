from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Napier"

@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='mask.jpg')
    end = '">'
    return start+url+end,200