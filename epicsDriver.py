#!/usr/bin/env python

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import variables as var
from pcaspy import Driver, SimpleServer
import epicsDefinition as ed

class myDriver(Driver):
	def __init__(self):
		super(myDriver, self).__init__()

	def read(self, reason):

		return float(subscribe.simple(reason, hostname=var.mqtt_server).payload);

	def write(self, reason, value):
        	status = True
		publish.single(reason, str(value), hostname=var.mqtt_server);

        	if status:
			self.setParam(reason, value)
			return status

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(ed.prefix, ed.pvdb)
    driver = myDriver()
    print("Connected Epics")

while True:
	server.process(0.2)

