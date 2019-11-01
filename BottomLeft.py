from random import shuffle
import Heuristics
import Polygon
import Placements


def solution_slide(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse)
    new_polygons = []
    placed = [False for _ in array_polygons]
    for i in range(len(array_polygons)):
        array_polygons[i] = Heuristics.rotate_polygon_heuristic(array_polygons[i], rotate_function)
        array_polygons[i] = Placements.placement_bottom_left_slide(array_polygons, i, x_lim, placed)
        new_polygons.append(array_polygons[i])
        placed[i] = True
    return new_polygons, Heuristics.calculate_function_objective(new_polygons, placed)


def solution(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse)
    new_polygons = []
    for i in range(len(array_polygons)):
        array_polygons[i] = Heuristics.rotate_polygon_heuristic(array_polygons[i], rotate_function)
        array_polygons[i] = Placements.placement_bottom_left(array_polygons, i, x_lim, new_polygons)
        new_polygons.append(array_polygons[i])
    return new_polygons, Heuristics.return_line_y(new_polygons)


def random_solve(array_polygons, x_lim, function):
    shuffle(array_polygons)
    return function(array_polygons, x_lim)
