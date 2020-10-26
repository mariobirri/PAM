###
# MQTT brocker and topics
###
mqtt_server = "localhost"
mqtt_port = 1883
mqtt_timeout = 60

topic_mot1_speed = 'MOT1.SPEED'
topic_mot1_pos = 'MOT1.POS'
topic_mot1_rbv = 'MOT1.RBV'
topic_mot1_move ='MOT1.MOVE'
topic_mot1_rbc = 'MOT1.RBV_CHECK'


###
# Global variables to store the values for the bridge
###

#MOT1
mot1_nr = 0
mot1_move = 'false'
mot1_rbv = 0
