import paho.mqtt.client as paho
import time

class Connection:
    """Establishes MQTT connection through Paho python client"""

    def __init__(self,id,username=None,password=None):
        """Creates a client instance with a random ID if no ID is given"""
        self.client = paho.Client(client_id=id)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log
        self.client_id = self.client._client_id

        if username!=None and password!=None:
            self.client.username_pw_set(username,password)

    def on_connect(self, client, userdata, flags, rc):
        # Debug message
        print('Connected!')

    def on_disconnect(self, client, userdata, rc):
        print('Disconnected!')

    def on_log(self,client, userdata, level, buf):
        # Debug message
        print('log!')

    def connect(self,broker,port,keepalive):
        """Establishes a connection with the given host"""
        self.client.connect(host=broker, port=port,keepalive=keepalive)
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()