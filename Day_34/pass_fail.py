from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello"


@app.route('/mark/<int:score>')
def hello1(score):
    return render_template('mark.html', score=score)


if __name__ == "__main__":
    app.run(debug=True)
