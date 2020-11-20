from flask import Flask, render_template, request, redirect, jsonify, url_for
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
    posts = blog_details13.all()
    return render_template('display1.html', posts=posts)


@app.route('/post', methods=['GET', 'Post'])
def post1():
    print("Hello")
    form = Post_form(request.form)
    if form.validate():
        post1 = blog_details13(form.title.data, form.blogcontent)
        db.session.add(post1)
        db.session.commit()
        # return re
    print(form.data)
    return render_template('create_post.html', form=form, legend='Write Post today')


@app.route('/json/<id>', methods=['GET', 'Post'])
def jsondata():
    data = blog_details13.query.filterby()


if __name__ == '__main__':
    app.run(debug=True)
