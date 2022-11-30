from flask import Blueprint, render_template, request, flash, redirect, url_for
import re

auth = Blueprint('auth', __name__)

emailReg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return ""
    
@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if re.fullmatch(emailReg, email) == False or len(email) > 150:
            flash('Invalid email.', category='error')
        elif len(userName) < 3 or len(userName) > 14:
            flash('User name must be between 3 and 14 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        else:
            flash('Success! Account created.', category='success')
            addUser(email, userName, password2)

    return render_template("sign_up.html")