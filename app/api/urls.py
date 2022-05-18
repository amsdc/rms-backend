from app.api import app_api
from app.api import endpoints as e

app_api.add_resource(e.Login, "/users/sign_in")
app_api.add_resource(e.Register, "/users/sign_up")
app_api.add_resource(e.UserLists, "/users/all")
app_api.add_resource(e.UserInfo, "/users/<int:user_id>/")