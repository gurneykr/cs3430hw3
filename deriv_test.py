from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot
from tof import tof
from deriv import deriv
import unittest
import math

class Assign01UnitTests(unittest.TestCase):
    def test_01(self):
        print('\n***** Test 01 ***********')
        e1 = make_plus(make_pwr('x', 1.0), make_const(1.0))
        e2 = make_pwr('x', 3.0)
        e3 = make_prod(make_const(5.0), make_pwr('x', 1.0))
        e4 = make_plus(e2, e3)
        e5 = make_plus(e4, make_const(2.0))
        e6 = make_prod(e1, e5)
        drv = deriv(e6)
        assert not drv is None
        print('-- derivative is:\n')
        print(e6)
        print(drv)
        e6f = tof(drv)
        assert not e6f is None
        gt = lambda x: 4.0 * (x ** 3) + 3 * (x ** 2) + 10.0 * x + 7.0
        print('\n Comparison with ground truth:\n')
        err = 0.00001
        for i in range(10):
            value = e6f(i)
            print(value, gt(i))
            assert abs(e6f(i) - gt(i)) <= err
        print('Test 01:pass')
        #(x+1)(3x^2+5) + (x^3+5x+2)

    def test_02(self):
        print('\n***** Test 02 ***********')
        e1 = make_prod(make_const(2.0), make_pwr('x', 4.0))
        e2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
        e3 = make_plus(e1, e2)
        e4 = make_plus(e3, make_const(1.0))
        e5 = make_prod(make_const(-1.0), make_pwr('x', 5.0))
        e6 = make_plus(e5, make_const(1.0))
        e7 = make_prod(e4, e6)
        print('-- function expression is:\n')
        print(e7)
        drv = deriv(e7)
        assert not drv is None
        print('\n - - derivative is:\n')
        print(drv)
        e7f = tof(drv)
        assert not e7f is None
        gt = lambda x: -18.0 * (x ** 8) + 6.0 * (x ** 5) - 5.0 * (x ** 4) + 8.0 * (x ** 3) - 1.0
        err = 0.00001
        print('n - -comparison with ground truth:\n')
        for i in range(10):
            print(e7f(i), gt(i))
            assert abs(e7f(i) - gt(i)) <= err
        print('Test 02: pass')
    # def test_03(self):
    #     print('\n *****Test03 ***********')
    #     q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)), make_plus(
    #     make_pwr('x', 1.0), make_const(-3.0)))
    #     pex = make_pwr_expr(q, 3.0)
    #     print('-- function expression is:\n')
    #     print(pex)
    #     pexdrv = deriv(pex)
    #     print(pexdrv)
    def test_03(self):
        print('\n***** Test 03 ***********')
        q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)), make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        print('-- function expression is:\n')
        print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        print('\n - - derivative is:\n')
        print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0 * (((x + 11.0) ** 2) / ((x - 3.0) ** 4))
        err = 0.00001
        print('\n - -comparison with ground truth:\n')
        for i in range(10):
            if i != 3.0:
                print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= 0.001
        print('Test 03:pass')

    if __name__ == "__main__":
        unittest.main()