# zommath2
zommath but remade and decancerified

this currently features quadratic and buy one get one calculation
to use bogo do
from zommath2 import bogocalc
bogocalc(however many you buy,how many you get,how much off,buy price of item)
bogocalc(10,1,100,1)

to use Quadratic do
from zommath2 import Quadratic
first you will need to make a Quadratic object and provide the a, b, and c of the Quadratic
q = Quadratic(1,2,-3)
the solutions are
q.plusans()
and
q.minusans()
the Determinant can be gotten by
q.deter()

you can change the a, b and c with
set_nums()
use it like this:
q.set_nums()
