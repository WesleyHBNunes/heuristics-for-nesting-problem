import Heuristics
import Polygon
import Placements


def solve(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse)
    triangles_polygons = Polygon.triangulation_all_polygons(array_polygons)
    new_polygons = []
    placed = [False for _ in array_polygons]
    for i in range(len(array_polygons)):
        array_polygons[i] = Heuristics.rotate_polygon_heuristic(
            array_polygons[i], rotate_function, triangles_polygons[i])
        array_polygons[i] = Placements.placement_greedy(array_polygons, i, x_lim, placed, triangles_polygons)
        new_polygons.append(array_polygons[i])
        placed[i] = True

    return new_polygons, Heuristics.calculate_function_objective(array_polygons, placed)
