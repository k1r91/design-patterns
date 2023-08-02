from typing import List
from map_site import MapSite
from direction import Direction


class Room(MapSite):

    def __init__(self, room_number: int):
        self._room_number: int = room_number
        self._sides: List[MapSite] = list()

    def get_side(self, direction: Direction) -> MapSite:
        pass

    def set_side(self, direction: Direction, site: MapSite) -> None:
        pass

    def enter(self):
        pass


class Wall(MapSite):

    def enter(self):
        pass


class Door(MapSite):

    def __init__(self, room_1: Room, room_2: Room):
        self.room_1 = room_1
        self.room_2 = room_2
        self.is_open = True

    def enter(self):
        pass


class Maze:
    """
    consists of a set of rooms
    """
    def __init__(self, rooms: dict[Room: bool]):
        self.rooms = rooms

    def add_room(self, room: Room):
        self.rooms.update({room: True})


class MazeGame:
    """
    create rooms and doors
    """
    pass