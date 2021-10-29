
"""
Factory Design Pattern

Motivation:
 - Object creation logic becomes too convoluted
 - Initializer is not descriptive
 - Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to:
   . A separate method (Factory method)
   . That may exist in a separate class (Factory)
   . Can create hierarchy of factories with Abstract Factory
"""


from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

   # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
   #     if system == CoordinateSystem.CARTESIAN:
   #         self.x = a
   #         self.y = b
   #     elif system == CoordinateSystem.POLAR:
   #         self.x = a * sin(b)
   #         self.y = a * sin(b)

# Factory method
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

# Factory class
    class PointFactory:

        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.PointFactory.new_polar_point(1, 2)
