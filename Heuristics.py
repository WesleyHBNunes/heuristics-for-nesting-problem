import math
import Heuristic_Multiples_Placements
import Bottom_Left
import Greedy
import New_Heuristic
import Polygon
import copy
import time


def solve_with_bottom_left(array_polygons, x_lim, sort_function, rotate_function, reverse):
    return Bottom_Left.solution(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        rotate_function=rotate_function,
        reverse=reverse)


def solve_with_bottom_left_slide(array_polygons, x_lim, sort_function, rotate_function, reverse):
    return Bottom_Left.solution_slide(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        rotate_function=rotate_function,
        reverse=reverse)


def solve_with_bottom_left_greedy(array_polygons, x_lim, sort_function, reverse):
    return Bottom_Left.solution_bottom_left_greedy(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        reverse=reverse)


def solve_with_greedy(array_polygons, x_lim, sort_function, rotate_function, reverse):
    return Greedy.solve(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        rotate_function=rotate_function,
        reverse=reverse)


def solve_with_new_heuristic_modified(array_polygons, x_lim, sort_function, reverse):
    return New_Heuristic.solve_modified(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        reverse=reverse)


def solve_with_new_heuristic(array_polygons, x_lim, sort_function, rotate_function, reverse):
    return New_Heuristic.solve(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        rotate_function=rotate_function,
        reverse=reverse)


def solve_with_heuristic_multiples_placements(array_polygons, x_lim, sort_function, reverse):
    return Heuristic_Multiples_Placements.solution(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        reverse=reverse)


def solve_with_heuristic_multiples_placements_random(array_polygons, x_lim, sort_function, reverse, iteration):
    begin = time.time()
    best_results = 99999
    best_polygons = []
    for i in range(iteration):
        polygons, limit_y = Heuristic_Multiples_Placements.solution(
            array_polygons=array_polygons,
            x_lim=x_lim,
            sort_function=sort_function,
            reverse=reverse)
        if limit_y < best_results:
            best_polygons = polygons
            best_results = limit_y
        if time.time() - begin >= 3600:
            return best_polygons, best_results
    return best_polygons, best_results


def heuristic_highest_side(polygon_original):
    polygon = copy.deepcopy(polygon_original)
    points_x, points_y = Polygon.highest_side(polygon)
    if points_x[0] - points_x[1] > points_y[0] - points_y[1]:
        if points_y[0] - points_y[1] == 0:
            angle = 90
        else:
            angle = math.degrees(math.atan((points_x[0] - points_x[1]) / (points_y[0] - points_y[1])))
    else:
        if points_x[0] - points_x[1] == 0:
            angle = 0
        else:
            angle = 270 + math.degrees(math.atan((points_y[0] - points_y[1]) / (points_x[0] - points_x[1])))
    polygon_rotated = Polygon.rotate_polygon_no_tri(polygon, angle)
    angle2 = heuristic_highest_axis(polygon)
    polygon = Polygon.rotate_polygon_no_tri(polygon, angle2)
    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(polygon)
    r_min_x, r_max_x, r_min_y, r_max_y = Polygon.min_max_points_polygon(polygon_rotated)
    if r_max_x - r_min_x > max_x - min_x:
        return angle2
    return angle


def rotate_new_heuristic(points_x, points_y):
    if points_x[0] - points_x[1] > points_y[0] - points_y[1]:
        if points_y[0] - points_y[1] == 0:
            angle = 90
        else:
            angle = math.degrees(math.atan((points_x[0] - points_x[1]) / (points_y[0] - points_y[1])))
    else:
        if points_x[0] - points_x[1] == 0:
            angle = 0
        else:
            angle = 270 + math.degrees(math.atan((points_y[0] - points_y[1]) / (points_x[0] - points_x[1])))
    return angle


def heuristic_highest_axis(polygon):
    width, height = Polygon.width_height(polygon)
    if height <= width:
        return 90
    return 0


