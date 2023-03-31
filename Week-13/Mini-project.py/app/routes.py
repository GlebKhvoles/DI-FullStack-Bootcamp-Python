import flask
from app import app, db
from app.models import User
from app.forms import UserForm, LoginForm
from flask import render_template, request, redirect, url_for, flash, abort
import json
import re
def open_json_file(file_path):
    with open(file_path) as f:
        return json.load(f)
def zipcode_func():
    result = []
    all = User.query.all()
    for person in all:
        new_list = [i for i in person.zipcode]
        if int(new_list[0]) == 5:
            result.append(person)
    return result
@app.route('/')
def index():
    my_file = User.query.all()
    first_five = User.query.limit(5)
    zipcode_5 = zipcode_func()
    return render_template('index.html', my_file=my_file, first_five=first_five, zipcode_5=zipcode_5)

@app.route('/add_user', methods=("GET", "POST"))
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, street=form.street.data, city=form.city.data, zipcode=form.zipcode.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html', form=form)

@app.route("/login", methods=("GET", "POST"))
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        name = login_form.name.data
        user = User.query.filter_by(name=name).first()
        if re.search('\d', name):
            flash('You can not use numbers in the name', 'error')
        if user:
            flash('You logged in!', 'success')
            return flask.redirect(flask.url_for('index'))
        else:
            flash('You need to sign up!', 'error')
            return flask.redirect(flask.url_for('add_user'))



    return render_template('login.html', form=login_form)

