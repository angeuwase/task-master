from project.auth import auth_blueprint
from flask import render_template, current_app, redirect, url_for, flash, request
from project.forms import RegistrationForm, LoginForm
from project.models import User
from project import db
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash
from werkzeug.urls import url_parse



@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        

        user = User.query.filter_by(email=email).first()

        if user:
            flash('You already have an account. Please sign in.')
            return redirect(url_for('auth.login'))

        else:
            new_user = User(email, password)

            try:
                db.session.add(new_user)
                db.session.commit()
                flash('You have been registered. Please login')
                current_app.logger.info('New user added to the database: {}'.format(new_user.email))
                return redirect(url_for('auth.login'))


            except:
                flash('An error occured while trying to register you. Please try again')
                current_app.logger.error('An error occured while trying to register a new user')

    return render_template('auth/register.html', form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        
        if user:

            if user.is_password_valid(password):
                login_user(user)
                flash('You have been logged in')
                current_app.logger.info('User signed into the application: {}'.format(user.email))

                next_page = request.args.get('next')
                
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('auth.profile')
                return redirect(next_page)
            else:
                form.email.data = ''
                flash('Incorrect username or password')
                current_app.logger.info('Login attempt with invalid credentials: {}'.format(user.email))


        else:
            flash('You do not have an account. Please sign up')
            return redirect(url_for('auth.register'))

    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')

@auth_blueprint.route('/logout')
@login_required
def logout():
    current_app.logger.info('User logged out: {}'.format(current_user.email))
    logout_user()
    return render_template('main/index.html')


