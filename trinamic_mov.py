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
M1 = MOT(myInterface,0)
M2 = MOT(myInterface,1)
M3 = MOT(myInterface,2)


print("-----------------")
#print(driverBoard.showMotionConfiguration())
print("-----------------")

M2.setAxisParameter(140, 5) #microstep 32
M2.setAxisParameter(6, 24) # run current
M2.setAxisParameter(7, 8) # halt current
M2.setAxisParameter(174, -2)
M2.setAxisParameter(182, 14000)

M2.setAxisParameter(181, 14000)
M2.setAxisParameter(5, 400000)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(var.topic_mot1_pos)
	client.subscribe('STOP')
	client.subscribe(var.topic_mot1_rbv)
	client.subscribe(var.topic_mot1_rbc)
	client.subscribe('M1.HOME')

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	if msg.topic == var.topic_mot1_pos:
		pos = int(msg.payload.decode('UTF-8'))
		M2.moveTo(pos, 15000)

	elif msg.topic == 'M1.HOME':
		M2.rotate(15000)
		while M2.getAxisParameter(3) != 0: time.sleep(0.1)
		M2.stop()
		M2.setAxisParameter(1, 0)

	elif msg.topic == var.topic_mot1_rbc: rbv = M2.getActualPosition(); publish.single(var.topic_mot1_rbv, rbv, hostname=var.mqtt_server)
	elif msg.topic == 'STOP':
		M2.stop()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(var.mqtt_server, var.mqtt_port, var.mqtt_timeout)
#client.loop_start()
client.loop_forever()
