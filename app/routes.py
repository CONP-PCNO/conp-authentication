from flask import render_template
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app.forms import SignInForm
from app.forms import SignUpForm

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('logged_in'))
    signin = SignInForm()
    signup = SignUpForm()

    #if request.method == 'POST' and form.validate():
    #    if load_user(form.username.data) is None:
    #        flash('Invalid username')
    #    else:
    #        if check_password_hash(cred.password, form.password.data):
    #            return redirect(url_for('browse'))
    #       else:
    #            flash('Invalid password')
    #return render_template('login.html', title='Login', form=form)

    return render_template('login.html', title='Log in', signin=signin, signup=signup)

@app.route('/success')
@login_required
def logged_in():
    # Protected user content can be handled here
    return

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))