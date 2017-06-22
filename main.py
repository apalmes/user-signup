#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask User Sign-up re: LaunchCode
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/user-signup/


from flask import Flask, redirect, request, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True 


@app.route('/', methods=['POST', 'GET'])
def user_signup():

    username = ''
    email = ''
    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    title = 'User Sign-up'

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if (len(username) < 3) or (len(username) > 20) or (username == "") or (username.count(" ") > 0):
            user_error = "That is not a valid username"
            username = ''

        if (len(password) < 3) or (len(password) > 20) or (password == "") or (password.count(" ") > 0):
            password_error = "That is not a valid password"

        if (verify != password) or (password == ""):
            verify_error = "The passwords do not match"

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = "That is not a valid email"
            email = ''
    
        if (not user_error) and (not password_error) and (not verify_error) and (not email_error):
            return redirect('/welcome?username={0}'.format(username))

    return render_template('sign-up.html', title=title, username=username, email=email, user_error=user_error,
                           password_error=password_error, verify_error=verify_error, email_error=email_error)


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    title = 'Welcome!'
    return render_template('welcome.html', title=title, username=username)


if __name__ == '__main__':
    app.run()
