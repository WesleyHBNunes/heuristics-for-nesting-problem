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
        array_polygons[i] = Polygon.decide_best_position(array_polygons, i, x_lim, placed)
        placed[i] = True
    return Polygon.create_polygons_to_plot(array_polygons), calculate_function_objective(array_polygons)


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


def calculate_function_objective(array_polygons):
    fo = 0
    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > fo:
            fo = highest_y
    return fo
