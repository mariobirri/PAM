import variables as var

###
# Epics definitions
###
prefix = 'MTEST-PAM:' 
pvdb = {

	#MOT0
	'M0.POS' : 	{'type' : 'float', 	'scan' : 0.2,	'prec' : 3},
	'M0.RBV' : 	{'type' : 'float', 	'scan' : 0.2,	'prec' : 3},
	'M0.SPEED' : 	{'type' : 'float', 	'scan' : 0.2,	'prec' : 3},
	'M0.HOME' : 	{'type' : 'int', 	'scan' : 0.2},
	'M0.TWR' : 	{'type' : 'int', 	'scan' : 0.2},
	'M0.TWF' : 	{'type' : 'int',	'scan' : 0.2},
	'M0.TWV' : 	{'type' : 'int', 	'scan' : 0.2},

	#MOT1
	'M1.POS' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M1.RBV' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M1.SPEED' :    {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M1.HOME' :     {'type' : 'int',        'scan' : 0.2},
	'M1.TWR' :      {'type' : 'int',        'scan' : 0.2},
	'M1.TWF' :      {'type' : 'int',        'scan' : 0.2},
	'M1.TWV' :      {'type' : 'int',        'scan' : 0.2},

	#MOT2
	'M2.POS' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M2.RBV' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M2.SPEED' :    {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M2.HOME' :     {'type' : 'int',        'scan' : 0.2},
	'M2.TWR' :      {'type' : 'int',        'scan' : 0.2},
	'M2.TWF' :      {'type' : 'int',        'scan' : 0.2},
	'M2.TWV' :      {'type' : 'int',        'scan' : 0.2},

	#MOT3
	'M3.POS' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M3.RBV' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M3.SPEED' :    {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M3.HOME' :     {'type' : 'int',        'scan' : 0.2},
	'M3.TWR' :      {'type' : 'int',        'scan' : 0.2},
	'M3.TWF' :      {'type' : 'int',        'scan' : 0.2},
	'M3.TWV' :      {'type' : 'int',        'scan' : 0.2},

	#MOT4
	'M4.POS' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M4.RBV' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M4.SPEED' :    {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M4.HOME' :     {'type' : 'int',        'scan' : 0.2},
	'M4.TWR' :      {'type' : 'int',        'scan' : 0.2},
	'M4.TWF' :      {'type' : 'int',        'scan' : 0.2},
	'M4.TWV' :      {'type' : 'int',        'scan' : 0.2},

	#MOT5
	'M5.POS' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M5.RBV' :      {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M5.SPEED' :    {'type' : 'float',      'scan' : 0.2,	'prec' : 3},
	'M5.HOME' :     {'type' : 'int',        'scan' : 0.2},
	'M5.TWR' :      {'type' : 'int',        'scan' : 0.2},
	'M5.TWF' :      {'type' : 'int',        'scan' : 0.2},
	'M5.TWV' :      {'type' : 'int',        'scan' : 0.2},
}
