from enum import Enum


class Name(Enum):
    BACKGROUND_0 = 'Background 0'
    BACKGROUND_1 = 'Background 1'
    SHADING = 'Shading'
    COLLISION = 'Collision'


class Size(Enum):
    SMALL = (600, 300)
    MEDIUM = (800, 400)
    LARGE = (1000, 500)


class Tilemap:
    def __init__(self, name=Name.COLLISION, size=Size.SMALL, tilemap=None):
        self.name = name.value if isinstance(name, Name) else name
        self.width = size.value[0] if isinstance(size, Size) else size[0]
        self.height = size.value[1] if isinstance(size, Size) else size[1]
        self.tilemap = [[0]*self.width]*self.height if tilemap is None else tilemap

    def __getitem__(self, p):
        return self.tilemap[p[1]][p[0]]

    def __setitem__(self, p, value):
        self.tilemap[p[1]][p[0]] = value
