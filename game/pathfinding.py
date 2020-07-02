from position import Position
from config import *


def calculate_neighbours(tile, map_tiles):
    neighbours = []
    if 0 <= tile.position.x - 1:
        if (map_tiles[tile.position.x - 1][tile.position.y].typeTyle != WALL) and(
                map_tiles[tile.position.x - 1][tile.position.y].typeTyle != TOWER):
            neighbours.append(map_tiles[tile.position.x - 1][tile.position.y])
    if tile.position.x + 1 < FIELD_SIZE:
        if (map_tiles[tile.position.x + 1][tile.position.y].typeTyle != WALL) and (
                map_tiles[tile.position.x - 1][tile.position.y].typeTyle != TOWER):
            neighbours.append(map_tiles[tile.position.x + 1][tile.position.y])
    if 0 <= tile.position.y - 1:
        if (map_tiles[tile.position.x][tile.position.y - 1].typeTyle != WALL) and (
                map_tiles[tile.position.x][tile.position.y - 1].typeTyle != TOWER):
            neighbours.append(map_tiles[tile.position.x][tile.position.y - 1])
    if tile.position.y + 1 < FIELD_SIZE:
        if (map_tiles[tile.position.x][tile.position.y + 1].typeTyle != WALL) and (
                map_tiles[tile.position.x][tile.position.y + 1].typeTyle != TOWER):
            neighbours.append(map_tiles[tile.position.x][tile.position.y + 1])
    return neighbours


def calculate_estimated_distance_to_end(map):
    end = Position(FIELD_SIZE - 1, FIELD_SIZE - 1)
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            map[x][y].estimated_distance_to_end = (end.x - x) + (end.y - y)


def get_path(start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = current.parent
    path.append(start)
    path.reverse()
    return path


def sort_by_estimate(tile):
    return tile.estimated_distance_to_end


def find_path(map_tiles, start):
    calculate_estimated_distance_to_end(map_tiles)
    end = map_tiles[FIELD_SIZE - 1][FIELD_SIZE - 1]

    open = {start}
    closed = set()

    while len(open) > 0:
        current = min(open, key=sort_by_estimate)
        if current == end:
            return get_path(start, end)
        open.remove(current)
        closed.add(current)
        neighbours = calculate_neighbours(current, map_tiles)
        for neighbour in neighbours:
            if neighbour in closed or neighbour in open:
                continue
            neighbour.estimated_distance_to_end += current.estimated_distance_to_end
            neighbour.parent = current
            open.add(neighbour)

