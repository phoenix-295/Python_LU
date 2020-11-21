from flask import render_template, Flask, request, redirect, url_for, jsonify
from forms1 import Post_form
from modal1 import app, blog_details13, db
from flask_restful import Resource, Api


@app.route('/image')
def image1():
    return render_template("image.html")


post = [{'blogtitle': "My first post", 'blogcontent': "Hello how are you", 'date1': "2020, Nov 19"},
        {'blogtitle': "flask project", 'blogcontent': "just do it", 'date1': "2020, Nov 19"}]


@app.route('/', methods=['GET', 'POST'])
def display():
    posts = blog_details13.query.all()
    return render_template('display.html', posts=posts)


@app.route("/post", methods=['GET', 'POST'])
def post1():
    print("Hello")
    form = Post_form(request.form)
    if form.validate():
        post1 = blog_details13(form.title.data, form.content.data)
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('display'))
    return render_template('create_post.html', form=form, legend='Write Post today')


class Data1(Resource):
    def get(self, id1):
        data = blog_details13.query.filter_by(blogid=id1).first()
        return {'about': str(data)}


if __name__ == '__main__':
    app.run(debug=True)
