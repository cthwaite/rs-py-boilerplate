# coding: utf-8
'''Pure-python fallback implementation.
'''

import warnings

# warn users when the pure-python implementation is imported.
warnings.warn('Using pure-python implementation of rs_py_boilerplate.core',
              RuntimeWarning)


def sum_as_string(a, b):
    '''Sum two integers and return the result as a string.

    Args:
        a (int)
        b (int)

    Returns:
        str
    '''
    return '{}'.format(a + b)
