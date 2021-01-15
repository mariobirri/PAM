import variables as var 

##
# Epics definitions
###
prefix = 'MTEST-PAM:' 

pvdb = {}
for x in range(var.MOT_ELEMENTS):
	pvdb["M" + str(x) + ".POS"] =   {'type' : 'float',      'scan' : 0.2,   'prec' : 3}
	pvdb["M" + str(x) + ".RBV"] =   {'type' : 'float',      'scan' : 0.2,   'prec' : 3}
	pvdb["M" + str(x) + ".SPEED"] = {'type' : 'float',      'scan' : 0.2,   'prec' : 3}
	pvdb["M" + str(x) + ".HOME"] =  {'type' : 'int',        'scan' : 0.2}
	pvdb["M" + str(x) + ".TWR"] =   {'type' : 'int',        'scan' : 0.2}
        pvdb["M" + str(x) + ".TWF"] =   {'type' : 'int',        'scan' : 0.2}
        pvdb["M" + str(x) + ".TWV"] =   {'type' : 'int',        'scan' : 0.2}

print(pvdb)
