import paho.mqtt.client as paho

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

    def connect(self,broker="broker.mqttdashboard.com"):
        self.client.connect(broker, 1883)

        self.client.loop_start()
        self.client.loop_stop()

        return 'connected'
