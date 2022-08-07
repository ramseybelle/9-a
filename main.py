class Point:
    def distance_to(self, point2):
        """

        :type point2: object
        """
        pass


point_1: Point = Point(7)
point_2 = Point(-6, 18)
print(point_1.distance_to(point_2))


class LineSegment:
    def length(self):
        pass

    def is_parallel_to(self, line_seg2):
        pass

    def slope(self):
        pass


line_seg_1 = LineSegment(point_2)
print(line_seg_1.length())
print(line_seg_1.slope())

point_3 = Point(-2, 2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment()
print(line_seg_1.is_parallel_to(line_seg_2))
