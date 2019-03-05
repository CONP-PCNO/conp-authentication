from app import app
from flask import render_template
from app.forms import SignInForm
from app.forms import SignUpForm

@app.route('/')
@app.route('/login')
def login():

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