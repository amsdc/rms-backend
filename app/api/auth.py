from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import check_password_hash
from flask import abort, current_app
import jwt
import time

from app import mysql

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    if user:
        password_hash = user[2]
        if check_password_hash(password_hash, password):
            return user[0]

@basic_auth.error_handler
def basic_auth_error(status):
    abort(403, "Invalid username or password")

def generate_token(user_id):
    return jwt.encode({'user_id': user_id,
                'exp': time.time() + 600},
    current_app.config['SECRET_KEY'], algorithm='HS256')


@token_auth.verify_token
def verify_token(token):
    try:
        jtkn = jwt.decode(token, current_app.config['SECRET_KEY'],
        algorithms=['HS256'])
        # print(jtkn)
        return jtkn["user_id"]
    except:
        return None
        

@token_auth.error_handler
def token_auth_error(status):
    abort(401, "You have not supplied a token in the headers or"
               " the token issued by your client is invalid.")