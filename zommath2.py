from math import sqrt


def bogocalc(buy, get, discount, price):
    total = buy + get

    buy_cost = buy * price
    get_cost = get * price
    unitprice = buy_cost + get_cost * (1 - discount / 100)
    return unitprice / total


class Quadratic:
    def __init__(self, a=None, b=None, c=None):
        self._a = a
        self._b = b
        self._c = c

    def set_nums(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def deter(self):
        return self._b**2 - 4 * self._a * self._c

    def plusans(self):
        top_plus = self._b - sqrt(self.deter())
        plus_ans = top_plus / (2 * self._a)

        return plus_ans

    def minusans(self):
        top_minus = self._b + sqrt(self.deter())
        minus_ans = top_minus / (2 * self._a)

        return minus_ans

    def __str__(self):
        return f"{self._a}x^2 + {self._b}x + {self._c}"


if __name__ == "__main__":
    q = Quadratic(1, 2, -3)
    print(f"-2 ± √({q.deter()})")
    for a in range(1, 10):
        q.set_nums(a, 2, -3)
        print(f"Solving: {q}")
        print(f"Plus ans: {q.plusans()}")
        print(f"Minus ans: {q.minusans()}")
        print(f"Determinant: {q.deter()}")




#3 for 3 sale
#buy x get y z% off`
