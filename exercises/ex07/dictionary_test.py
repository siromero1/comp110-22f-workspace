"""Ex07 - Dictionary Test."""

__author__ = "730576249"


from dictionary import invert
import pytest


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)