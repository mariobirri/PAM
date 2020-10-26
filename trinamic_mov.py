#!/usr/bin/env python3

import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import variables as var
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from MOT import MOT
import time

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
PyTrinamic.showInfo()
M0 = MOT(myInterface,0)
M1 = MOT(myInterface,1)

M1.setAxisParameter(140, 5) #microstep 32
M1.setAxisParameter(6, 24) # run current
M1.setAxisParameter(7, 8) # halt current
M1.setAxisParameter(174, -2)
M1.setAxisParameter(182, 14000)
M1.setAxisParameter(181, 14000)
M1.setAxisParameter(5, 400000)
M1.setMaxVelocity(15000)

topic =['STOP','M1.HOME','M1.SPEED','M1.POS','M1.RBV','M1.SCAN']


# convert a msg to an int value
def msg2Int(inMsg):
	return int(inMsg.payload.decode('UTF-8'))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	for x in topic:
		client.subscribe(x)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	if msg.topic == 'STOP': M1.stop()
	elif msg.topic == 'M1.SCAN': publish.single('M1.RBV', M1.getActualPosition(), hostname=var.mqtt_server)
	elif msg.topic == 'M1.POS': M1.moveTo(msg2Int(msg), M1.getMaxVelocity())
	elif msg.topic == 'M1.SPEED': M1.setMaxVelocity(msg2Int(msg))
	elif msg.topic == 'M1.HOME':
		M1.rotate(15000)
		while M1.getAxisParameter(3) != 0: time.sleep(0.1)
		M1.stop()
		M1.setAxisParameter(1, 0)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(var.mqtt_server, var.mqtt_port, var.mqtt_timeout)
#client.loop_start()
client.loop_forever()
