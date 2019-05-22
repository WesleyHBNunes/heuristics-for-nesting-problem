from random import shuffle

import Polygon

# CONST
LAMBDA = 0.00000000001


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

        width, height = Polygon.width_height(array_polygons[i])
        if height <= width:
            array_polygons[i] = Polygon.rotate_polygon(array_polygons[i], 90)

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
        current_max_point_y = max(current_list_y)
        current_min_point_y = min(current_list_y)

        highest_y_point = return_line_y(new_polygons)
        abstract_polygon = [(current_min_point_x, 0),
                            (current_max_point_x, 0),
                            (current_max_point_x, highest_y_point),
                            (current_min_point_x, highest_y_point)]
        polygons_to_analyze = []
        for polygon in new_polygons:
            if Polygon.is_overlapping(abstract_polygon, polygon):
                polygons_to_analyze.append(polygon)

        polygons_to_analyze = sort_polygons_to_analyze(polygons_to_analyze)
        placed = False

        for j in range(1, len(polygons_to_analyze)):
            current_list_x, current_list_y = list(zip(*polygons_to_analyze[j]))
            list_x, list_y = list(zip(*polygons_to_analyze[j-1]))
            min_current_y = min(current_list_y)
            max_y = max(list_y)

            if current_max_point_y - current_min_point_y < min_current_y - max_y:
                placed = True
                point_y = max_y + LAMBDA
                array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, point_y)
                new_polygons.append(array_polygons[i])
                break

        if not placed:
            point_y = return_line_y(polygons_to_analyze)
            array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, point_y)
            new_polygons.append(array_polygons[i])

    return Polygon.create_polygons_to_plot(new_polygons), return_line_y(new_polygons)


def random_solve(array_polygons, x_lim, function):
    shuffle(array_polygons)
    return function(array_polygons, x_lim)


def solve(array_polygons, x_lim, function, sort_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    return function(array_polygons, x_lim)


def return_line_y(array_polygons):
    line_y = 0

    for polygon in array_polygons:
        list_x, list_y = zip(*polygon)
        highest_y = max(list_y)
        if max(list_y) > line_y:
            line_y = highest_y
    return line_y + LAMBDA


def sort_polygons_to_analyze(polygons):
    index = 0
    list_min_y_index = []
    for polygon in polygons:
        list_x, list_y = list(zip(*polygon))
        list_min_y_index.append((min(list_y), index))
        index += 1
    list_min_y_index.sort(key=lambda tup: tup[0])
    polygons_sorted = []
    for i in range(len(polygons)):
        polygons_sorted.append(polygons[int(list_min_y_index[i][1])])
    return polygons_sorted
