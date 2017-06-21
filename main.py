from flask import Flask, redirect, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

def user():
    user=username = request.form['username']

@app.route('/sign-up', methods=['POST'])
def user_signup():
    

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    password_error= ''
    verify_error=''
    email_error=''

    if (len(username) < 3) or (len(username) > 20) or username == "":
        user_error = "That is not a valid username"
        
    for char in username:
        if char == " ":
            user_error = "That is not a valid username"
            
    if (len(password) < 3) or (len(password) > 20) or password == "":
        password_error = "That is not a valid password"
    
    for char in password:
        if char == " ":
            password_error = 'That is not a valid password'
    
    if (verify != password) or password == '':
        verify_error="The passwords do not match"


    if (len(email) < 3)  or (len(email) > 20) and '@' or "." not in email:
        email_error = "That is not a valid email"
    
    if email == "":
        email_error= ""

    for char in email:
        if char == " ":
            email_error= 'That is not a valid email'
    
    if not user_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('sign-up.html', title='User Sign-up', user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome', methods=['GET','POST'])

def welcome():
    username=request.args.get('username')
    
    return render_template('welcome.html', title='Welcome!', username=username)

@app.route('/')
def index():
    
    return render_template('sign-up.html', title='User Sign-up')

app.run()