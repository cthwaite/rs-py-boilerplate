# coding: utf-8
'''
'''

try:
    from ._core import sum_as_string
except ImportError:
    from .pure import sum_as_string