def rotate_polygon_heuristic(polygon, function, triangle):
    return Polygon.rotate_polygon(polygon, function(polygon), triangle)


def calculate_function_objective(array_polygons, placed):
    objective_function = 0
    for i in range(len(array_polygons)):
        if placed[i]:
            list_x, list_y = zip(*array_polygons[i])
            highest_y = max(list_y)
            if max(list_y) > objective_function:
                objective_function = highest_y
    return objective_function


def return_line_y(array_polygons):
    line_y = 0

    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > line_y:
            line_y = highest_y
    return line_y


def decide_best_position(polygons, index, limit_x, placed, triangles):
    ifp = []
    for i in range(len(polygons)):
        if not placed[i]:
            break
        if index != i:
            ifp += Polygon.calculate_ifp_between_two_polygons(polygons, i, index, placed, limit_x, triangles)
    best_point = Polygon.return_best_point_in_ifp(ifp)
    if best_point == ():
        point_y = calculate_function_objective(polygons, placed)
        return Polygon.add_number_axis_x_y(polygons[index], 0, point_y, triangles[index])
    return Polygon.move_polygon_by_reference_point(
        best_point[0], polygons[index], (best_point[1], best_point[2]), triangles[index])


def slide_polygon(array_polygon, polygons_placed, i, limit_x, triangles_polygons):
    placed = False
    if limit_x > 1000:
        jump = 1
    else:
        jump = .1
    while not placed:
        array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], 0, .00001, triangles_polygons[i])
        moved_below, array_polygon[i] = slide_polygon_below(array_polygon, polygons_placed, i, jump, triangles_polygons)
        moved_left, array_polygon[i] = slide_polygon_left(array_polygon, polygons_placed, i, jump, triangles_polygons)
        # moved_left, array_polygon[i] = slide_polygon_right(array_polygon, polygons_placed, i, x_lim)
        if not moved_below and not moved_left:
            placed = True
    return array_polygon[i]


def slide_polygon_below(array_polygon, polygons_placed, i, jump, triangles_polygons):
    placed = False
    count = 0
    while not placed:
        array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], 0, -jump, triangles_polygons[i])
        overlapping = False
        for j in range(len(array_polygon)):
            if i != j and polygons_placed[j]:
                if Polygon.is_overlapping(triangles_polygons[i], triangles_polygons[j]):
                    overlapping = True
        if overlapping or Polygon.negative_point(array_polygon[i]):
            array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], 0, jump, triangles_polygons[i])
            placed = True
        else:
            count += 1
    if count > 0:
        return True, array_polygon[i]
    return False, array_polygon[i]


def slide_polygon_left(array_polygon, polygons_placed, i, jump, triangles_polygons):
    placed = False
    count = 0
    while not placed:
        array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], -jump, 0, triangles_polygons[i])
        overlapping = False
        for j in range(len(array_polygon)):
            if i != j and polygons_placed[j]:
                if Polygon.is_overlapping(triangles_polygons[i], triangles_polygons[j]):
                    overlapping = True
        if overlapping or Polygon.negative_point(array_polygon[i]):
            array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], jump, 0, triangles_polygons[i])
            placed = True
        else:
            count += 1
    if count > 0:
        return True, array_polygon[i]
    return False, array_polygon[i]


# def slide_polygon_right(array_polygon, polygons_placed, i, x_lim):
#     placed = False
#     count = 0
#     while not placed:
#         array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], 0.1, 0)
#         overlapping = False
#         for j in range(len(array_polygon)):
#             if i != j and polygons_placed[j]:
#                 if Polygon.is_overlapping(array_polygon[i], array_polygon[j]):
#                     overlapping = True
#         min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(array_polygon[i])
#         if overlapping or max_x > x_lim:
#             array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], -0.1, 0)
#             placed = True
#         else:
#             count += 1
#     if count > 0:
#         return True, array_polygon[i]
#     return False, array_polygon[i]
