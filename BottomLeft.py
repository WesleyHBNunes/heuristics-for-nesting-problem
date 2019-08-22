from random import shuffle
import Heuristics
import Polygon


def solution(array_polygons, x_lim, function):
    new_polygons = []
    for i in range(len(array_polygons)):

        array_polygons[i] = Heuristics.rotate_polygon_heuristic(array_polygons[i], function)
        if i == 0:
            new_polygons.append(array_polygons[i])
            continue
        list_x, list_y = list(zip(*new_polygons[i - 1]))
        max_point_x = max(list_x)

        current_list_x, current_list_y = list(zip(*array_polygons[i]))

        if max(current_list_x) + max_point_x < x_lim:
            point_x = max_point_x
        else:
            point_x = 0

        array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], point_x, 0)
        current_list_x, current_list_y = list(zip(*array_polygons[i]))
        current_list_x = list(current_list_x)
        current_max_point_x = max(current_list_x)
        current_min_point_x = min(current_list_x)

        highest_y_point = Heuristics.return_line_y(new_polygons)
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
                array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, max_point_y)
                if not polygon_overlapping(array_polygons[i], polygons_to_analyze):
                    array_polygons[i] = original_polygon
                    array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], 0, max_point_y)
                    new_polygons.append(array_polygons[i])
                    break
        else:
            new_polygons.append(array_polygons[i])

    return new_polygons, Heuristics.return_line_y(new_polygons)


def random_solve(array_polygons, x_lim, function):
    shuffle(array_polygons)
    return function(array_polygons, x_lim)


def solve(array_polygons, x_lim, sort_function, rotate_function, reverse):
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse=reverse)
    return solution(array_polygons, x_lim, rotate_function)


def polygon_overlapping(polygon, polygons_to_analyze):
    for p in polygons_to_analyze:
        if Polygon.is_overlapping(polygon, p):
            return True
    return False
