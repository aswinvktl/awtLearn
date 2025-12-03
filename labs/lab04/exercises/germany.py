from flask import Flask, render_template
app = Flask(__name__)

@app.route("/germany")
def germany():
    return render_template('germany.html')

@app.route("/germanyHistory")
def history():
    return render_template('germanyHistory.html')

@app.route("/germanyFootball")
def football():
    return render_template('germanyFootball.html')