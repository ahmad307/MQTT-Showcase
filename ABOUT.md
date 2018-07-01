## Goal
This web application applies *MQTT connectivity protocol* to send and receive messages, using publish and subscribe pattern. It mimics *HiveMQ* web client (http://www.hivemq.com/demos/websocket-client/).

## Tools
### Back-End
The application uses *Django* back-end framework and *Eclipse Paho Python Client*. *Paho* is an implementation of the *MQTT* protocol.

### Front-End
Bootstrap and JQuery front-end libraries.

## Process
The Django project has one application called ```mqtt```. Under ```mqtt/views.py``` (responsible for controlling the app template) an object of ```Connection``` class is created, where this object takes responsibility of starting/ending MQTT connections, publishing/subscribing to topics etc..

Connection and publishing requests are made by Ajax ```POST``` requests to the server (i.e. views.py) and template is rendered according to the received response.

## Experience
Upon starting the project I had had several months experience with Django having built more than one application with it, and had known JavaScript and other front-end technologies for over a year. However, my Django knowledge was deeper.

I had never dealt with *MQTT* or any connectivity protocol and had next to none knowledge about networking in general.

During the project I specifically brushed up on my *JQuery* knowledge, aside understanding *MQTT* protocol and how is it really useful.