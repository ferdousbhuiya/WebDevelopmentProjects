from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return 'Hello world'
@app.route("/bye")
def bye():
    return 'Bye'
@app.route("/<name>")
def greets(name):
    return f"Hello,{name}!"

if __name__ == "__main__":
    app.run(debug=True)