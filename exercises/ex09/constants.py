"""Constants used through the simulation."""

BOUNDS_WIDTH: int = 400
MAX_X: float = BOUNDS_WIDTH / 2
MIN_X: float = -MAX_X
VIEW_WIDTH: int = BOUNDS_WIDTH + 20

BOUNDS_HEIGHT: int = 400
MAX_Y: float = BOUNDS_HEIGHT / 2
MIN_Y: float = -MAX_Y
VIEW_HEIGHT: int = BOUNDS_HEIGHT + 20

CELL_RADIUS: int = 15
CELL_COUNT: int = 50
CELL_SPEED: float = 1.0

VULNERABLE: int = 0
INFECTED: int = 1
IMMUNE: int = -1

START_INFECTED: int = 3
START_IMMUNE: int = 3

RECOVERY_PERIOD: int = 90