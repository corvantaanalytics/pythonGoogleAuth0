from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    google_login_url = url_for('google_login', _external=True)
    print("google_login_url :: ",google_login_url)
    return f'<a href="{google_login_url}">SignIn</a>'

@app.route('/login/google')
def google_login():
    redirect_uri = 'http://localhost:5000/login/callback'
    client_id = 'XXXX'

    oauth_authorize_url = (
        'https://accounts.google.com/o/oauth2/auth'
        f'?response_type=token&client_id={client_id}&redirect_uri={redirect_uri}&scope=openid%20profile%20email'
    )
    print("oauth_authorize_url",oauth_authorize_url)
    return redirect(oauth_authorize_url)

@app.route('/login/callback')
def google_callback():
    return "Welcome!."

if __name__ == '_main_':
    app.run(debug=True)