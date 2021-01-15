import glob

###
# MQTT brocker and topics
###
mqtt_server = "localhost"
mqtt_port = 1883
mqtt_timeout = 60

###
# exchange information beween mqtt and epics
###
ports = glob.glob('/dev/ttyACM*')
TMCM_NO_MOT_PER_MODULE = 6


#get the number of TMCM
TMCM_NO = len(ports)
MOT_ELEMENTS = TMCM_NO_MOT_PER_MODULE * TMCM_NO
