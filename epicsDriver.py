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
		
		return subscribe.simple(reason, hostname=var.mqtt_server).payload;
		'''
		if reason == 'M0.RBV': value = subscribe.simple('M0.RBV', hostname=var.mqtt_server).payload;
                elif  reason == 'M1.RBV': value = subscribe.simple('M1.RBV', hostname=var.mqtt_server).payload;
                elif  reason == 'M2.RBV': value = subscribe.simple('M2.RBV', hostname=var.mqtt_server).payload;
                elif  reason == 'M3.RBV': value = subscribe.simple('M3.RBV', hostname=var.mqtt_server).payload;
                elif  reason == 'M4.RBV': value = subscribe.simple('M4.RBV', hostname=var.mqtt_server).payload;
                elif  reason == 'M5.RBV': value = subscribe.simple('M5.RBV', hostname=var.mqtt_server).payload;
		
		
		else: value = self.getParam(reason)
		return value
		'''
		
	def write(self, reason, value):
        	status = True
		publish.single(reason, value, hostname=var.mqtt_server);
		'''
		if reason == 'STOP': publish.single('STOP', value, hostname=var.mqtt_server);
			
		elif reason == 'M0.HOME': 	publish.single('M0.HOME', value, hostname=var.mqtt_server);
                elif reason == 'M0.SPEED': 	publish.single('M0.SPEED', value, hostname=var.mqtt_server);
                elif reason == 'M0.POS': 	publish.single('M0.POS', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWR': 	publish.single('M0.TWR', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWF': 	publish.single('M0.TWF', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWV': 	publish.single('M0.TWV', value, hostname=var.mqtt_server);
			
		elif reason == 'M0.HOME': 	publish.single('M0.HOME', value, hostname=var.mqtt_server);
                elif reason == 'M0.SPEED': 	publish.single('M0.SPEED', value, hostname=var.mqtt_server);
                elif reason == 'M0.POS': 	publish.single('M0.POS', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWR': 	publish.single('M0.TWR', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWF': 	publish.single('M0.TWF', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWV': 	publish.single('M0.TWV', value, hostname=var.mqtt_server);                

		elif reason == 'M0.HOME': 	publish.single('M0.HOME', value, hostname=var.mqtt_server);
                elif reason == 'M0.SPEED': 	publish.single('M0.SPEED', value, hostname=var.mqtt_server);
                elif reason == 'M0.POS': 	publish.single('M0.POS', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWR': 	publish.single('M0.TWR', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWF': 	publish.single('M0.TWF', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWV': 	publish.single('M0.TWV', value, hostname=var.mqtt_server);
			
		elif reason == 'M0.HOME': 	publish.single('M0.HOME', value, hostname=var.mqtt_server);
                elif reason == 'M0.SPEED': 	publish.single('M0.SPEED', value, hostname=var.mqtt_server);
                elif reason == 'M0.POS': 	publish.single('M0.POS', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWR': 	publish.single('M0.TWR', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWF': 	publish.single('M0.TWF', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWV': 	publish.single('M0.TWV', value, hostname=var.mqtt_server);
			
		elif reason == 'M0.HOME': 	publish.single('M0.HOME', value, hostname=var.mqtt_server);
                elif reason == 'M0.SPEED': 	publish.single('M0.SPEED', value, hostname=var.mqtt_server);
                elif reason == 'M0.POS': 	publish.single('M0.POS', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWR': 	publish.single('M0.TWR', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWF': 	publish.single('M0.TWF', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWV': 	publish.single('M0.TWV', value, hostname=var.mqtt_server);
			
		elif reason == 'M0.HOME': 	publish.single('M0.HOME', value, hostname=var.mqtt_server);
                elif reason == 'M0.SPEED': 	publish.single('M0.SPEED', value, hostname=var.mqtt_server);
                elif reason == 'M0.POS': 	publish.single('M0.POS', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWR': 	publish.single('M0.TWR', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWF': 	publish.single('M0.TWF', value, hostname=var.mqtt_server);
                elif reason == 'M0.TWV': 	publish.single('M0.TWV', value, hostname=var.mqtt_server);
		'''
        	if status:
			self.setParam(reason, value)
			return status

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(ed.prefix, ed.pvdb)
    driver = myDriver()

while True:
	server.process(0.2)

