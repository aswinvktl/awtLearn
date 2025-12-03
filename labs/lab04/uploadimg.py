from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
def hello ():
    return f'''<p>Hello funde</p>
                <p><a href="/upload">upload some images lil bro</a></p>'''

@app.route("/display/")
def display():
    return '<img src="' + url_for('static', filename='uploads/upload.jpg')+'"/>'

# we consider the user account scenario where we get the image from the user
@app.route("/upload", methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/upload.jpg')
        
        return f'''<p>file uploaded</p>
        <p><a href= "/display">check it out</a></p>'''
    else:
        page = f'''
            <html>
            <body>
            <form action="" method="post" name="form" enctype="multipart/form-data">
                <input type="file" name="datafile" />
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body>
            </html>

'''
        
        return page, 200