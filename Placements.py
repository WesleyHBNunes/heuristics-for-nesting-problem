import Heuristics
import Polygon


def placement_vertex(polygons, index, limit_x, placed):
    polygons[index] = Heuristics.decide_best_position(polygons, index, limit_x, placed)
    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x)
    return polygons[index]


def placement_greedy(polygons, index, limit_x, placed):
    if index == 0:
        return polygons[index]
    if limit_x >= 4900:
        jump = 100
    elif 500 <= limit_x < 4900:
        jump = 10
    else:
        jump = 1
    overlapping = True
    while overlapping:
        polygons[index] = Polygon.add_number_axis_x_y(polygons[index], jump, 0)
        list_x, list_y = list(zip(*polygons[index]))
        max_point_x = max(list_x)
        min_point_x = min(list_x)
        if max_point_x > limit_x:
            polygons[index] = Polygon.add_number_axis_x_y(polygons[index], - min_point_x, jump)
        for j in range(len(polygons)):
            overlapping = False
            if placed[j] and index != j:
                if Polygon.is_overlapping(polygons[index], polygons[j]):
                    overlapping = True
                    break

    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x)
    return polygons[index]


def placement_bottom_left_slide(polygons, index, limit_x, placed):
    if index == 0:
        return polygons[index]
    list_x, list_y = list(zip(*polygons[index]))
    max_point_x = max(list_x)
    polygons[index] = Polygon.add_number_axis_x_y(polygons[index], limit_x - max_point_x,
                                                  Heuristics.calculate_function_objective(polygons, placed))
    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x)
    return polygons[index]


def placement_bottom_left(polygons, index, limit_x, new_polygons):
    if index == 0:
        return polygons[index]
    list_x, list_y = list(zip(*new_polygons[index - 1]))
    max_point_x = max(list_x)
    current_list_x, current_list_y = list(zip(*polygons[index]))

    if max(current_list_x) + max_point_x < limit_x:
        point_x = max_point_x
    else:
        point_x = 0

    polygons[index] = Polygon.add_number_axis_x_y(polygons[index], point_x, 0)
    current_list_x, current_list_y = list(zip(*polygons[index]))
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

    original_polygon = polygons[index]
    if Polygon.polygon_overlapping(polygons[index], polygons_to_analyze):
        polygons_to_analyze = Polygon.sort(polygons_to_analyze, Polygon.minimum_y, False)
        for polygon_overlapped in polygons_to_analyze:
            list_x, list_y = list(zip(*polygon_overlapped))
            max_point_y = max(list_y)
            polygons[index] = original_polygon
            polygons[index] = Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y + 0.000001)
            if not Polygon.polygon_overlapping(polygons[index], polygons_to_analyze):
                polygons[index] = original_polygon
                polygons[index] = Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y)
                return polygons[index]
    else:
        return polygons[index]


def placement_bottom_left_greedy(polygons, index, limit_x, placed):
    if index == 0:
        return polygons[index]
    if limit_x >= 4900:
        jump_value = 100
    elif 500 <= limit_x < 4900:
        jump_value = 10
    else:
        jump_value = 1
    stop = False
    original_polygon = polygons[index]
    possibles_positions = []
    jump = 0
    while not stop:
        polygons[index] = original_polygon
        polygons[index] = Polygon.add_number_axis_x_y(polygons[index], jump, 0)
        current_list_x, current_list_y = list(zip(*polygons[index]))
        if max(current_list_x) > limit_x:
            stop = True
            continue
        jump += jump_value
        jump = int(jump * 100)/100
        highest_y_point = Heuristics.return_line_y(polygons)
        current_max_point_x = max(current_list_x)
        current_min_point_x = min(current_list_x)
        abstract_polygon = [(current_min_point_x, 0),
                            (current_max_point_x, 0),
                            (current_max_point_x, highest_y_point),
                            (current_min_point_x, highest_y_point)]

        polygons_to_analyze = []
        for i in range(len(polygons)):
            if Polygon.is_overlapping(abstract_polygon, polygons[i]) and placed[i] and index != i:
                polygons_to_analyze.append(polygons[i])
        aux_polygon = polygons[index]
        if not Polygon.polygon_overlapping(polygons[index], polygons_to_analyze):
            possibles_positions.append(polygons[index])
        else:
            polygons_to_analyze = Polygon.sort(polygons_to_analyze, Polygon.minimum_y, False)
            for polygon_overlapped in polygons_to_analyze:
                list_x, list_y = list(zip(*polygon_overlapped))
                max_point_y = max(list_y)
                polygons[index] = aux_polygon
                polygons[index] = Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y)
                if not Polygon.polygon_overlapping(polygons[index], polygons_to_analyze):
                    polygons[index] = aux_polygon
                    polygons[index] = Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y)
                    possibles_positions.append(polygons[index])
                    break
    best_fo = 99999
    result = []
    placed[index] = True
    for p in possibles_positions:
        polygons[index] = p
        fo = Heuristics.calculate_function_objective(polygons, placed)
        if fo < best_fo:
            result = p
            best_fo = fo
    polygons[index] = result
    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x)
    return polygons[index]
