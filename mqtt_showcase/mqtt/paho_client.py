import paho.mqtt.client as paho
import time

class Connection:
    def __init__(self):
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_log = self.on_log

    def on_connect(self,client, userdata, flags, rc):
        # Debug message
        print('Connected')

    def on_log(self,client, userdata, level, buf):
        # Debug message
        print('log!')

    def connect(self,broker,port):
        self.client.connect(broker, port)
        self.client.loop_start()
        self.client.loop_stop()
