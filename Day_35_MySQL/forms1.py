from wtforms import Form, StringField, validators, TextAreaField, SubmitField


class Post_form(Form):
    title = StringField('Title', validators=[validators.DataRequired()])
    content = TextAreaField('Content', validators=[validators.DataRequired()])
    submit = SubmitField('Post')
