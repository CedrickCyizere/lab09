#!/usr/bin/env python3

from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        """
        >>> p = Point(3, 4)
        >>> p
        Point(3, 4)
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        >>> p = Point(3, 4)
        >>> repr(p)
        'Point(3, 4)'
        """
        return f"Point({self.x}, {self.y})"

    def translate(self, dx, dy):
        """
        >>> p = Point(3, 4)
        >>> p.translate(1, 2)
        Point(4, 6)
        """
        return Point(self.x + dx, self.y + dy)

class Rectangle:
    def __init__(self, upper_left=Point(), lower_right=Point()):
        """
        >>> r = Rectangle(Point(1, 1), Point(4, 5))
        >>> r
        Rectangle(Point(1, 1), Point(4, 5))
        """
        self.upper_left = upper_left
        self.lower_right = lower_right

    def __repr__(self):
        """
        >>> r = Rectangle(Point(1, 1), Point(4, 5))
        >>> repr(r)
        'Rectangle(Point(1, 1), Point(4, 5))'
        """
        return f"Rectangle({self.upper_left}, {self.lower_right})"

    def area(self):
        """
        >>> r = Rectangle(Point(1, 1), Point(4, 5))
        >>> r.area()
        12
        """
        width = abs(self.lower_right.x - self.upper_left.x)
        height = abs(self.upper_left.y - self.lower_right.y)
        return width * height

    def perimeter(self):
        """
        >>> r = Rectangle(Point(1, 1), Point(4, 5))
        >>> r.perimeter()
        14
        """
        width = abs(self.lower_right.x - self.upper_left.x)
        height = abs(self.upper_left.y - self.lower_right.y)
        return 2 * (width + height)

    def translate(self, dx, dy):
        """
        >>> r = Rectangle(Point(1, 1), Point(4, 5))
        >>> r.translate(1, 2)
        Rectangle(Point(2, 3), Point(5, 7))
        """
        return Rectangle(self.upper_left.translate(dx, dy), self.lower_right.translate(dx, dy))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
