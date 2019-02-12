from eventlet import wsgi
import eventlet
from threading import Lock
from flask import Flask, request
from flask_socketio import SocketIO, emit
from kafka import KafkaConsumer
import json

async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

with open('config_consumer.json', 'r') as f:
    config = json.load(f)

consumer = KafkaConsumer(bootstrap_servers=config['KAFKA_BROKER'],
                         sasl_plain_username=config['KAFKA_USERNAME'],
                         sasl_plain_password=config['KAFKA_PASSWORD'],
                         auto_offset_reset='largest',
                         security_protocol='SASL_SSL',
                         sasl_mechanism='PLAIN',
                         ssl_check_hostname=False,
                         ssl_cafile=config["SSL_CAFILE"],
                         ssl_certfile=config["SSL_CERTFILE"],
                         ssl_keyfile=config["SSL_KEYFILE"])
consumer.subscribe([config["TOPIC"]])


def background_thread():
    for message in consumer:
        socketio.sleep(0)
        message = eval(message.value.decode("utf-8").replace("L", ''))

        acc = list(message[0])
        gyro = list(message[1])
        timestamp = message[2]

        message_json = [
          {"x": acc[0], "y": acc[1], "z": acc[2]},
          {"roll": gyro[0], "pitch": gyro[1], "yaw": gyro[2]},
          timestamp
        ]

        socketio.emit(
          'response', message_json)


@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('response', {'data': []})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    wsgi.server(eventlet.listen(('localhost', 5000)), app)

