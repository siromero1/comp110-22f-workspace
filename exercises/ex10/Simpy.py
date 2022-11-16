"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730576249"


class Simpy:
    """Initialize values attribute."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initalize values attribute to the argument."""
        self.values = values
    
    def __repr__(self) -> str:
        """Produce a string representation."""
        return f"Simpy({self.values})"
    
    def fill(self, insert_num: float, amount: int) -> None:
        """Fill Simpy's values with a specific number of values."""
        self.values = []
        for number in range(0, amount):
            self.values.append(insert_num)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill Simpy's values with a range of values in increments."""
        assert step != 0.0
        while start < stop:
            self.values.append(start)
            start += step
        while start > stop:
            self.values.append(start)
            start += step
    
    def sum(self) -> float:
        """The sum of values."""
        result: float
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding Simpy objects and/or floats."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                item += rhs
                result.values.append(item)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raising powers to floats and/or Simpy objects."""
        result: Simpy = Simpy([])
        idx: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(self.values[idx] ** rhs)
                idx += 1
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """True or False based on the equality of each item in Values."""
        result: list[bool] = []
        idx: int = 0
        if isinstance(rhs, Simpy):
            for item in self.values:
                if self.values[idx] == rhs.values[idx]:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        else:
            for items in self.values:
                if self.values[idx] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Which value is greater than?"""
        result: list[bool] = []
        idx: int = 0
        if isinstance(rhs, Simpy):
            for item in self.values:
                if self.values[idx] > rhs.values[idx]:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        else:
            for items in self.values:
                if self.values[idx] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                idx += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returning a specific item from Simpy object."""
        result: list[float] = []
        if isinstance(rhs, int):
            for item in self.values:
                result.append(rhs)
        else:
            for items in range(len(rhs)):
                if rhs[items] is True:
                    result.append(self.values[items])
        return f"Simpy({result})"