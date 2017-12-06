from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tuple = (x, y)

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def mag(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def norm(self):
        return self / self.mag()