from django.shortcuts import render
from mqtt.paho_client import Connection

def index(request):
    response = {}
    response['submit_btn_text'] = 'Connect'
    if request.method == 'POST':
        # Get entered data
        broker = request.POST.get('host')
        port = int(request.POST.get('port'))
        id = request.POST.get('client_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        keepalive = int(request.POST.get('keep_alive'))

        # Establish a connection through 'Connection' class
        if len(username)!=0 and len(password)!=0:
            client = Connection(id,username,password)
        else:
            client = Connection(id)
        client.connect(broker,port,keepalive)

        response['connection_result'] = 'Connected'
        response['submit_btn_text'] = 'Disconnect'

    return render(request, 'mqtt/index.html', response)
