# Copyright (c) 2022 AKNP Solutions

# This file is part of RMS Backend.

# RMS Backend is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# RMS Backend is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with RMS Backend.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, request, current_app

from flask_mysqldb import MySQL

from config import Config

mysql = MySQL()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    mysql.init_app(app)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
