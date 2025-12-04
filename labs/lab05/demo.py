from flask import Flask, session
import configparser

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
'''
def init(app):
    config = configparser.ConfigParser()
    print("INIT FUNCTION")
    config_location = "etc/defaults.cfg"
    config.read(config_location)
    
    app.config['API_KEY'] = config.get("config", "secret_key")
    init(app)
'''


@app.route("/")
def index():
    return "Root route for the sessions example"

@app.route('/session/write/<name>/')
def write(name=None):
    session['name'] = name
    return "Wrote %s into 'name' key of session" %name

@app.route('/session/read')
def read():
    try:
        if (session['name']):
            return str(session['name'])
    except KeyError:
        pass
    return "No session variable set for 'name' key"

@app.route('/session/remove/')
def remove():
    session.pop('name', None)
    return "Removed key 'name' from session"