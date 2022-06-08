from email import message
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    message = "Bu bir mesajdir sanirim..."
    return render_template("index.html",message= 0)

@app.route("/message")
def message():
    message = "Bu bir message..."
    return render_template("p.html", message= message)
  

if __name__ == "__main__":
    app.run(debug = True)    