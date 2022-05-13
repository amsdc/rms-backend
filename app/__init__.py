from flask import Flask, request, current_app
from flask_restful import Api

api = Api()

def create_app():

    app = Flask(__name__)
    # app.config.from_object(config_class)

    api.init_app(app)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
