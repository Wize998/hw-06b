# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Classify a triangle by side lengths.
    Returns one of:
      "Equilateral", "Isosceles", "Scalene", "Right", "NotATriangle", "InvalidInput"
    Rules:
      - a, b, c must be integers (bools are NOT allowed) in the range 1..200
      - Triangle inequality: sum of any two sides > the third
      - Right triangle uses Pythagoras (order-independent)
    """

    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (a, b, c)):
        return "InvalidInput"
    if any(x <= 0 or x > 200 for x in (a, b, c)):
        return "InvalidInput"

    s = sorted((a, b, c))
    if s[0] + s[1] <= s[2]:
        return "NotATriangle"

    if a == b == c:
        return "Equilateral"

    if s[0] * s[0] + s[1] * s[1] == s[2] * s[2]:
        return "Right"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"
