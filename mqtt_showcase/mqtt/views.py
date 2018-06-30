from django.shortcuts import render,HttpResponse
from mqtt.paho_client import Connection
import json
import time

# Global connection variable
client = None

def index(request):
    """Directs to main index page."""
    return render(request,'mqtt/index.html')

def post(request):
    """
    Receives forms submission and connects/publishes/subscribes depending
    on the submitted form.
    :param request:  Ajax POST request.
    """
    # Access global client object throughout the scope
    global client

    form_name = request.POST.get('hiddenattr')
    if request.method == 'POST':
        if form_name == 'publish':
            topic = request.POST.get('topic')
            message = request.POST.get('message')
            try:
                client.publish(topic,message)
            except(AttributeError):
                return HttpResponse(json.dumps({'message':'Not Connected'}),content_type='applicaiton/json')

        elif form_name == 'subscribe':
            topic = request.POST.get('subscribe_topic')
            client.subscribe(topic)

        # If form is 'connection_form'
        else:
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

def post_disconnect(request):
    """End connection created in 'client' object.
    :param request: ajax POST request.
    """
    global client
    if request.method == 'POST':
        client.disconnect()

    return HttpResponse(json.dumps({}),content_type='application/json')

def get_messages(request):
    global client
    messages = client.messages
    time.sleep(1)
    print("get_messages",messages)
    return HttpResponse(json.dumps({'messages':messages}),content_type='appliaction/json')