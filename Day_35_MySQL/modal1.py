from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/testdb'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class blog_details13(db.Model):
    blogid = db.Column(db.Integer, primary_key=True)  # Automatic increment
    blogtitle = db.Column(db.String(100), nullable=False)
    blogcontent = db.Column(db.String(500), nullable=False)
    # date1 = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __init__(self, blogtitle, blogcontent):
        self.blogtitle = blogtitle
        self.blogcontent = blogcontent
        # self.date1 = date1

    def __repr__(self):
        return f"({self.blogtitle}, {self.blogcontent})"


if __name__ == '__main__':
    db.create_all()
