"""EX05 - List - Utility - Functions."""

__author__ = "730576249"


def only_evens(x: list[int]) -> list[int]:
    """Finding even numbers of a list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            even_list.append(x[i])
        i += 1
    return even_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatinating two lists together."""
    new_list: list[int] = xs + ys
    return new_list


def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Subset of a given list."""
    return