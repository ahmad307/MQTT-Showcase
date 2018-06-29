from django.shortcuts import render,HttpResponse
from mqtt.paho_client import Connection
import json

def index(request):
    return render(request,'mqtt/index.html')

def post(request):
    if request.method == 'POST':
        # Get entered data
        broker = request.POST.get('host')
        port = int(request.POST.get('port'))
        id = request.POST.get('client_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        keepalive = int(request.POST.get('keep_alive'))

        # Establish a connection through 'Connection' class
        if len(username) != 0 and len(password) != 0:
            client = Connection(id, username, password)
        else:
            client = Connection(id)
        client.connect(broker, port, keepalive)

    return HttpResponse(json.dumps({}),content_type='application/json')

