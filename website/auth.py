from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

emailReg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login Success', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not belong to a current user', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already belongs to a user', category='error')
        elif not re.fullmatch(emailReg, email) or len(email) > 150:
            flash('Invalid email.', category='error')
        elif len(userName) < 3 or len(userName) > 14:
            flash('User name must be between 3 and 14 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        else:
            newUser = User(email=email, userName=userName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash('Success! Account created.', category='success')
            return redirect(url_for('views.index'))

    return render_template("sign_up.html", user=current_user)