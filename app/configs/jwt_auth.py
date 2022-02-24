from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os

def init_app(app: Flask):
    
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=60)
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET")
    
    JWTManager(app)