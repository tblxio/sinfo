import eventlet
from threading import Lock
from flask import Flask, request
from flask_socketio import SocketIO, emit
from kafka import KafkaConsumer
import json
import pandas as pd
from ds.model_saving import load_model
import os

# flask approach based on example:
# https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/example/app.py
async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

with open('config_consumer.json', 'r') as f:
    config = json.load(f)

path_model = os.path.join(os.getcwd(),
                          'ds/models/harsh_events.model')

model = load_model(path_model)

consumer = KafkaConsumer(bootstrap_servers=config['KAFKA_BROKER'],
                         sasl_plain_username=config['KAFKA_USERNAME'],
                         sasl_plain_password=config['KAFKA_PASSWORD'],
                         auto_offset_reset='largest',
                         security_protocol='SASL_SSL',
                         sasl_mechanism='PLAIN',
                         ssl_check_hostname=False,
                         ssl_cafile=config['SSL_CAFILE'],
                         ssl_certfile=config['SSL_CERTFILE'],
                         ssl_keyfile=config['SSL_KEYFILE'])
consumer.subscribe([config['TOPIC']])


def background_thread():

    i = 0
    gap = 0
    window_size = 21
    point_gap = 10
    harsh_acc = 0
    harsh_turn = 0
    signals_name = ['accel_x', 'accel_y', 'accel_z',
                    'gyro_roll', 'gyro_pitch', 'gyro_yaw']

    signals = np.zeros((window_size, len(signals_name)))

    # consume records from a Kafka cluster
    for message in consumer:
        socketio.sleep(0)
        message = eval(message.value.decode('utf-8').replace('L', ''))

        acc = list(message[0])
        gyro = list(message[1])
        timestamp = message[2]

        # fill signals with measurements
        if i < window_size:
            signals[i, :] = acc[0], acc[1], acc[2], gyro[0], gyro[1], gyro[2]

        # once the array is full - use FIFO approach
        else:
            signals[0: window_size - 1, :] = signals[1: window_size, :]
            signals[-1, :] = acc[0], acc[1], acc[2], gyro[0], gyro[1], gyro[2]

        # evaluate every new point_gap data points
        if gap >= point_gap and i > window_size:
            df = pd.DataFrame(signals, columns=signals_name)
            pred = model.predict(df)
            harsh_acc = pred['harsh_accel']
            harsh_turn = pred['harsh_turn']
            gap = 0

        i += 1
        gap += 1

        message_json = [
          {'x': acc[0], 'y': acc[1], 'z': acc[2]},
          {'roll': gyro[0], 'pitch': gyro[1], 'yaw': gyro[2]},
          timestamp,
          str(harsh_acc),
          str(harsh_turn)
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
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
