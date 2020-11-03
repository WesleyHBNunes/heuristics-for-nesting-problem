import Heuristics
import Polygon
import copy
import Placements
import random


def solution_random(array_polygons, x_lim, sort_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    triangles_polygons = Polygon.triangulation_all_polygons(array_polygons)
    placed = [False for _ in range(len(array_polygons))]
    for i in range(len(array_polygons)):
        best_fo = 99999999999
        original_polygon = array_polygons[i]
        original_triangle = copy.deepcopy(triangles_polygons[i])
        # original_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
        final_polygon = array_polygons[i]
        final_triangle = copy.deepcopy(triangles_polygons[i])
        # final_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
        for k in range(2):
            for j in range(len(array_polygons[i])):
                placed[i] = False
                array_polygons[i] = original_polygon
                triangles_polygons[i] = copy.deepcopy(original_triangle)
                # triangles_polygons[i] = cPickle.loads(cPickle.dumps(original_triangle))
                angle = Heuristics.rotate_new_heuristic(
                    (array_polygons[i][j][0], array_polygons[i][(j + 1) % len(array_polygons[i])][0]),
                    (array_polygons[i][j][1], array_polygons[i][(j + 1) % len(array_polygons[i])][1]))
                if k == 0:
                    angle += 90
                array_polygons[i] = Polygon.rotate_polygon(array_polygons[i], angle, triangles_polygons[i])
                x = random.randint(0, 1)
                if x == 0:
                    array_polygons[i] = Placements.placement_bottom_left_greedy(
                        array_polygons, i, x_lim, placed, triangles_polygons)
                elif x == 1:
                    array_polygons[i] = Placements.placement_vertex(
                        array_polygons, i, x_lim, placed, triangles_polygons)
                placed[i] = True
                current_fo = Heuristics.calculate_function_objective(array_polygons, placed)
                if current_fo < best_fo:
                    final_polygon = array_polygons[i]
                    final_triangle = copy.deepcopy(triangles_polygons[i])
                    # final_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
                    best_fo = current_fo
                elif current_fo == best_fo:
                    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(array_polygons[i])
                    min_x, max_x, min_y, max_y2 = Polygon.min_max_points_polygon(final_polygon)
                    if max_y < max_y2:
                        final_polygon = array_polygons[i]
                        final_triangle = copy.deepcopy(triangles_polygons[i])
                        # final_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
        array_polygons[i] = final_polygon
        triangles_polygons[i] = copy.deepcopy(final_triangle)
        # triangles_polygons[i] = cPickle.loads(cPickle.dumps(final_triangle))
    return array_polygons, Heuristics.calculate_function_objective(array_polygons, placed)


def solution(array_polygons, x_lim, sort_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    triangles_polygons = Polygon.triangulation_all_polygons(array_polygons)
    placed = [False for _ in range(len(array_polygons))]
    for i in range(len(array_polygons)):
        best_fo = 99999999999
        original_polygon = array_polygons[i]
        original_triangle = copy.deepcopy(triangles_polygons[i])
        # original_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
        final_polygon = array_polygons[i]
        final_triangle = copy.deepcopy(triangles_polygons[i])
        # final_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
        for k in range(2):
            for j in range(len(array_polygons[i])):
                for x in range(2):
                    placed[i] = False
                    array_polygons[i] = original_polygon
                    triangles_polygons[i] = copy.deepcopy(original_triangle)
                    # triangles_polygons[i] = cPickle.loads(cPickle.dumps(original_triangle))
                    angle = Heuristics.rotate_new_heuristic(
                                        (array_polygons[i][j][0], array_polygons[i][(j + 1) % len(array_polygons[i])][0]),
                                        (array_polygons[i][j][1], array_polygons[i][(j + 1) % len(array_polygons[i])][1]))
                    if k == 0:
                        angle += 90
                    array_polygons[i] = Polygon.rotate_polygon(array_polygons[i], angle, triangles_polygons[i])
                    if x == 0:
                        array_polygons[i] = Placements.placement_bottom_left_greedy(
                            array_polygons, i, x_lim, placed, triangles_polygons)
                    else:
                        array_polygons[i] = Placements.placement_vertex(
                            array_polygons, i, x_lim, placed, triangles_polygons)
                    placed[i] = True
                    current_fo = Heuristics.calculate_function_objective(array_polygons, placed)
                    if current_fo < best_fo:
                        final_polygon = array_polygons[i]
                        final_triangle = copy.deepcopy(triangles_polygons[i])
                        # final_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
                        best_fo = current_fo
                    elif current_fo == best_fo:
                        min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(array_polygons[i])
                        min_x, max_x, min_y, max_y2 = Polygon.min_max_points_polygon(final_polygon)
                        if max_y < max_y2:
                            final_polygon = array_polygons[i]
                            final_triangle = copy.deepcopy(triangles_polygons[i])
                            # final_triangle = cPickle.loads(cPickle.dumps(triangles_polygons[i]))
        array_polygons[i] = final_polygon
        triangles_polygons[i] = copy.deepcopy(final_triangle)
        # triangles_polygons[i] = cPickle.loads(cPickle.dumps(final_triangle))
    return array_polygons, Heuristics.calculate_function_objective(array_polygons, placed)
