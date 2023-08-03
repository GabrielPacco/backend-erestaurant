from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
#from .routes import main 

socketio = SocketIO()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    @app.route('/')
    def home():
        return render_template('index.html')

    #app.register_blueprint(main)
    CORS(app, origins=['https://frontend-erestaurant-768a1a368801.herokuapp.com/'])
    #CORS(app)
    socketio.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    socketio.run(app)
