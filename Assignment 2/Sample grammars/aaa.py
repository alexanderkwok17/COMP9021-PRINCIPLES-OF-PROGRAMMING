from math import sqrt


class equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.validate_equation():
            print('Incorrect data')

    def validate_equation(self):
        return self.a != 0

    def compute_roots(self):
        a = self.a
        b = self.b
        c = self.c
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return
        if delta == 0:
            self.root_1 = -b / (2*a)
            self.root_2 = root_1
        else:
            self.root_1 = (-b - sqrt(delta)) / (2*a)
            self.root_2 = (-b + sqrt(delta)) / (2*a)

