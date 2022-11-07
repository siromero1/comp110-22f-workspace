"""Dictionary related utility functions."""

__author__ = "730576249"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all the values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table_data: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """New table with only certain rows of data."""
    col_table: dict[str, list[str]] = {}
    if row_num >= len(table_data):
        return table_data
    for key in table_data:
        col_value: list[str] = []
        for N in range(0, row_num):
            col_value.append(table_data[key][N])
        col_table[key] = col_value
    return col_table


def select(col_table: dict[str, list[str]], col_name: list[str]) -> dict[str, list[str]]:
    """Specific subset of original columns."""
    new_table: dict[str, list[str]] = {}
    for key in col_name:
        new_table[key] = col_table[key]
    return new_table


def concat(data_table_1: dict[str, list[str]], data_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two data tables."""
    result_dict: dict[str, list[str]] = {}
    for thing in data_table_1:
        result_dict[thing] = data_table_1[thing]
    for i in data_table_2:
        if i in result_dict:
            for item in range(len(data_table_2[i])):
                result_dict[i].append(data_table_2[i][item])
        else:
            result_dict[i] = data_table_2[i]
    return result_dict


def count(value_list: list[str]) -> dict[str, int]:
    """Counting the time a value appears in input list."""
    result: dict[str, int] = {}
    for key in value_list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result