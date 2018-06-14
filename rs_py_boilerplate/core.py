# coding: utf-8
'''
'''

try:
    from ._core import sum_as_string
except ImportError:
    import warnings
    warnings.warn('Falling back on pure Python `sum_as_string`', RuntimeWarning)

    from .pure import sum_as_string
