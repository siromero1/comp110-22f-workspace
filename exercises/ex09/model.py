"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = "730576249"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other_point: Point) -> float:
        """Finding the distance between two points."""
        from math import sqrt
        dist: float = sqrt(((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2))
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_infected() is True:
            return "red"
        if self.is_immune() is True:
            return "pink"
    
    def contract_disease(self) -> None:
        """Representing sickness."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Is the cell vulnerable?"""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Is the cell infected?"""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, other_cell: Cell) -> None:
        """Two Cell objects make contact."""
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()
        if other_cell.is_infected() and self.is_vulnerable():
            self.contract_disease()
    
    def immunize(self) -> None:
        """Making the cell immune."""
        self.sickness = constants.IMMUNE
    
    def is_immmune(self) -> bool:
        """Checking if cell is immune."""
        if self.sickness is constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infection_num: int, immune_num: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if (infection_num >= cells) or infection_num <= 0:
            raise ValueError("Some number of Cell objects must be infected.")
        if (immune_num >= cells) or (immune_num >= infection_num):
            raise ValueError("Improper number of immmune or infected cells.")
        for _ in range(0, cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(0, infection_num):
            self.population[i].contract_disease()

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checking if two cells came into contact."""
        for cell in range(len(self.population)):
            for cell_2 in range(cell + 1, len(self.population)):
                first_cell: Cell = self.population[cell]
                second_cell: Cell = self.population[cell_2]
                if first_cell.location.distance(second_cell.location) < constants.CELL_RADIUS:
                    first_cell.contact_with(second_cell)
    
    def is_complete(self) -> bool:
        """Running simulation through completion."""
        for cell in self.population:
            if cell.is_infected() is True:
                return False
            if cell.is_vulnerable() is True:
                return True
            if cell.is_immune() is True:
                return True