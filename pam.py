#!/usr/bin/env python3

import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import variables as var
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from MOT import MOT
import time

MOT_ELEMENTS = 9
M = [None] * MOT_ELEMENTS
cm = [None] * 2
con = [None] * 2

MOT_TWV_DEFAULT = 1.0
MTWV = [MOT_TWV_DEFAULT] * MOT_ELEMENTS
 
cm[0] = ConnectionManager('--port /dev/ttyACM1 --module-id 1')
cm[1] = ConnectionManager('--port /dev/ttyACM0 --module-id 2')

con[0] = cm[0].connect()
con[1] = cm[1].connect()


# init the motors
for x in range(len(M)):
	if x < 6:
		M[x] = MOT(con[0],x)
	else:
		M[x] = MOT(con[1],x-6)
	print(x)
	print(x-6)
	print(M[x])

# set the motor parameters
for x in range(len(M)):
	if x != 4:
		M[x].setAxisParameter(140, 5) #microstep 32
		M[x].setAxisParameter(6, 130) # run current
		M[x].setAxisParameter(7, 2) # halt current
		M[x].setAxisParameter(174, 9)
		M[x].setAxisParameter(182, 14000)
		M[x].setAxisParameter(181, 14000)
		M[x].setAxisParameter(5, 400000)
		M[x].setMaxVelocity(15000)
	else:
		M[x].setAxisParameter(140, 5) #microstep 32
		M[x].setAxisParameter(6, 24) # run current
		M[x].setAxisParameter(7, 8) # halt current
		M[x].setAxisParameter(174, -2)
		M[x].setAxisParameter(182, 14000)
		M[x].setAxisParameter(181, 14000)
		M[x].setAxisParameter(5, 400000)
		M[x].setMaxVelocity(15000)

stepRev = 200 * 32
mmStep = 1 / stepRev


# topics to listen mqtt
topic =['STOP','SCAN']
for x in range(len(M)):
	topic.append('M' + str(x) + '.HOME');
	topic.append('M' + str(x) + '.SPEED');
	topic.append('M' + str(x) + '.POS');
	topic.append('M' + str(x) + '.RBV');
	topic.append('M' + str(x) + '.TWR');
	topic.append('M' + str(x) + '.TWF');
	topic.append('M' + str(x) + '.TWV');

print(topic)

# homing procedure
def home(inMotor, inTopic):
	inMotor.rotate(-15000)
	time.sleep(0.1)
	while inMotor.getActualVelocity() != 0:
		publish.single(inTopic, posInMm(inMotor.getActualPosition()), hostname=var.mqtt_server)
		time.sleep(0.2)
	inMotor.stop()
	time.sleep(0.1)
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
	for x in range(len(M)):
		publish.single('M' + str(x) + '.RBV', posInMm(M[x].getActualPosition()), hostname=var.mqtt_server)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected TMCM")
	for x in topic:
		client.subscribe(x)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	global MTWV

	if msg.payload == '': msg.payload = 0;

	if msg.topic == 'STOP': 
		for x in range(len(M)): 
			M[x].stop();

	elif msg.topic == 'SCAN': scan();

	elif msg.topic[0] == 'M' and msg.topic[1].isnumeric():
		indexOfPoint = msg.topic.find('.')

		if indexOfPoint == -1: 
			print('cannot find point');
		else:
			MOTNR = int(msg.topic[1:indexOfPoint])
			CMD = msg.topic[indexOfPoint+1:]
			if CMD == 'POS': M[MOTNR].moveTo(mm2Int(msg2Float(msg)), M[MOTNR].getMaxVelocity());
			elif CMD == 'SPEED': M[MOTNR].setMaxVelocity(mm2Int(msg2Float(msg)));
			elif CMD == 'HOME': home(M[MOTNR], 'M' + str(MOTNR) + '.RBV');
			elif CMD == 'TWR': M[MOTNR].moveTo(M[MOTNR].getActualPosition() - mm2Int(MTWV[MOTNR]), M[MOTNR].getMaxVelocity()) ;
			elif CMD == 'TWF': M[MOTNR].moveTo(M[MOTNR].getActualPosition() + mm2Int(MTWV[MOTNR]), M[MOTNR].getMaxVelocity()) ;
			elif CMD == 'TWV': MTWV[MOTNR] = msg2Float(msg);



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(var.mqtt_server, var.mqtt_port, var.mqtt_timeout)
#client.loop_start()
client.loop_forever()
