from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from routes.message_routes import message_routes
from routes.auth_routes import auth_routes
from websocket.socket_server import socketio

app = Flask(__name__)
CORS(app)
app.register_blueprint(message_routes)
app.register_blueprint(auth_routes)
socketio.init_app(app, cors_allowed_origins='*')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
