# from forms1 import Post_form
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/image")
def hello_world():
    return render_template('image.html')


if __name__ == "__main__":
    app.run(debug=True)
