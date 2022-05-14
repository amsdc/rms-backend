from flask_restful import Resource, abort

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