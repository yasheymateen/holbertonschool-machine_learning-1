#!/usr/bin/env python3
"""Implement np_cat(mat1, mat2, axis=0) function"""


def np_cat(mat1, mat2, axis=0):
    """
        Concatenate two matrices along a specific axis
        mat1: numpy.ndarray
        mat2: numpy.ndarray
        axis: axis along which to join arrays

        Return: new numpy.ndarray
    """
    import numpy as np
    return np.concatenate((mat1[:], mat2[:]), axis=axis)
