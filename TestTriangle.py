# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TriangleTests(unittest.TestCase):
    # ----- valid triangles -----
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(7, 7, 7), "Equilateral")

    def test_isosceles_all_permutations(self):
        for a, b, c in [(5, 5, 3), (5, 3, 5), (3, 5, 5)]:
            with self.subTest(sides=(a, b, c)):
                self.assertEqual(classifyTriangle(a, b, c), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene")

    def test_right_345_all_orders(self):
        for a, b, c in [(3, 4, 5), (5, 3, 4), (4, 5, 3)]:
            with self.subTest(sides=(a, b, c)):
                self.assertEqual(classifyTriangle(a, b, c), "Right")

    def test_right_5_12_13(self):
        self.assertEqual(classifyTriangle(5, 12, 13), "Right")

    def test_not_triangle_equality_boundary(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "NotATriangle")

    def test_not_triangle_strict(self):
        self.assertEqual(classifyTriangle(2, 3, 6), "NotATriangle")

    def test_zero_and_negative(self):
        bads = [(0, 4, 5), (4, 0, 5), (4, 5, 0),
                (-1, 2, 2), (2, -1, 2), (2, 2, -1)]
        for s in bads:
            with self.subTest(sides=s):
                self.assertEqual(classifyTriangle(*s), "InvalidInput")

    def test_non_integers(self):
        for s in [(3.5, 4, 5), ("3", 4, 5), (True, 4, 5)]:
            with self.subTest(sides=s):
                self.assertEqual(classifyTriangle(*s), "InvalidInput")

    # common spec guard: sides must be <= 200
    def test_too_large_values(self):
        for s in [(201, 10, 10), (10, 201, 10), (10, 10, 201)]:
            with self.subTest(sides=s):
                self.assertEqual(classifyTriangle(*s), "InvalidInput")

if __name__ == "__main__":
    unittest.main()
