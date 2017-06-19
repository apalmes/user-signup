from flask import Flask, redirect, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route('/welcome', methods=['POST'])
def user_signup():
    

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error= ''
    verify_error=''
    email_error=''

    if len(username) < 3 or len(username) > 20 or username == "":
        user_error = "That is not a valid username"
        
    for char in username:
        if char == " ":
            user_error = "That is not a valid username"
            
    if len(password) < 3 or len(password) > 20 or password == "":
        pass_error = "That is not a valid password"
    
    for char in password:
        if char == " ":
            pass_error = 'That is not a valid password'
    
    if verify != password or password == '':
        verify_error="The passwords do not match"


    if len(email) < 3  or len(email) > 20 and '@' or "." not in email:
        email_error = "That is not a valid email"
    
    if email == "":
        email_error= ""

    for char in email:
        if char == " ":
            email_error= 'That is not a valid email'
    
    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return render_template('signup.html', user_error=user_error, pass_error=pass_error, verify_error=verify_error, email_error=email_error)
    
@app.route('/')
def index():
    
    return render_template('signup.html', title='User Signup')

app.run()