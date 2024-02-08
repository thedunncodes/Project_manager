from .. import app
from ..users.forms import Register_form, login_form
from ..modules.models import user
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/")
@login_required
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        User = user.objects(email=form.email.data).first()
        if User and User.email == form.email.data:
            login_user(User)
            next_page = request.args.get('next')
            flash(f'{User.name} {next_page}you have a succesful login')
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash('Login terminated')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    form = Register_form()
    if form.validate_on_submit():
        User = user(name=form.name.data, email=form.email.data, password=form.password.data)
        User.save()
        flash(f'{form.name.data}, Login sucessful. Please check email and password', 'danger')
        return redirect(url_for("home"))
    return render_template('register.html', form=form)

@app.route("/logout", methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))