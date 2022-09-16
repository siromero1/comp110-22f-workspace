"""EX04 - List - Ultility - Functions"""

__author__ = "730576249"

def all(list_ints: list[int], number: int) -> bool:
    i: int = 0
    while i < len(list_ints):
        if list_ints[i] == number:
            return True
    return False

def max(input: list[int]) -> int:
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
    if num_list == int_list:
        return True
    return False