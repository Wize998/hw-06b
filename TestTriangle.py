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

    def test_T01_equilateral_7_7_7(self):
        self.assertEqual(classifyTriangle(7, 7, 7), "Equilateral")

    def test_T02_isosceles_5_5_3(self):
        self.assertEqual(classifyTriangle(5, 5, 3), "Isosceles")

    def test_T03_isosceles_5_3_5(self):
        self.assertEqual(classifyTriangle(5, 3, 5), "Isosceles")

    def test_T04_isosceles_3_5_5(self):
        self.assertEqual(classifyTriangle(3, 5, 5), "Isosceles")

    def test_T05_scalene_4_5_6(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene")

    def test_T06_right_3_4_5(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")

    def test_T07_right_5_3_4(self):
        self.assertEqual(classifyTriangle(5, 3, 4), "Right")

    def test_T08_right_4_5_3(self):
        self.assertEqual(classifyTriangle(4, 5, 3), "Right")

    def test_T09_right_5_12_13(self):
        self.assertEqual(classifyTriangle(5, 12, 13), "Right")

    def test_T10_not_triangle_1_2_3(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "NotATriangle")

    def test_T11_not_triangle_2_3_6(self):
        self.assertEqual(classifyTriangle(2, 3, 6), "NotATriangle")

    def test_T12_invalid_0_4_5(self):
        self.assertEqual(classifyTriangle(0, 4, 5), "InvalidInput")

    def test_T13_invalid_4_0_5(self):
        self.assertEqual(classifyTriangle(4, 0, 5), "InvalidInput")

    def test_T14_invalid_4_5_0(self):
        self.assertEqual(classifyTriangle(4, 5, 0), "InvalidInput")

    def test_T15_invalid_neg1_2_2(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), "InvalidInput")

    def test_T16_invalid_2_neg1_2(self):
        self.assertEqual(classifyTriangle(2, -1, 2), "InvalidInput")

    def test_T17_invalid_2_2_neg1(self):
        self.assertEqual(classifyTriangle(2, 2, -1), "InvalidInput")

    def test_T18_invalid_float(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), "InvalidInput")

    def test_T19_invalid_str(self):
    
        self.assertEqual(classifyTriangle("3", 4, 5), "InvalidInput")

    def test_T20_invalid_bool(self):
        self.assertEqual(classifyTriangle(True, 4, 5), "InvalidInput")

    def test_T21_invalid_201_10_10(self):
        self.assertEqual(classifyTriangle(201, 10, 10), "InvalidInput")

    def test_T22_invalid_10_201_10(self):
        self.assertEqual(classifyTriangle(10, 201, 10), "InvalidInput")

    def test_T23_invalid_10_10_201(self):
        self.assertEqual(classifyTriangle(10, 10, 201), "InvalidInput")


if __name__ == "__main__":
    unittest.main()
