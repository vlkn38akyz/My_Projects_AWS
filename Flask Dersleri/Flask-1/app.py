from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", number1 = 10, number2 = 20, isim = "volkan akyuz")

@app.route("/personel")
def personel():
    return render_template("personel.html", Isim = "Volkan", Soyisim = "Akyüz", Yas = 42)

if __name__ == "__main__":
    app.run(debug = True)    