#!/usr/bin/env python

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import variables as var
from pcaspy import Driver, SimpleServer

prefix = 'MTEST-TRI:'
pvdb = {
    'MA1-M1-POS' :   {'TYPE': 'int', 'PREC' : 3, 'SCAN' : 0.2},
    'MA1-M1-RBV' :   {'TYPE': 'int', 'PREC' : 3, 'SCAN' : 0.2},
    'MA1-M1-SPEED' : {'TYPE': 'int', 'PREC' : 3, 'SCAN' : 0.2},
}

class myDriver(Driver):
	def __init__(self):
		super(myDriver, self).__init__()

	def read(self, reason):
		if reason == 'MA1-M1-RBV': value = subscribe.simple(var.topic_mot1_rbv, hostname=var.mqtt_server).payload;
                elif  reason == 'MA1-M2-RBV': value = subscribe.simple(var.topic_mot2_rbv, hostname=var.mqtt_server).payload;
                elif  reason == 'MA1-M3-RBV': value = subscribe.simple(var.topic_mot3_rbv, hostname=var.mqtt_server).payload;
                elif  reason == 'MA2-M1-RBV': value = subscribe.simple(var.topic_mot4_rbv, hostname=var.mqtt_server).payload;
                elif  reason == 'MA2-M2-RBV': value = subscribe.simple(var.topic_mot5_rbv, hostname=var.mqtt_server).payload;
                elif  reason == 'MA2-M3-RBV': value = subscribe.simple(var.topic_mot6_rbv, hostname=var.mqtt_server).payload;

		else: value = self.getParam(reason)
		return value

	def write(self, reason, value):
        	status = True
		if reason == 'MA1-M1-POS': publish.single(var.topic_mo1_pos, value, hostname=var.mqtt_server); 
		elif reason == 'MA1-M2-POS': publish.single(var.topic_mo2_pos, value, hostname=var.mqtt_server);
                elif reason == 'MA1-M3-POS': publish.single(var.topic_mo3_pos, value, hostname=var.mqtt_server);
                elif reason == 'MA2-M1-POS': publish.single(var.topic_mo4_pos, value, hostname=var.mqtt_server);
                elif reason == 'MA2-M2-POS': publish.single(var.topic_mo5_pos, value, hostname=var.mqtt_server);
                elif reason == 'MA2-M3-POS': publish.single(var.topic_mo6_pos, value, hostname=var.mqtt_server);
                elif reason == 'MA1-M1-SPEED': publish.single(var.topic_mo1_speed, value, hostname=var.mqtt_server);
                elif reason == 'MA1-M2-SPEED': publish.single(var.topic_mo2_speed, value, hostname=var.mqtt_server);
                elif reason == 'MA1-M3-SPEED': publish.single(var.topic_mo3_speed, value, hostname=var.mqtt_server);
                elif reason == 'MA2-M1-SPEED': publish.single(var.topic_mo4_speed, value, hostname=var.mqtt_server);
                elif reason == 'MA2-M2-SPEED': publish.single(var.topic_mo5_speed, value, hostname=var.mqtt_server);
                elif reason == 'MA2-M3-SPEED': publish.single(var.topic_mo6_speed, value, hostname=var.mqtt_server);


        	if status:
			self.setParam(reason, value)
			return status

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = myDriver()

while True:
	server.process(0.1)

