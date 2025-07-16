from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, UserMixin

auth_bp = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id, email, password, approved=True):
        self.id = str(id)               # must be string
        self.email = email.lower()
        self.password = password
        self.approved = approved

HARDCODED_USER = User(id=1, email="admin@sdg.com", password="admin@1234", approved=True)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').lower()
        password = request.form.get('password', '')
        
        if email == HARDCODED_USER.email and password == HARDCODED_USER.password:
            if HARDCODED_USER.approved:
                login_user(HARDCODED_USER)
                return redirect(url_for('main.estate_gallery'))
            else:
                flash("Access not yet approved by admin.", "warning")
        else:
            flash("Invalid email or password.", "danger")
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
