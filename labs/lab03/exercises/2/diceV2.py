from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/dice/<int:num>")

# we use num as the parameter that is supplied by the url 
def dice (num):

    if 0 > num or num > 6:
        return "please enter a number between 1 and 6"
    
    else:

        rolls = []
        total = 0
        for r in range(num):
            roll = random.randint(1,6)
            rolls.append(str(roll))
            total += roll
    html = f'''

            <html>
            <body>
            <p>you rolled {num} dice</p>
            <p>The results are: {','.join(rolls)}</p>
            <p>The total is:{total}</p>
            </body>
            </html>
'''
    
    return html