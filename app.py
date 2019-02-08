from eventlet import wsgi
import eventlet
from threading import Lock
from flask import Flask, request
from flask_socketio import SocketIO, emit, disconnect

async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# background task example
def background_thread():
    count = 0
    data = []
    while True:
        socketio.sleep(3)
        count += 1
        data.append(count)
        socketio.emit(
            'response', {'connected': True, 'data': data, 'count': count})

@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)

if __name__ == '__main__':
    wsgi.server(eventlet.listen(('', 5000)), app)
