from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/dice", methods = ['POST', 'GET'])

def dice():
    if request.method == 'POST':
        try:
            num_dice = request.form["num"]
            num = int(num_dice)

        except(ValueError, KeyError):
            return "<h1> INVALID INPUT </h1>"


        rolls = []
        total = 0
            
        for r in range():
            roll = random.randint(1,6)
            rolls.append(str(roll))
            total += roll

        result_page = f'''
        <html>
        <body>
            <h1>Dice roll results</h1>
            <p>you used {num} dices</p>
            <p>the result is: {','.join(rolls)}</p>
            <p>the total is{total}</p>
        </body>
        </html>
        '''
        return result_page
        
    else:
        page = f'''
        <html>
        <body>
        <h1>ROLL YOUR DICES!!!</h1>
        <form action="/dice" method="post" name="dice">
        <label for="num">Enter number of dices</label>
        <input type="text" name="num" id="dice_num"/>
        <input type="submit" value="roll dice"/>
        </form>
        </body>
        </html>
        '''

    return page