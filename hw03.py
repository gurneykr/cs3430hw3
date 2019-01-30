#!/usr/bin/python

#######################################
# module: hw03.py
# YOUR NAME
# YOUR A#
#######################################

# place all necessary imports here.
#
# I placed the updated version of maker.py
# Use it as you see fit.

def maximize_revenue(dmnd_eq, constraint=lambda x: x >= 0):
    # your code here
    pass

def dydt_given_x_dxdt(yt, x, dxdt):
    # your code here
    pass

def oil_disk_test():
    yt = make_prod(make_const(0.02*math.pi),
                    make_pwr('r', 2.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                             make_const(20.0))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)

def arm_tumor_test():
    # your code here
    pass
    
