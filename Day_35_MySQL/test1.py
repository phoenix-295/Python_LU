from flask import Flask, render_template

app = Flask(__name__)


@app.route("/image")
def hello_world():
    return render_template('image.html')


@app.route("/nik")
def hello1():
    return "Hello Nik"


if __name__ == "__main__":
    app.run(debug=True)
