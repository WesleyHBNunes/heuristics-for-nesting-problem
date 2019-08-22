import BottomLeft
import math
import Polygon


def solve_with_bottom_left(array_polygons, x_lim, sort_function, rotate_function, reverse):
    return BottomLeft.solve(
        array_polygons=array_polygons,
        x_lim=x_lim,
        sort_function=sort_function,
        rotate_function=rotate_function,
        reverse=reverse)


def solve_with_new_heuristic(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    placed = [False for _ in range(len(array_polygons))]
    for i in range(len(array_polygons)):
        array_polygons[i] = rotate_polygon_heuristic(array_polygons[i], rotate_function)
        array_polygons[i] = decide_best_position(array_polygons, i, x_lim, placed)
        array_polygons[i] = slide_polygon(array_polygons, placed, i)
        placed[i] = True
    return array_polygons, calculate_function_objective(array_polygons, placed)


def heuristic_highest_side(polygon):
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
    polygon_rotated = Polygon.rotate_polygon(polygon, angle)
    angle2 = heuristic_highest_axis(polygon)
    polygon = Polygon.rotate_polygon(polygon, angle2)
    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(polygon)
    r_min_x, r_max_x, r_min_y, r_max_y = Polygon.min_max_points_polygon(polygon_rotated)
    if r_max_x - r_min_x > max_x - min_x:
        return angle2
    return angle


def heuristic_highest_axis(polygon):
    width, height = Polygon.width_height(polygon)
    if height <= width:
        return 90
    return 0


def rotate_polygon_heuristic(polygon, function):
    return Polygon.rotate_polygon(polygon, function(polygon))


def calculate_function_objective(array_polygons, placed):
    of = 0
    for i in range(len(array_polygons)):
        if placed[i]:
            list_x, list_y = zip(*array_polygons[i])
            highest_y = max(list_y)
            if max(list_y) > of:
                of = highest_y
    return of


def return_line_y(array_polygons):
    line_y = 0

    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > line_y:
            line_y = highest_y
    return line_y


def decide_best_position(polygons, index, limit_x, placed):
    best_points = []
    for i in range(len(polygons)):
        if index != i and placed[i]:
            ifp = Polygon.return_real_ifp_between_two_polygons(polygons, i, index, placed)
            for p in ifp:
                aux = Polygon.move_polygon_by_reference_point(p[0], polygons[index], (p[1], p[2]))
                list_points_x, list_points_y = zip(*aux)
                if not max(list_points_x) > limit_x:
                    best_points.append(p)
    best_point = Polygon.return_best_point_in_ifp(best_points)
    if best_point == ():
        aux_polygon = []
        for i in range(len(polygons)):
            if placed[i]:
                aux_polygon.append(polygons[i])
        point_y = return_line_y(aux_polygon)
        return Polygon.add_number_axis_x_y(polygons[index], 0, point_y)
    return Polygon.move_polygon_by_reference_point(best_point[0], polygons[index], (best_point[1], best_point[2]))


def slide_polygon(array_polygon, polygons_placed, i):
    placed = False
    while not placed:
        array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], 0, -0.1)
        overlapping = False
        for j in range(len(array_polygon)):
            if i != j and polygons_placed[j]:
                if Polygon.is_overlapping(array_polygon[i], array_polygon[j]):
                    overlapping = True
        if overlapping or Polygon.negative_point(array_polygon[i]):
            array_polygon[i] = Polygon.add_number_axis_x_y(array_polygon[i], 0, 0.1)
            placed = True
    return array_polygon[i]


