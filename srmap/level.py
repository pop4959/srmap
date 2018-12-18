import struct
import gzip
from enum import Enum
from srmap.actor import Actor
from srmap.property import Property
from srmap.tilemap import Tilemap, Name, Size


class Theme(Enum):
    PROTOTYPE = 'StageVR'
    METRO = 'StageMetro'
    SS_ROYALE = 'StageShip'
    MANSION = 'StageMansion'
    PLAZA = 'StageCity'
    FACTORY = 'StageIndustry'
    THEME_PARK = 'StageThemePark'
    POWERPLANT = 'StagePowerplant'
    SILO = 'StageSilo'
    LIBRARY = 'StageUniversity'
    NIGHTCLUB = 'StageNightclub'
    ZOO = 'StageZoo'
    SWIFT_PEAKS = 'StageSki'
    CASINO = 'StageCasino'
    FESTIVAL = 'StageFestival'
    RESORT = 'StageResort'
    AIRPORT = 'StageAirport'


class Level:
    def __init__(self, version=6, actors=None, tilemaps=None, theme=Theme.PROTOTYPE, is_singleplayer=False,
                 bomb_timer=0, author='Unknown', name='Untitled', description='', workshop_id=0):
        self.version = version
        self.actors = [] if actors is None else actors
        self.tilemaps = [Tilemap(Name.BACKGROUND_0, Size.SMALL), Tilemap(Name.BACKGROUND_1, Size.SMALL),
                         Tilemap(Name.SHADING, Size.SMALL),
                         Tilemap(Name.COLLISION, Size.SMALL)] if tilemaps is None else tilemaps
        self.theme = theme.value if isinstance(theme, Theme) else theme
        self.is_singleplayer = is_singleplayer
        self.bomb_timer = bomb_timer
        self.author = author
        self.name = name
        self.description = description
        self.workshop_id = workshop_id

    def load(self, path):
        with gzip.open(path, 'rb') as f:
            self.version = struct.unpack('<i', f.read(4))[0]
            self.actors = []
            num_actors = struct.unpack('<i', f.read(4))[0]
            for a in range(num_actors):
                actor_position = struct.unpack('<ff', f.read(8))
                actor_size = struct.unpack('<ff', f.read(8))
                actor_type = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
                actor_properties = []
                actor_num_properties = struct.unpack('<i', f.read(4))[0]
                for p in range(actor_num_properties):
                    property_name = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
                    property_value = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
                    actor_properties.append(Property(property_name, property_value))
                self.actors.append(Actor(actor_position, actor_size, actor_type, actor_properties))
            self.tilemaps = []
            num_tilemaps = struct.unpack('<i', f.read(4))[0]
            for t in range(num_tilemaps):
                tilemap_name = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
                tilemap_size = struct.unpack('<ii', f.read(8))
                tilemap = []
                for y in range(tilemap_size[1]):
                    tilemap_row = []
                    for x in range(tilemap_size[0]):
                        tilemap_row.append(struct.unpack('<i', f.read(4))[0])
                    tilemap.append(tilemap_row)
                self.tilemaps.append(Tilemap(tilemap_name, tilemap_size, tilemap))
            self.theme = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
            self.is_singleplayer = False if struct.unpack('<b', f.read(1))[0] == 0 else True
            if self.is_singleplayer:
                self.bomb_timer = struct.unpack('<i', f.read(4))[0]
            self.author = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
            self.name = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
            self.description = f.read(struct.unpack('<b', f.read(1))[0]).decode('ascii')
            self.workshop_id = struct.unpack('<q', f.read(8))[0]

    def save(self, path):
        data = b''
        num_actors = len(self.actors)
        data += struct.pack('<ii', self.version, num_actors)
        for i in range(num_actors):
            actor = self.actors[i]
            num_properties = len(actor.properties)
            data += struct.pack('<ffffb{}si'.format(len(actor.type)), actor.position[0], actor.position[1],
                                actor.size[0], actor.size[1], len(actor.type), actor.type.encode('ascii'),
                                num_properties)
            for j in range(num_properties):
                property = actor.properties[j]
                data += struct.pack('<b{}sb{}s'.format(len(property.name), len(property.value)), len(property.name),
                                    property.name.encode('ascii'), len(property.value), property.value.encode('ascii'))
        num_tilemaps = len(self.tilemaps)
        data += struct.pack('<i', num_tilemaps)
        for i in range(num_tilemaps):
            t_data = b''
            tilemap = self.tilemaps[i]
            t_data += struct.pack('<b{}sii'.format(len(tilemap.name)), len(tilemap.name), tilemap.name.encode('ascii'),
                                  tilemap.width, tilemap.height)
            for y in range(tilemap.height):
                r_data = b''
                for x in range(tilemap.width):
                    r_data += struct.pack('<i', tilemap.tilemap[y][x])
                t_data += r_data
            data += t_data
        data += struct.pack('<b{}sb'.format(len(self.theme)), len(self.theme), self.theme.encode('ascii'),
                            self.is_singleplayer)
        if self.is_singleplayer:
            data += struct.pack('<i', self.bomb_timer)
        data += struct.pack('<b{}sb{}sb{}sq'.format(len(self.author), len(self.name), len(self.description)),
                            len(self.author), self.author.encode('ascii'), len(self.name), self.name.encode('ascii'),
                            len(self.description), self.description.encode('ascii'), self.workshop_id)
        with gzip.open(path, 'wb') as f:
            f.write(data)
