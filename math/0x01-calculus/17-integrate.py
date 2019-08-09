#!/usr/bin/env python3
"""Implement poly_integral(poly, C=0) function"""


def poly_integral(poly, C=0):
    """
        Calculate the integral of a polynomial represented by a list of
        coefficients
        poly: list of integers
        C: int integral constant

        Return: list of integers, or None if poly or C is invalid
    """
    if not type(poly) is list or not (type(C) is int or type(C) is float):
        return None

    integral = [C]
    for i, coeff in enumerate(poly, 1):
        if coeff % i == 0:
            integral.append(coeff // i)
        else:
            integral.append(coeff / i)
    return integral
