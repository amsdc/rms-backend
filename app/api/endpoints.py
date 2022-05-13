from flask_restful import Resource, abort

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
