from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    microsoft_login_url = url_for('microsoft_login', _external=True)
    return f'<a href="{microsoft_login_url}">SignIn with Microsoft</a>'

@app.route('/login/microsoft')
def microsoft_login():
    redirect_uri = 'http://localhost:5000/login/callback'
    client_id = 'XXXX'

    oauth_authorize_url = (
        'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
        f'?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=User.Read%20openid%20profile%20email'
    )
    return redirect(oauth_authorize_url)

@app.route('/login/callback')
def microsoft_callback():
    # Here you will receive the authorization code from Microsoft.
    # You'll need to exchange this code for an access token using a POST request.

    # Example of exchanging the code for an access token (you need to implement this logic):
    # exchange_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
    # data = {
    #     'grant_type': 'authorization_code',
    #     'code': received_code,
    #     'client_id': client_id,
    #     'redirect_uri': redirect_uri,
    #     'client_secret': your_client_secret
    # }
    # response = requests.post(exchange_url, data=data)
    # access_token = response.json().get('access_token')

    # Once you have the access token, you can make requests to Microsoft Graph API to get user information.

    return "Welcome!."

if __name__ == '__main__':
    app.run(debug=True)
