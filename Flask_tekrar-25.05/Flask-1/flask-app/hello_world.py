from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "Flaks deneme dersi"

@app.route("/ikinci")
def ikinci():
    return "Hello world from Flask"

@app.route("/second")
def second():
    return "This is my second page"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/a/b")
def a():
    return "<h2>This is the subpath of a/b page</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

@app.route("/bes/<string:id>")
def bes(id):
    return f'Id of this page is {id}'

@app.route("/on/<string:new>")
def on(new):
    return f'Id of this page is {new}'

@app.route("/onbir/<string:new>")
def onbir(new):
    return f'Id of this page is {new}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    #app.run(debug=True)