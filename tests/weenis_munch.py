


import pytest

from aitest.aiskel import fib, main

__author__ = "Max Busboom"
__copyright__ = "Max Busboom"
__license__ = "MIT"

def munch(v):

    if v == '10':
        assert False

    return int(v)

def test_munch():
    """ Test that srings can be converted to integers """
    assert munch("1") == 1
    assert munch("2") == 2
    assert munch("7") == 7

    with pytest.raises(AssertionError):
        munch("10")