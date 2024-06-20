from math import pi


class Point:
    """A simple class about (x, y) data points"""

    def __init__(self, x, y):
        """Input an (x, y) data point"""
        self.x = x
        self.y = y

    def radius(self):
        """returns distance from (x, y) to origin"""
        return (self.x**2 + self.y**2) ** 0.5

    def rect_area(self):
        """returns area of rectangle with a vertex at (x, y) centered
        around origin"""
        return 4.0 * abs(self.x * self.y)

    def circ_area(self):
        """returns area of circle through (x, y) centered around
        origin"""
        return pi * self.radius() ** 2


if __name__ == "__main__":
    p1 = Point(6, 8)
    print("p1.radius() =", p1.radius())
    print("p1.rect_area() =", p1.rect_area())
    print("p1.circ_area() =", p1.circ_area())
    p2 = Point(3, 4)
    print("p2.radius() =", p2.radius())
    print("p2.rect_area() =", p2.rect_area())
    print("p2.circ_area() =", p2.circ_area())
    print("p1.x = {0}, p1.y = {1}".format(p1.x, p1.y))
    print("p2.x = {0}, p2.y = {1}".format(p2.x, p2.y))
    help(Point.radius)
