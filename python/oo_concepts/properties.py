import unittest

import math


class Properties(unittest.TestCase):
    def test_property_type(self):
        class Rectangle(object):
            def __init__(self, width, height):
                self._width = width
                self._height = height

            def get_area(self):
                return self._height * self._width

            area = property(get_area, doc='Area of the rectangle')

        r = Rectangle(10, 10)
        self.assertEqual(100, r.area)

    # def test_property_decorator(self):
    #     class Rectangle(object):
    #         def __init__(self, width, height):
    #             self._width = width
    #             self._height = height
    #
    #         @property
    #         def area(self):
    #             return self._height * self._width
    #
    #         @area.setter
    #         def area(self, scale):
    #             self._width /= scale
    #             self._height /= scale
    #
    #     r = Rectangle(10, 10)
    #     self.assertEqual(100, r.area)
    #     r.area(10)
    #     self.assertEqual(1, r.area)
    #
    def test_x(self):
        class Rectangle(object):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            @property
            def area(self):
                '''area of the rectangle'''
                return self.width * self.height

            @area.setter
            def area(self, value):
                scale = math.sqrt(value / self.area)
                self.width *= scale
                self.height *= scale

        r = Rectangle(10, 10)
        self.assertEqual(100, r.area)

        r.area = 10
        self.assertAlmostEqual(10, r.area, 1)


if __name__ == '__main__':
    unittest.main()
