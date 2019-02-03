from poly12 import find_poly_1_zeros, find_poly_2_zeros
from deriv import deriv
from prod import prod
from const import const
from plus import plus
from var import var
from pwr import pwr
from quot import quot
from tof import tof
from derivtest import loc_xtrm_1st_drv_test
from point2d import point2d

from maker import make_const, make_prod, make_plus, make_pwr
def maximize_revenue(demand_expr, constraint):
    priceExpr = demand_expr
    priceExprFn = tof(priceExpr)
    revenueExpr =  mult_x(priceExpr)

    extrema = loc_xtrm_1st_drv_test(revenueExpr)

    for i, j in extrema:
        if i == "max":
            x = j.get_x().get_val()
            if constraint(j.get_x().get_val()):
                price = priceExprFn(j.get_x().get_val())
                max_revenue = price * j.get_x().get_val()

    return [(const(x)),(const(max_revenue)),(const(price))]

def mult_x(expr):#1/12x^2 - 10x + 300

    if isinstance(expr, plus):
        if isinstance(expr.get_elt2(), const):
            return plus(mult_x(expr.get_elt1()), prod(expr.get_elt2(), make_pwr('x', 1.0)))
        else:
            return plus(mult_x(expr.get_elt1()), mult_x(expr.get_elt2()))
    elif isinstance(expr, pwr):
        if isinstance(expr.get_deg(), const):
            return pwr(expr.get_base(), const(expr.get_deg().get_val()+1))
        else:
            return pwr(mult_x(expr.get_base()), mult_x(expr.get_deg()))
    elif isinstance(expr, prod):
        return prod(mult_x(expr.get_mult1()), mult_x(expr.get_mult2()))
    elif isinstance(expr, quot):
        return quot(mult_x(expr.get_num()), mult_x(expr.get_denom()))
    else:
        return expr

def test01():
    print("***Max Revenue Test 01 *****")
    e1 = make_prod( make_const(1.0/12.0), make_pwr('x', 2.0))
    e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
    sum1 = make_plus(e1, e2)
    demand_expr = make_plus(sum1, make_const(300.0))
    num_units, rev, price = maximize_revenue(demand_expr, constraint=lambda x: 0 <= x <= 60)
    print('x = ', num_units.get_val())
    print("rev= ", rev.get_val())
    print('price = ', price.get_val())
    print("Max Revenue Test: pass")


if __name__ == "__main__":
    test01()