from django.shortcuts import render
from mqtt.paho_client import Connection

def index(request):
    client = Connection()
    print(client.connect('broker.mqttdashboard.com'))

    return render(request, 'mqtt/index.html')
