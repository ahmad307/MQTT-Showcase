import paho.mqtt.client as paho

class Connection:
    """Establishes MQTT connection through Paho python client"""

    def __init__(self,id,username=None,password=None):
        """Creates a client instance with a random ID if no ID is given.
        :param username: String
        :param password: String
        """
        self.client = paho.Client(client_id=id)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log
        self.client.on_publish = self.on_publish
        self.client.on_message = self.on_message
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

    def on_publish(self, client, userdata, mid):
        print('Published!')

    def on_message(self, client, userdata, msg):
        """Called when a message is published by a subscribed topic."""
        print('message:', str(msg.payload).replace("b'",""))

    def connect(self, broker,port, keepalive):
        """Establishes a connection with the given host.
        :param broker: String of the host to connect to
        :param port: Integer with the port number
        :param keepalive: Integer with the up period
        :return:
        """
        self.client.connect(host=broker, port=port,keepalive=keepalive)
        self.client.loop_start()

    def disconnect(self):
        """Ends previously built connection with the host."""
        self.client.loop_stop()
        self.client.disconnect()

    def publish(self, topic, message):
        """
        :param topic: String of the topic under which to publish the message
        :param message: String of the message to be published
        :return: None
        """
        self.client.publish(topic, message, qos=1)

    def subscribe(self, topic):
        """
        :param topic: String of the topic to subscribe to.
        :return: None
        """
        self.client.subscribe(topic,qos=1)