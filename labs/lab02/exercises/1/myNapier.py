from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return (
        "<h1>Home Page</h1>"
        "<h3>NAVIGATION</h3>"
        '<a href="/mynapier">My Napier - so far</a>' # single quotes to match python syntax
    )


@app.route("/mynapier")
def mynapier():
    return ("<p>I am aswin, 3rd year cs student. I edit videos and i love watching movies. I am an international student and live in edinburgh. It is a beautiful city. </p>"
            '<a href= "/year1">Year 1</a>'
            )

@app.route("/year1")
def y1():
    return (
        "<p>It was a very confusing year</p>"
        "<p>I moved from 35 degrees to 3.5 degrees.</p>"
        "<p>It was very cold for me in the beginning, not just the weather but my life as a whole</p>"
        "<p>I did not know a single person in this country and was struggling with almost everything</p>"
        "<p>But it was first year, I slowly started doing things I like, started going to the gym, watching movies, making the food I like, found good roommates and all</p>"
        "<p>Year one academically was pretty alright, but it laid the foundation for a lot of things and taught me how to live</p>"
        '<a href= "/year2">Year 2</a>'
    )

@app.route("/year2")
def y2():
    return(
        "<p>This was the best year. I understood this country and university and all. Started to know people, got a job that I like and life was going pretty smooth.</p>"
        "<p>I met some amazing people and spent time with them, talking about the things I like and all.</p>"
        "<p>Academically, it was better than first year, I understood a lot of concepts that was being taught and overall enjoyed it</p>"
        "<p><a href= 'https://fsteamnapier.co.uk/'>Formula Student Team Napier </a>. came to my life this year and that was a good addition</p>"
        "<p>Overall, met a lot of people, had a good time and was pretty good.</p>"
        '<a href= "/year3">Year 3</a>'
    )

@app.route("/year3")
def y3():
    return(
        "<p>Just started, this is an year 3 project</p>"
        "<p>It seems alright so far. Have a lot to catch up. So i better keep going.</p>"
        '<a href= "/jobs">Volunteering and Jobs'
    )

@app.route("/jobs")
def jobs():
    return(
        "<p>It was actually pretty fun and met a lot of people there</p>"
        '<a href= "/travel">Travel'
    )

@app.route("/travel")
def travel():
    return(
        "<p>I had the chance to go to certain places</p>"
        "<p>I went to the highlands it was actually pretty nicee</p>"
        "<p> Then I went to silverstone, which was so great. glasgow, aberdeen and all. Haven't been to inverness</p>"
        '<a href= "/future">future'
    )

@app.route("/future")
def future():
    return(
        "<p>I want to start preparing for my dissertation and start to think about what I am gonna do, for that, I will have to give every second of my life to learn this shi</p>"
        '<a href= "/goodbye">Goodbye!!!!'
    )

@app.route("/goodbye")
def home1():
    return(
        "<p>Thanks for reading, all the best. GoodBye</p>"
        '<a href= "/"> HOME'
    )