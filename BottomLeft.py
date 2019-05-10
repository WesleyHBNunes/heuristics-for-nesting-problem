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


def random_solution(array_polygons, x_lim):
    shuffle(array_polygons)
    return solution(array_polygons, x_lim)


def sorted_by_area_solution(array_polygons, x_lim):
    array_polygons = Polygon.sort_by_area(array_polygons)
    return solution(array_polygons, x_lim)


def return_line_y(array_polygons):
    line_y = 0

    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > line_y:
            line_y = highest_y
    return line_y + LAMBDA
