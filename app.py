from eventlet import wsgi
import eventlet
from threading import Lock
from flask import Flask, request
from flask_socketio import SocketIO, emit
from kafka import KafkaConsumer

async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


consumer = KafkaConsumer('topic',
                         bootstrap_servers='...:....',
                         auto_offset_reset='largest')


def background_thread():
    for message in consumer:
        socketio.sleep(0)
        message = message.value.decode("utf-8")
        message = message[message.find('['):-1]

        socketio.emit(
          'response', {'data': message})


@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('response', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    wsgi.server(eventlet.listen(('localhost', 5000)), app)
