from flask_restful import Resource, abort

from app import mysql

# from app.models import Announcement, Achievement
# from app.api.helpers import remove_html_tags

class Login(Resource):
    def get(self):
        """get 
        
        Get all the announcements, in a JSON form. Then in static site,
        we will add a parser to render like in achievements.
        """
        return {
                "user_id": 1234,
                "username": "user",
                "password": "passwd",
                "user_type": "manager" or "customer"
            }

class UserLists(Resource):
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