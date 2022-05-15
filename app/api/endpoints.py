from flask_restful import (
    Resource, 
    abort, 
    reqparse
)

from werkzeug.security import generate_password_hash

from app import mysql
from app.api.auth import basic_auth, generate_token, token_auth


# from app.models import Announcement, Achievement
# from app.api.helpers import remove_html_tags

class Login(Resource):
    decorators = [basic_auth.login_required]
    def get(self):
        user_id = basic_auth.current_user()
        return {
            "token": generate_token(user_id)
        }


class UserLists(Resource):
    
    decorators = [token_auth.login_required]
    
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        users_tup = cur.fetchall()
        ret_list = []
        for user_tup in users_tup:
            ret_list.append({
                                "user_id": user_tup[0],
                                "username": user_tup[1],
                                "password": user_tup[2],
                                "user_type": user_tup[3]
                            })
        return ret_list

class Register(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True,
            help = 'No username provided', location = 'json')
        self.reqparse.add_argument('password', type = str, required = True,
            help = 'No password provided', location = 'json')
        super().__init__()
    
    def post(self):
        data = self.reqparse.parse_args()
        username = data["username"]
        password = generate_password_hash(data["password"])
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password, user_type) VALUES (%s, %s, 'customer')", (username, password))
        mysql.connection.commit()

"""
Template
class <<resource_name>>(Resource):
    
    decorators = [token_auth.login_required]
    
    def get(self):
        <<your code>>
    
    def post(self):
        <<your code>>
    
    ... for other HTTP methods

NOTE: Replace things in << >> as applicable.
"""