from flask import Flask, render_template

app = Flask(__name__)

Tags = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sontag"]


@app.route("/")
def index():
    numbers = [1,2,3,4,5,6,7]
    return render_template("index.html",numbers = numbers)

@app.route("/print")
def print():
   
    return render_template("print.html",len = len(Tags), Tags = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sontag"])


@app.route("/forif")
def forif():
    sayilar = [-1,-2,3,5,6,8]
    return render_template("forif.html",len = len(sayilar), sayilar = sayilar)


@app.route("/forx")
def forx():
    sayi = 101
    sum = 0  
    for i in range(0,sayi):
        sum += i

    return render_template("forx.html", sayi = sayi, sum = sum )

  

if __name__ == "__main__":
    app.run(debug = True)  

    