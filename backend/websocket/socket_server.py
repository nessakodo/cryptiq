from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('send_message')
def handle_send(data):
    emit('receive_message', data, broadcast=True)
