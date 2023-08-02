from enum import Enum


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


if __name__ == '__main__':
    west = Direction.WEST
    print(west in Direction)