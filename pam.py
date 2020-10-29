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
con = connectionManager.connect()
PyTrinamic.showInfo()
M0 = MOT(con,0)
M1 = MOT(con,1)
M2 = MOT(con,2)
M3 = MOT(con,3)
M4 = MOT(con,4)  # vextra
M5 = MOT(con,5)

M0.setAxisParameter(140, 5) #microstep 32
M0.setAxisParameter(6, 130) # run current
M0.setAxisParameter(7, 2) # halt current
M0.setAxisParameter(174, 9)
M0.setAxisParameter(182, 14000)
M0.setAxisParameter(181, 14000)
M0.setAxisParameter(5, 400000)
M0.setMaxVelocity(15000)

M1.setAxisParameter(140, 5) #microstep 32
M1.setAxisParameter(6, 130) # run current
M1.setAxisParameter(7, 2) # halt current
M1.setAxisParameter(174, 9)
M1.setAxisParameter(182, 14000)
M1.setAxisParameter(181, 14000)
M1.setAxisParameter(5, 400000)
M1.setMaxVelocity(15000)

M2.setAxisParameter(140, 5) #microstep 32
M2.setAxisParameter(6, 130) # run current
M2.setAxisParameter(7, 2) # halt current
M2.setAxisParameter(174, 9)
M2.setAxisParameter(182, 14000)
M2.setAxisParameter(181, 14000)
M2.setAxisParameter(5, 400000)
M2.setMaxVelocity(15000)

M3.setAxisParameter(140, 5) #microstep 32
M3.setAxisParameter(6, 130) # run current
M3.setAxisParameter(7, 2) # halt current
M3.setAxisParameter(174, 9)
M3.setAxisParameter(182, 12000)
M3.setAxisParameter(181, 12000)
M3.setAxisParameter(5, 30000)
M3.setMaxVelocity(15000)

M4.setAxisParameter(140, 5) #microstep 32
M4.setAxisParameter(6, 24) # run current
M4.setAxisParameter(7, 8) # halt current
M4.setAxisParameter(174, -2)
M4.setAxisParameter(182, 14000)
M4.setAxisParameter(181, 14000)
M4.setAxisParameter(5, 400000)
M4.setMaxVelocity(15000)

M5.setAxisParameter(140, 5) #microstep 32
M5.setAxisParameter(6, 130) # run current
M5.setAxisParameter(7, 2) # halt current
M5.setAxisParameter(174, 9)
M5.setAxisParameter(182, 12000)
M5.setAxisParameter(181, 12000)
M5.setAxisParameter(5, 30000)
M5.setMaxVelocity(15000)

stepRev = 200 * 32
mmStep = 1 / stepRev

# variables for tweek value
M0TWV = 1.0
M1TWV = 1.0
M2TWV = 1.0
M3TWV = 1.0
M4TWV = 1.0
M5TWV = 1.0

# topics to listen mqtt
topic =['STOP','SCAN',
	'M0.HOME','M0.SPEED','M0.POS','M0.RBV','M0.TWR','M0.TWF','M0.TWV',
	'M1.HOME','M1.SPEED','M1.POS','M1.RBV','M1.TWR','M1.TWF','M1.TWV',
	'M2.HOME','M2.SPEED','M2.POS','M2.RBV','M2.TWR','M2.TWF','M2.TWV',
	'M3.HOME','M3.SPEED','M3.POS','M3.RBV','M3.TWR','M3.TWF','M3.TWV',
	'M4.HOME','M4.SPEED','M4.POS','M4.RBV','M4.TWR','M4.TWF','M4.TWV',
	'M5.HOME','M5.SPEED','M5.POS','M5.RBV','M5.TWR','M5.TWF','M5.TWV']

# homing procedure
def home(inMotor, inTopic):
	inMotor.rotate(-15000)
	time.sleep(0.1)
	while inMotor.getActualVelocity() != 0:
		publish.single(inTopic, posInMm(inMotor.getActualPosition()), hostname=var.mqtt_server)
		time.sleep(0.2)
	inMotor.stop()
	time.sleep(0.1)
	hpos = inMotor.getActualPosition()
	inMotor.setAxisParameter(1,0)
	inMotor.moveTo(6400)

# convert a msg to an int value
def msg2Int(inMsg):
	return int(inMsg.payload.decode('UTF-8'))

def msg2Float(inMsg):
	return float(inMsg.payload.decode('UTF-8'))

def posInMm(pos):
	return float("{:.3f}".format(pos * mmStep))

def mm2Int(inMM):
	return int(inMM * stepRev)


