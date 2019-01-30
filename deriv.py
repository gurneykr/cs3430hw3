#!/usr/bin/python

####################################
# Krista
# A01671888
####################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_pwr, make_pwr_expr
import math

def deriv(expr):
    if isinstance(expr, const):
        return const_deriv(expr)
    elif isinstance(expr, pwr):
        return pwr_deriv(expr)
    elif isinstance(expr, prod):
        return prod_deriv(expr)
    elif isinstance(expr, plus):
        return plus_deriv(expr)
    else:
        raise Exception('deriv:' + repr(expr))

# the derivative of a consant is 0.
def const_deriv(c):
    assert isinstance(c, const)
    return const(val=0.0)

def plus_deriv(s):
    return plus(deriv(s.get_elt1()), deriv(s.get_elt2()))

def pwr_deriv(p):
    assert isinstance(p, pwr)
    b = p.get_base()
    d = p.get_deg()
    if isinstance(b, var):
        if isinstance(d, const):
            return prod(d , pwr(b, prod(d, const(-1))))
        elif isinstance(d, plus):
            return prod(d, pwr(b, prod(d ,const(-1))))
        else:
            raise Exception('pwr_deriv: case 1: ' + str(p))
    if isinstance(b, pwr):  # think this is (x^2 (^3))
        if isinstance(d, const):
           return prod(b.get_base(), prod(b.get_deg(), const))
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))
    elif isinstance(b, plus):  # (x+2)^3
        if isinstance(d, const):
            return prod(d, pwr(b, d.get_val()-1))
        else:
            raise Exception('pwr_deriv: case 3: ' + str(p))
    elif isinstance(b, prod):#(3x)^2 => (2*3*x)^(2-1)
        if isinstance(d, const):
            pwr( prod(d, prod(b.get_mult1(), b.get_mult2())), d.get_val()-1)
        else:
            raise Exception('pwr_deriv: case 4: ' + str(p))
    else:
        raise Exception('power_deriv: case 5: ' + str(p))

def prod_deriv(p):
    assert isinstance(p, prod)
    m1 = p.get_mult1()  # 6
    m2 = p.get_mult2()  # x^3
    if isinstance(m1, const):
        if isinstance(m2, const):
            return const(0)
        elif isinstance(m2, pwr):  # 6*(x^3)=> 6*3*(x^(3-1))
            # get 6 * 3
            alt1 = prod(m1, m2.get_deg())
            # get x^3-1
            alt2 = pwr(m2.get_base(), plus(m2.get_deg(), const(-1)))
            return prod(alt1, alt2)
        elif isinstance(m2, plus):  # 3*(x+1)
            if isinstance(deriv(m2), const):
                return const(0)
            else:
                return prod(m1, deriv(m2))
        elif isinstance(m2, prod):  # 4*(3x)
            if isinstance(deriv(m2), const):
                return const(0)
            else:
                return prod(m1, deriv(m2))
        else:
            raise Exception('prod_deriv: case 0' + str(p))
    elif isinstance(m1, plus):
        if isinstance(m2, const):  # (x+1)*3
            if isinstance(deriv(m2), const):
                return const(0)
            else:
                return prod(m1, deriv(m2))
        # elif isinstance(m2, pwr):  # (1+x)*(2^3)
        #     pass
        # elif isinstance(m2, plus):  # (1+x)*(x+3)
        #     pass
        # elif isinstance(m2, prod):  # (3+x)*(2x)
        #     pass
        else:
            raise Exception('prod_deriv: case 1:' + str(p))
    elif isinstance(m1, pwr):
        if isinstance(m2, const):  # (x^2)*3 => (2x^1)*3
            if isinstance(deriv(m2), const):
                return const(0)
            else:
                return prod(deriv(m1), m2)
        else:
            raise Exception('prod_deriv: case 2:' + str(p))

    elif isinstance(m1, prod):
        if isinstance(m2, const):#(3x)*4
            if isinstance(deriv(m2), const):
                return const(0)
            else:
                return prod(deriv(m1), m2)
        else:
            return prod(m1, deriv(m2))
    else:
       raise Exception('prod_deriv: case 4:' + str(p))