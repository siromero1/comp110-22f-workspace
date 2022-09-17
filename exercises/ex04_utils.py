"""EX04 - List - Ultility - Functions."""

__author__ = "730576249"


def all(list_ints: list[int], number: int) -> bool:
    """Finding an int in a list of ints."""
    i: int = 0
    match: bool = True 
    if len(list_ints) == 0:
        match = False
    while i <= len(list_ints) - 1 and match:
        if list_ints[i] == number:
            match = True
        else:
            match = False
        i += 1
    return match


def max(input: list[int]) -> int:
    """Returning the max number in a list."""
    i: int = 0
    max_number: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if max_number < input[i]:
            max_number = input[i]
        i = i + 1
    return max_number


def is_equal(num_list: int, int_list: int) -> bool:
    """Comparing two lists of ints."""
    if num_list == int_list:
        return True
    return False