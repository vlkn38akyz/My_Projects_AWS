from flask import Flask, render_template

app = Flask(__name__)

Tags = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sontag"]

@app.route("/")
def index():
    numbers = [1,2,3,4,5,6,7]
    return render_template("index.html",numbers = numbers)

@app.route("/print")
def print():
    
    return render_template("print.html",len = len(Tags), Tags = Tags)
  

if __name__ == "__main__":
    app.run(debug = True)  