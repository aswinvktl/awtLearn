from flask import Flask

app = Flask(__name__)

# decorator
@app.route("/") 

# function definition
def hello(): 
    return "<p>Hello, World!</p><p>hello</p>"