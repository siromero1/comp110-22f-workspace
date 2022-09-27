"""EX05 - Tests for Functions."""

__author__ = "730576249"


from utils import only_evens, concat, sub


def test_only_evens() -> None:
    """Finding the even numbers in a list."""
    assert only_evens([]) == []


def test_only_evens_1() -> None:
    """Use case 1 - Even numbers in a list."""
    evens: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(evens) == [2, 4, 6, 8]


def test_only_evens_2() -> None:
    """Use case 2 - Even numbers in a list."""
    evens: list[int] = [2, 2, 2, 5]
    assert only_evens(evens) == [2, 2, 2]


def test_concat() -> None:
    """Two lists are being concatinated."""
    assert concat([], []) == []


def test_concat_1() -> None:
    """Use case 1 - Making a concatinated list."""
    concat_list_1: list[int] = [1, 2, 3, 4]
    concat_list_2: list[int] = [5, 6, 7, 8]
    assert concat_list_1 + concat_list_2 == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_2() -> None:
    """Use case 2 - Making a concatinated list."""
    concat_list1: list[int] = [10, 9, 8, 7, 6]
    concat_list2: list[int] = [5, 4, 3, 2, 1]
    assert concat_list1 + concat_list2 == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_sub() -> None:
    """Testing the sub function."""
    assert sub([]) == []


def test_sub_1() -> None:
    """Use case 1 - Testing the sub function."""


def test_sub_2() -> None:
    """Use case 2 - Testing the sub function."""