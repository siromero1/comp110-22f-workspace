"""EX07 - Dictionary - Functions."""

__author__ = "730576249"


def main() -> None:
    """Main function."""
    print(favorite_color)


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values."""
    flip: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in flip:
            raise KeyError("Error.")
        flip[dict_1[key]] = key
    return flip


def count(value_list: list[str]) -> dict[str, int]:
    """Counting the time a value appears in input list."""
    result: dict[str, int] = {}
    for key in value_list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Finding the most common favorite color."""