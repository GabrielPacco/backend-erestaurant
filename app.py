from app import create_app, socketio

app = create_app()
socketio.init_app(app)
