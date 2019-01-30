#!/usr/bin/python


###########################################
# module: tof.py
# Krista Gurney
# A01671888
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
import math

def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))

## here is how you can implement converting
## a constant to a function.
def const_tof(c):
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):#expb^d
        def f(x):
            if isinstance(d, const):
                return math.pow(expb, d.get_val())
            elif isinstance(d, var):
                return math.pow(expb, x)
            elif isinstance(d, prod):
                return math.pow(expb, prod_tof(d)(x))
            elif isinstance(d, plus):
                return math.pow(expb, plus_tof(d)(x))
        return f
    elif isinstance(expb, var):
        if isinstance(d, const):#x^2
            def f(x):
                return math.pow(x, d.get_val())
            return f
        elif isinstance(d, plus):
            def f(x):
                return math.pow(x, plus_tof(d)(x))
            return f
        elif isinstance(d, pwr):
            def f(x):
                return math.pow(x, pwr_tof(d)(x))
            return f
        elif isinstance(d, var):
            def f(x):
                return math.pow(x, x)
            return f
        elif isinstance(d, prod):
            def f(x):
                return math.pow(x, prod_tof(d)(x))
            return f
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif isinstance(expb, plus):
        if isinstance(d, const):#(1+x)^3
            def f(x):
                return math.pow( plus_tof(expb)(x), d.get_val())
            return f
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    elif isinstance(expb, pwr):#(x^2)^2
        if isinstance(d, const):
            def f(x):
                return math.pow( pwr_tof(expb)(x), d.get_val())
            return f
        else:
            raise Exception('pw_tof: case 3:' + str(expr))
    elif isinstance(expb, prod):
        if isinstance(d, const):#4^(3x)
            def f(x):
                return math.pow(prod_tof(expb)(x), d.get_val())
            return f
        else:
            raise Exception('pw_tof: case 4:' + str(expr))
    else:
        raise Exception('pw_tof: case 5:' + str(expr))

def prod_tof(expr):
    assert isinstance(expr, prod)
    m1 = expr.get_mult1()
    m2 = expr.get_mult2()

    if isinstance(m1, const):
        if isinstance(m2, const):
            def f(x):
                return m1.get_val()*m2.get_val()
            return f
        elif isinstance(m2, prod):
            def f(x):
                return m1.get_val()*prod_tof(m2)(x)
            return f
        elif isinstance(m2, pwr):
            def f(x):
                return m1.get_val()*pwr_tof(m2)(x)
            return f
        elif isinstance(m2, plus):
            def f(x):
                return m1.get_val()*plus_tof(m2)(x)
            return f
        elif isinstance(m2, var):
            def f(x):
                return m1.get_val()*x
            return f
    elif isinstance(m1, prod):
        if isinstance(m2, const):
            def f(x):
                return prod_tof(m1)(x)*m2.get_val()
            return f
        elif isinstance(m2, prod):
            def f(x):
                return prod_tof(m1)(x)*prod_tof(m2)(x)
            return f
        elif isinstance(m2, pwr):
            def f(x):
                return prod_tof(m1)(x)*pwr_tof(m2)(x)
            return f
        elif isinstance(m2, plus):
            def f(x):
                return prod_tof(m1)(x)*plus_tof(m2)(x)
            return f
        elif isinstance(m2, var):
            def f(x):
                return prod_tof(m1)(x)*x
            return f
    elif isinstance(m1, pwr):
        if isinstance(m2, const):
            def f(x):
                return pwr_tof(m1)(x)*m2.get_val()
            return f
        elif isinstance(m2, prod):
            def f(x):
                return pwr_tof(m1)(x)*prod_tof(m2)(x)
            return f
        elif isinstance(m2, pwr):
            def f(x):
                return pwr_tof(m1)(x)*pwr_tof(m2)(x)
            return f
        elif isinstance(m2, plus):
            def f(x):
                return pwr_tof(m1)(x)*plus_tof(m2)(x)
            return f
        elif isinstance(m2, var):
            def f(x):
                return pwr_tof(m1)(x)*x
            return f
    elif isinstance(m1, plus):
        if isinstance(m2, const):
            def f(x):
                return plus_tof(m1)(x) + m2.get_val()
            return f
        elif isinstance(m2, prod):
            def f(x):
                return plus_tof(m1)(x) + prod_tof(m2)(x)
            return f
        elif isinstance(m2, pwr):
            def f(x):
                return plus_tof(m1)(x) + pwr_tof(m2)(x)
            return f
        elif isinstance(m2, plus):
            def f(x):
                return plus_tof(m1)(x) + plus_tof(m2)(x)
            return f
        elif isinstance(m2, var):
            def f(x):
                return plus_tof(m1)(x) + x
def plus_tof(expr):
    assert isinstance(expr, plus)
    elt1 = expr.get_elt1()
    elt2 = expr.get_elt2()

    if isinstance(elt1, const):
        if isinstance(elt2, const):
            def f(x):
                return elt1.get_val() + elt2.get_val()
            return f
        elif isinstance(elt2, prod):
            def f(x):
                return elt1.get_val() + prod_tof(elt2)(x)
            return f
        elif isinstance(elt2, pwr):
            def f(x):
                return elt1.get_val() + pwr_tof(elt2)(x)
            return f
        elif isinstance(elt2, plus):
            def f(x):
                return elt1.get_val() + plus_tof(elt2)(x)
            return f
    elif isinstance(elt1, prod):
        if isinstance(elt2, const):
            def f(x):
                return prod_tof(elt1)(x) + elt2.get_val()
            return f
        elif isinstance(elt2, prod):
            def f(x):
                return prod_tof(elt1)(x) + prod_tof(elt2)(x)
            return f
        elif isinstance(elt2, pwr):
            def f(x):
                return prod_tof(elt1)(x) + pwr_tof(elt2)(x)
            return f
        elif isinstance(elt2, plus):
            def f(x):
                return prod_tof(elt1)(x) + plus_tof(elt2)(x)
            return f
    elif isinstance(elt1, pwr):
        if isinstance(elt2, const):
            def f(x):
                return pwr_tof(elt1)(x) + elt2.get_val()
            return f
        elif isinstance(elt2, prod):
            def f(x):
                return pwr_tof(elt1)(x) + prod_tof(elt2)(x)
            return f
        elif isinstance(elt2, pwr):
            def f(x):
                return pwr_tof(elt1)(x) + pwr_tof(elt2)(x)
            return f
        elif isinstance(elt2, plus):
            def f(x):
                return pwr_tof(elt1)(x) + plus_tof(elt2)(x)
            return f
    elif isinstance(elt1, plus):
        if isinstance(elt2, const):
            def f(x):
                return plus_tof(elt1)(x) + elt2.get_val()
            return f
        elif isinstance(elt2, prod):
            def f(x):
                return plus_tof(elt1)(x) + prod_tof(elt2)(x)
            return f
        elif isinstance(elt2, pwr):
            def f(x):
                return plus_tof(elt1)(x) + pwr_tof(elt2)(x)
            return f
        elif isinstance(elt2, plus):
            def f(x):
                return plus_tof(elt1)(x) + plus_tof(elt2)(x)
            return f
