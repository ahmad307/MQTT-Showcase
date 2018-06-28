from django.shortcuts import render
from mqtt.paho_client import Connection

def index(request):
    result = {}
    if request.method == 'POST':
        client = Connection()
        broker = request.POST.get('host')
        port = int(request.POST.get('port'))

        client.connect(broker,port)
        result['connection_result'] = 'Connected'

    return render(request, 'mqtt/index.html', result)
