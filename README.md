# MQTT-Showcase
Web client for MQTT connectivity protocol. Mimics HiveMQ web client (http://www.hivemq.com/demos/websocket-client/).

## Set it up locally

### Requirements
* Python 3.x (3.6 recommended).
* Django (1.11.6 Recommended).
* paho-mqtt

After installing Python, use ```pip``` to install required packages.

### Instructions
* Clone this repository using ```git clone https://github.com/ahmad307/MQTT-Showcase.git```.
* Replace ```SECRET_KEY``` value in line 23 in ```settings.py``` file under ```mqtt_showcase``` directory with any Django project's secret key.
* Navigate to repository folder in your terminal and use ```python manage.py runserver``` command. (consider using ```py``` instead of ```python``` if the previous command didn't work).
* Your server is up and running!


***
You might encounter a ```Please Connect First``` error in the live version of the application, we are working on solving this problem.
