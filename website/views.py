from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import LogFile
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        logFile = request.form.get('logFile')
        methodName = request.form.get('methodName')
        if len(logFile) < -1:
            flash('Can not save empty file', category='error')
        else:
            new_logFile = LogFile(data=logFile, user_id = current_user.id, methodName=methodName)
            db.session.add(new_logFile)
            db.session.commit()
            flash('Log Saved!', category='success')


    return render_template('index.html', user=current_user)

@views.route('/saved_logs')
@login_required
def saved_logs():
    return render_template('saved_logs.html', user=current_user)