def scan():
	publish.single('M0.RBV', posInMm(M0.getActualPosition()), hostname=var.mqtt_server)
	publish.single('M1.RBV', posInMm(M1.getActualPosition()), hostname=var.mqtt_server)
	publish.single('M2.RBV', posInMm(M2.getActualPosition()), hostname=var.mqtt_server)
	publish.single('M3.RBV', posInMm(M3.getActualPosition()), hostname=var.mqtt_server)
	publish.single('M4.RBV', posInMm(M4.getActualPosition()), hostname=var.mqtt_server)
	publish.single('M5.RBV', posInMm(M5.getActualPosition()), hostname=var.mqtt_server)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	for x in topic:
		client.subscribe(x)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	global M0TWV, M1TWV, M2TWV, M3TWV, M4TWV, M5TWV

	if msg.payload == '': break;

	if msg.topic == 'STOP': M0.stop();M1.stop();M2.stop();M3.stop();M4.stop();M5.stop();
	elif msg.topic == 'SCAN': scan();

	elif msg.topic == 'M0.POS': M0.moveTo(mm2Int(msg2Float(msg)), M0.getMaxVelocity())
	elif msg.topic == 'M0.SPEED': M0.setMaxVelocity(mm2Int(msg2Float(msg)))
	elif msg.topic == 'M0.HOME': home(M0, 'M0.RBV')
	elif msg.topic == 'M0.TWR': M0.moveTo(M0.getActualPosition() - mm2Int(M0TWV), M0.getMaxVelocity())
	elif msg.topic == 'M0.TWF': M0.moveTo(M0.getActualPosition() + mm2Int(M0TWV), M0.getMaxVelocity())
	elif msg.topic == 'M0.TWV': M0TWV = msg2Float(msg)

	elif msg.topic == 'M1.POS': M1.moveTo(mm2Int(msg2Float(msg)), M1.getMaxVelocity())
	elif msg.topic == 'M1.SPEED': M1.setMaxVelocity(mm2Int(msg2Float(msg)))
	elif msg.topic == 'M1.HOME': home(M1, 'M1.RBV')
	elif msg.topic == 'M1.TWR': M1.moveTo(M1.getActualPosition() - mm2Int(M1TWV), M1.getMaxVelocity())
	elif msg.topic == 'M1.TWF': M1.moveTo(M1.getActualPosition() + mm2Int(M1TWV), M1.getMaxVelocity())
	elif msg.topic == 'M1.TWV': M1TWV = msg2Float(msg)

	elif msg.topic == 'M2.POS': M2.moveTo(mm2Int(msg2Float(msg)), M2.getMaxVelocity())
	elif msg.topic == 'M2.SPEED': M2.setMaxVelocity(mm2Int(msg2Float(msg)))
	elif msg.topic == 'M2.HOME': home(M2, 'M2.RBV')
	elif msg.topic == 'M2.TWR': M2.moveTo(M2.getActualPosition() - mm2Int(M2TWV), M2.getMaxVelocity())
	elif msg.topic == 'M2.TWF': M2.moveTo(M2.getActualPosition() + mm2Int(M2TWV), M2.getMaxVelocity())
	elif msg.topic == 'M2.TWV': M2TWV = msg2Float(msg)

	elif msg.topic == 'M3.POS': M3.moveTo(mm2Int(msg2Float(msg)), M3.getMaxVelocity())
	elif msg.topic == 'M3.SPEED': M3.setMaxVelocity(mm2Int(msg2Float(msg)))
	elif msg.topic == 'M3.HOME': home(M3, 'M3.RBV')
	elif msg.topic == 'M3.TWR': M3.moveTo(M3.getActualPosition() - mm2Int(M3TWV), M3.getMaxVelocity())
	elif msg.topic == 'M3.TWF': M3.moveTo(M3.getActualPosition() + mm2Int(M3TWV), M3.getMaxVelocity())
	elif msg.topic == 'M3.TWV': M3TWV = msg2Float(msg)

	elif msg.topic == 'M4.POS': M4.moveTo(mm2Int(msg2Float(msg)), M4.getMaxVelocity())
	elif msg.topic == 'M4.SPEED': M4.setMaxVelocity(mm2Int(msg2Float(msg)))
	elif msg.topic == 'M4.HOME': home(M4, 'M4.RBV')
	elif msg.topic == 'M4.TWR': M4.moveTo(M4.getActualPosition() - mm2Int(M4TWV), M4.getMaxVelocity())
	elif msg.topic == 'M4.TWF': M4.moveTo(M4.getActualPosition() + mm2Int(M4TWV), M4.getMaxVelocity())
	elif msg.topic == 'M4.TWV': M4TWV = msg2Float(msg)

	elif msg.topic == 'M5.POS': M5.moveTo(mm2Int(msg2Float(msg)), M5.getMaxVelocity())
	elif msg.topic == 'M5.SPEED': M5.setMaxVelocity(mm2Int(msg2Float(msg)))
	elif msg.topic == 'M5.HOME': home(M5, 'M5.RBV')
	elif msg.topic == 'M5.TWR': M5.moveTo(M5.getActualPosition() - mm2Int(M5TWV), M5.getMaxVelocity())
	elif msg.topic == 'M5.TWF': M5.moveTo(M5.getActualPosition() + mm2Int(M5TWV), M5.getMaxVelocity())
	elif msg.topic == 'M5.TWV': M5TWV = msg2Float(msg)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(var.mqtt_server, var.mqtt_port, var.mqtt_timeout)
#client.loop_start()
client.loop_forever()
