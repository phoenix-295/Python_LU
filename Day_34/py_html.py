from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello"


@app.route("/nik")
def hello1():
    return "Hello Nik"


@app.route('/all/<my_name>')
def all_name(my_name):
    return render_template('Hello.html', name=my_name)


if __name__ == "__main__":
    app.run(debug=True)
