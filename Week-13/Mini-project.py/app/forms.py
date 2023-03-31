from flask_wtf import FlaskForm
import wtforms


class UserForm(FlaskForm):
    name = wtforms.StringField('Username', validators=[wtforms.validators.DataRequired()])
    street = wtforms.StringField('Street', validators=[wtforms.validators.DataRequired()])
    city = wtforms.StringField('City', validators=[wtforms.validators.DataRequired()])
    zipcode = wtforms.StringField('Zipcode', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Add User', validators=[wtforms.validators.DataRequired()])

class LoginForm(FlaskForm):
    name = wtforms.StringField('Username', validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField('Log in')
