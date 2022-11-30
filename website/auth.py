from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return ""
    
@auth.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")