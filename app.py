from flask import Flask, redirect, url_for
from flask_login import LoginManager
from app.routes.auth import auth_bp, HARDCODED_USER
from app.routes.main import main_bp

import os
#from flask import Flask

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'app', 'templates'))


#app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Use environment variable in production

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# User loader (returns hardcoded user)
@login_manager.user_loader
def load_user(user_id):
    if str(HARDCODED_USER.id) == str(user_id):
        return HARDCODED_USER
    return None

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# Redirect root to login page
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
