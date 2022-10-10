"""Ex07 - Dictionary Test."""

__author__ = "730576249"


from dictionary import invert, count
import pytest


def test_invert() -> None:
    """Inverting keys and values."""
    assert invert({}) == {}


def test_invert_1() -> None:
    """Use case 1 - Inverting keys and values."""
    example_1: dict[str, str] = {'birthday': 'party', 'summer': 'time'}
    assert invert(example_1) == {'party': 'birthday', 'time': 'summer'}


def test_invert_2() -> None:
    """Use case 2 - Inverting keys and values."""
    example_2: dict[str, str] = {'apple': 'cat', 'orange': 'dog'}
    assert invert(example_2) == {'cat': 'apple', 'dog': 'orange'}


def test_count() -> None:
    """Counting frequency."""
    assert count([]) == {}


def test_count_1() -> None:
    """Use case 1 - Counting frequency."""
    list_1: list[str] = ['a', 'a', 'b', 'c']
    assert count(list_1) == {'a': 2, 'b': 1, 'c': 1}


def test_count_2() -> None:
    """Use case 2 - Counting frequency."""
    list_2: list[str] = ['pasta', 'sushi', 'pasta', 'pizza']
    assert count(list_2) == {'pasta': 2, 'sushi': 1, 'pizza': 1}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)