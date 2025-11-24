from flask import Flask, request
import random # for randomising the dice rolls

app = Flask(__name__)

@app.route("/dice", methods=['POST', 'GET'])
def dice ():
    if request.method == 'POST':

        try:
            num_dice = request.form["num"]
            num = int(num_dice)

        except(ValueError, KeyError):
            return "<h1>invalid input, try again</h1>"
        
        rolls = []
        total = 0


        # loop to calculate the value based on what the input was

        for r in range(num):
            roll = random.randint(1,6)
            rolls.append(str(roll))
            total += roll

        result_page = f'''

        <html>
        <body>
            <h1> Dice Roll Results</h1>
            <p>You rolled {num} dice</p>
            <p> The results are: {','.join(rolls)}</p>
            <p> The total is: {total}</p>
        </body>
        </html>
        '''

        return result_page
        # get data from user dammit
    else:

        page= f'''

        <html>
        <body>
            <h1>ROLL SOME DICE!!!</h1>
            <form action="/dice" method="post" name="dice">
            <label for="num">Enter the number of dice:</label>
            <input type="text" name="num"/>
            <input type="submit" name="submit"/>
            </form>
        </body>
        </html>

'''
        
        return page