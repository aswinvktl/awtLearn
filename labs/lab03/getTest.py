from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
    return "The default 'root' route"

@app.route("/account/", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        return "POST'ed to account root\n"
    else:
        return "GET /account root"