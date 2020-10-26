import variables as var

###
# Epics definitions
###
prefix = 'MTEST-TRI:' 
pvdb = {

    #MOT1
    'POS' : {'type' : 'int', 'scan' : 0.2},
    'RBV' : {'type' : 'int', 'scan' : 0.2},
    'SPEED' : {'type' : 'int', 'scan' : 0.2}
}
