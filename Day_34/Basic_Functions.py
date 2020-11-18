from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello"


def sum1(str1):
    return len(str1)


@app.route('/nik/<my_name>')
def hello1(my_name):
    l = sum1(my_name)
    return "Hello " + my_name + str(l)


if __name__ == "__main__":
    app.run(debug=True)
