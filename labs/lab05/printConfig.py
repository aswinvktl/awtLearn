'''
the config file is a text file with settings

configparser reads that file and turns it into python data

and then the config route prints the config file values to confirm that the config file was used and the app is now using those settings
'''


import configparser

from flask import Flask

app = Flask(__name__)

def init(app):
    config = configparser.ConfigParser()
    try:
        print("INIT FUNCTION")
        config_location = "etc/defaults.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")

    except:
        print ("Could not read configs from: ", config_location)

init(app)

@app.route("/")
def root ():
    return "Hello Napier from the configuration testing app"

@app.route('/config/')
def config():
    s = []
    s.append('debug'+str(app.config['DEBUG']))
    s.append('port:'+str(app.config['port']))
    s.append('url'+str(app.config['url']))
    s.append('ip_address'+str(app.config['ip_address']))
    return ','.join(s)