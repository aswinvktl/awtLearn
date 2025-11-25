from flask import Flask, request # request is to get the colour from the user as an argument

app = Flask(__name__)

@app.route("/bright")
def colour():
    colour = request.args.get('colour', '')

    if colour == '':
        return "<h1>Invalid Input</h1>"
    
    else:
        return f'''
                <html>
                <body style="background-color:{colour};"></body>
                <p>This is the background with the colour requested:</p>
                </html>

'''