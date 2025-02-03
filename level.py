import pytmx
from settings import MAPS_DIR
from functions import scroll


class Map:
    def __init__(self, filename, free_tile, finish_tile):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{filename}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tile
        self.finish_tile = finish_tile

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size - scroll[0], y * self.tile_size - scroll[1]))

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def is_free(self, position):
        try:
            return self.get_tile_id(position) in self.free_tiles
        except ValueError:
            return 2
