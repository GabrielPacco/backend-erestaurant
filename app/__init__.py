from flask import Flask 
from flask_cors import CORS
from .events import socketio
#from .routes import main 

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    #app.register_blueprint(main)
    CORS(app, origins=['https://frontend-erestaurant-768a1a368801.herokuapp.com/'])
    #CORS(app)
    socketio.init_app(app)

    return app