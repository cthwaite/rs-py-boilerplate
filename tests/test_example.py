# coding: utf-8

from rs_py_boilerplate import core


def test_sum_as_string():
    '''Test the sum_as_string() function.
    '''
    assert core.sum_as_string(1, 1) == '2'
