# Import Flask modules
from flask import Flask, render_template
from sqlalchemy import null
# Create an object named app 
app = Flask(__name__)

# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route("/")
def head():
    first="This is my first conditions experience"
    return render_template("index.html", message = "treni kacirma")


# Create a function named header which prints numbers elements of list one by one in `index.html` 
# and assign to the route of ('/')
@app.route("/volkan")
def header():
    names =["Serdar", "Sam", "Jasper", "Volkan", "Ilhan","HAkan"]
    #numbers = range(1.11)
    return render_template("body.html", object = names)


# run this app in debug mode on your local.
if __name__== "__main__":
    app.run(debug=True)



