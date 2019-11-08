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


def solution_bottom_left_greedy(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse)
    new_polygons = []
    placed = [False for _ in array_polygons]
    for i in range(len(array_polygons)):
        array_polygons[i] = Heuristics.rotate_polygon_heuristic(array_polygons[i], rotate_function)
        array_polygons[i] = Placements.placement_bottom_left_greedy(array_polygons, i, x_lim, placed)
        new_polygons.append(array_polygons[i])
        placed[i] = True
    return new_polygons, Heuristics.calculate_function_objective(new_polygons, placed)


# def solution_bottom_left_greedy(array_polygons, x_lim, sort_function, reverse):
#     array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
#     placed = [False for _ in range(len(array_polygons))]
#     for i in range(len(array_polygons)):
#         best_fo = 99999999999
#         original_polygon = array_polygons[i]
#         final_polygon = array_polygons[i]
#         for k in range(2):
#             for j in range(len(array_polygons[i])):
#                 placed[i] = False
#                 array_polygons[i] = original_polygon
#                 angle = Heuristics.rotate_new_heuristic(
#                                     (array_polygons[i][j][0], array_polygons[i][(j + 1) % len(array_polygons[i])][0]),
#                                     (array_polygons[i][j][1], array_polygons[i][(j + 1) % len(array_polygons[i])][1]))
#                 if k == 0:
#                     angle += 90
#                 array_polygons[i] = Polygon.rotate_polygon(array_polygons[i], angle)
#                 array_polygons[i] = Placements.placement_bottom_left_greedy(array_polygons, i, x_lim, placed)
#                 placed[i] = True
#                 current_fo = Heuristics.calculate_function_objective(array_polygons, placed)
#                 if current_fo < best_fo:
#                     final_polygon = array_polygons[i]
#                     best_fo = current_fo
#                 elif current_fo == best_fo:
#                     min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(array_polygons[i])
#                     min_x, max_x, min_y, max_y2 = Polygon.min_max_points_polygon(final_polygon)
#                     if max_y < max_y2:
#                         final_polygon = array_polygons[i]
#         array_polygons[i] = final_polygon
#     return array_polygons, Heuristics.calculate_function_objective(array_polygons, placed)
