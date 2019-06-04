from random import shuffle
import math
import Polygon

# CONST
LAMBDA = .00000000001


def solution(array_polygons, x_lim, function):
    new_polygons = []
    line_y = 0
    for i in range(len(array_polygons)):

        array_polygons[i] = rotate_polygon_heuristic(array_polygons[i], function)
        if i == 0:
            new_polygons.append(array_polygons[i])
            continue
        list_x, list_y = list(zip(*new_polygons[i - 1]))
        max_point_x = max(list_x)

        current_list_x, current_list_y = list(zip(*array_polygons[i]))
        current_list_x = list(current_list_x)
        if max(current_list_x) + max_point_x < x_lim:
            new_polygons.append(Polygon.add_number_axis_x_y(array_polygons[i], max_point_x + LAMBDA, line_y))
        else:
            line_y = return_line_y(new_polygons)
            new_polygons.append(Polygon.add_number_axis_x_y(array_polygons[i], 0, line_y))

    return Polygon.create_polygons_to_plot(new_polygons), return_line_y(new_polygons)


def better_solution(array_polygons, x_lim, function):
    new_polygons = []
    for i in range(len(array_polygons)):

        array_polygons[i] = rotate_polygon_heuristic(array_polygons[i], function)
        if i == 0:
            new_polygons.append(array_polygons[i])
            continue
        list_x, list_y = list(zip(*new_polygons[i - 1]))
        max_point_x = max(list_x)

        current_list_x, current_list_y = list(zip(*array_polygons[i]))

        if max(current_list_x) + max_point_x < x_lim:
            point_x = max_point_x + LAMBDA
        else:
            point_x = 0

        array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], point_x, 0)
        current_list_x, current_list_y = list(zip(*array_polygons[i]))
        current_list_x = list(current_list_x)
        current_max_point_x = max(current_list_x)
        current_min_point_x = min(current_list_x)

        highest_y_point = return_line_y(new_polygons)
        abstract_polygon = [(current_min_point_x, 0),
                            (current_max_point_x, 0),
                            (current_max_point_x, highest_y_point),
                            (current_min_point_x, highest_y_point)]
        polygons_to_analyze = []
        for polygon in new_polygons:
            if Polygon.is_overlapping(abstract_polygon, polygon):
                polygons_to_analyze.append(polygon)

        original_polygon = array_polygons[i]
        if polygon_overlapping(array_polygons[i], polygons_to_analyze):
            polygons_to_analyze = Polygon.sort(polygons_to_analyze, Polygon.minimum_y, False)
            for polygon_overlapped in polygons_to_analyze:
                list_x, list_y = list(zip(*polygon_overlapped))
                max_point_y = max(list_y)
                array_polygons[i] = original_polygon
                array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, max_point_y + LAMBDA)
                if not polygon_overlapping(array_polygons[i], polygons_to_analyze):
                    array_polygons[i] = original_polygon
                    array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, max_point_y + LAMBDA)
                    new_polygons.append(array_polygons[i])
                    break
        else:
            new_polygons.append(array_polygons[i])

    return Polygon.create_polygons_to_plot(new_polygons), return_line_y(new_polygons)


def random_solve(array_polygons, x_lim, function):
    shuffle(array_polygons)
    return function(array_polygons, x_lim)


def solve(array_polygons, x_lim, function, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    return function(array_polygons, x_lim, rotate_function)


def return_line_y(array_polygons):
    line_y = 0

    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > line_y:
            line_y = highest_y
    return line_y + LAMBDA


def polygon_overlapping(polygon, polygons_to_analyze):
    for p in polygons_to_analyze:
        if Polygon.is_overlapping(polygon, p):
            return True
    return False


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
    # print(angle)
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
