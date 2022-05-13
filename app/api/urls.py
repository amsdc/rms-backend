from app.api import app_api
from app.api import endpoints as e

app_api.add_resource(e.Login, "/login")