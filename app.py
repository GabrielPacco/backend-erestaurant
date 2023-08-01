import os
from app import create_app, socketio

app = create_app()

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)