from random import shuffle

import numpy as np

import Polygon

# CONST
LAMBDA = 0.00000000001


def sequential_solution(array_polygons):
    new_polygons = []
    for i in range(len(array_polygons)):
        if i == 0:
            new_polygons.append(array_polygons[i])
            continue

        list_x, list_y = list(zip(*new_polygons[i - 1]))
        max_point_x = max(list_x)
        new_polygons.append(Polygon.add_number_axis_x_y(array_polygons[i], max_point_x, 0))
    new_polygons_object = []

    for polygon in new_polygons:
        new_polygons_object.append(Polygon.create_polygon(np.array(polygon)))

    return new_polygons_object


def solution(array_polygons, x_lim):
    new_polygons = []
    line_y = 0
    for i in range(len(array_polygons)):
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


def better_solution(array_polygons, x_lim):
    new_polygons = []
    for i in range(len(array_polygons)):
        if i == 0:
            new_polygons.append(array_polygons[i])
            continue
        list_x, list_y = list(zip(*new_polygons[i - 1]))
        max_point_x = max(list_x)

        current_list_x, current_list_y = list(zip(*array_polygons[i]))
        current_list_x = list(current_list_x)

        if max(current_list_x) + max_point_x < x_lim:
            point_x = max_point_x + LAMBDA
        else:
            point_x = 0

        array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], point_x, 0)
        current_max_point_x = max(current_list_x)
        current_min_point_x = min(current_list_x)
        point_y = 0
        if i == 4:
            print('a')
        for polygon in new_polygons:
            list_x_polygon, list_y_polygon = list(zip(*polygon))
            max_x_polygon = max(list_x_polygon)
            min_x_polygon = min(list_x_polygon)
            max_y_polygon = max(list_y_polygon)
            if (current_min_point_x <= min_x_polygon <= max_x_polygon <= current_max_point_x) or (
                    min_x_polygon <= current_min_point_x <= current_max_point_x <= max_x_polygon) or (
                    min_x_polygon <= current_min_point_x <= max_x_polygon <= current_max_point_x) or (
                    current_min_point_x <= min_x_polygon <= current_max_point_x <= max_x_polygon):
                if max_x_polygon > point_y:
                    point_y = max_y_polygon + LAMBDA

        new_polygons.append(Polygon.add_number_axis_x_y(array_polygons[i], 0, point_y))
    return Polygon.create_polygons_to_plot(new_polygons), return_line_y(new_polygons)


def better_solution2(array_polygons, x_lim):
    new_polygons = []
    for i in range(len(array_polygons)):
        if i == 0:
            new_polygons.append(array_polygons[i])
            continue
        list_x, list_y = list(zip(*new_polygons[i - 1]))
        max_point_x = max(list_x)

        current_list_x, current_list_y = list(zip(*array_polygons[i]))
        current_list_x = list(current_list_x)

        if max(current_list_x) + max_point_x < x_lim:
            point_x = max_point_x + LAMBDA
        else:
            point_x = 0

        array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], point_x, 0)
        highest_y_point = return_line_y(new_polygons)
        new_list_y = []
        for number in current_list_y:
            new_list_y.append(number + highest_y_point)

        polygons_to_analyze = []
        for polygons in new_polygons:
            if Polygon.is_overlapping(array_polygons[i], polygons):
                polygons_to_analyze.append(polygons)

        point_y = return_line_y(polygons_to_analyze)
        array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, point_y)
        new_polygons.append(array_polygons[i])

    return Polygon.create_polygons_to_plot(new_polygons), return_line_y(new_polygons)


def random_solution(array_polygons, x_lim, function):
    shuffle(array_polygons)
    return function(array_polygons, x_lim)


def sorted_by_area_solution(array_polygons, x_lim, function):
    array_polygons = Polygon.sort(array_polygons, Polygon.area_polygon)
    return function(array_polygons, x_lim)


def sorted_by_ray_solution(array_polygons, x_lim, function):
    array_polygons = Polygon.sort(array_polygons, Polygon.ray_polygon)
    return function(array_polygons, x_lim)


def sorted_by_rectangle_of_polygon(array_polygons, x_lim, function):
    array_polygons = Polygon.sort(array_polygons, Polygon.rectangle_polygon_area)
    return function(array_polygons, x_lim)


def sorted_by_area_no_used_of_polygon(array_polygons, x_lim, function):
    array_polygons = Polygon.sort(array_polygons, Polygon.area_no_used_of_polygon)
    return function(array_polygons, x_lim)


def return_line_y(array_polygons):
    line_y = 0

    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > line_y:
            line_y = highest_y
    return line_y + LAMBDA
