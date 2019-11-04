import Heuristics
import Polygon
import Placements


def solve_modified(array_polygons, x_lim, sort_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    placed = [False for _ in range(len(array_polygons))]
    for i in range(len(array_polygons)):
        best_fo = 99999999999
        original_polygon = array_polygons[i]
        final_polygon = array_polygons[i]
        for k in range(2):
            for j in range(len(array_polygons[i])):
                placed[i] = False
                array_polygons[i] = original_polygon
                angle = Heuristics.rotate_new_heuristic(
                                    (array_polygons[i][j][0], array_polygons[i][(j + 1) % len(array_polygons[i])][0]),
                                    (array_polygons[i][j][1], array_polygons[i][(j + 1) % len(array_polygons[i])][1]))
                if k == 0:
                    angle += 90
                array_polygons[i] = Polygon.rotate_polygon(array_polygons[i], angle)
                array_polygons[i] = Placements.placement_vertex(array_polygons, i, x_lim, placed)
                placed[i] = True
                current_fo = Heuristics.calculate_function_objective(array_polygons, placed)
                if current_fo < best_fo:
                    final_polygon = array_polygons[i]
                    best_fo = current_fo
                elif current_fo == best_fo:
                    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(array_polygons[i])
                    min_x, max_x, min_y, max_y2 = Polygon.min_max_points_polygon(final_polygon)
                    if max_y < max_y2:
                        final_polygon = array_polygons[i]
        array_polygons[i] = final_polygon
    return array_polygons, Heuristics.calculate_function_objective(array_polygons, placed)


def solve(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    placed = [False for _ in range(len(array_polygons))]
    for i in range(len(array_polygons)):
        array_polygons[i] = Heuristics.rotate_polygon_heuristic(array_polygons[i], rotate_function)
        array_polygons[i] = Placements.placement_vertex(array_polygons, i, x_lim, placed)
        placed[i] = True
    return array_polygons, Heuristics.calculate_function_objective(array_polygons, placed)