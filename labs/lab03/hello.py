from flask import Flask, request

app = Flask(__name__)

# decorator
@app.route("/") 

# function definition
def hello():
    print (request.method, request.path, request.form)
    return "<p>Hello, World!</p>"