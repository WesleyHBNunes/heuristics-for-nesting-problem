import Heuristics
import Polygon
import copy


def placement_vertex(polygons, index, limit_x, placed, triangles_polygons):
    polygons[index] = Heuristics.decide_best_position(polygons, index, limit_x, placed, triangles_polygons)
    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x, triangles_polygons)
    return polygons[index]


def placement_greedy(polygons, index, limit_x, placed, triangles_polygons):
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
        polygons[index] = Polygon.add_number_axis_x_y(polygons[index], jump, 0, triangles_polygons[index])
        list_x, list_y = list(zip(*polygons[index]))
        max_point_x = max(list_x)
        min_point_x = min(list_x)
        if max_point_x > limit_x:
            polygons[index] = \
                Polygon.add_number_axis_x_y(polygons[index], - min_point_x, jump, triangles_polygons[index])
        for j in range(len(polygons)):
            overlapping = False
            if placed[j] and index != j:
                if Polygon.is_overlapping(triangles_polygons[index], triangles_polygons[j]):
                    overlapping = True
                    break

    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x, triangles_polygons)
    return polygons[index]


def placement_bottom_left_slide(polygons, index, limit_x, placed, triangles_polygons):
    if index == 0:
        return polygons[index]
    list_x, list_y = list(zip(*polygons[index]))
    max_point_x = max(list_x)
    polygons[index] = Polygon.add_number_axis_x_y(polygons[index], limit_x - max_point_x,
                                                  Heuristics.calculate_function_objective(polygons, placed),
                                                  triangles_polygons[index])
    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x, triangles_polygons)
    return polygons[index]


def placement_bottom_left(polygons, index, limit_x, new_polygons, triangles_polygons):
    if index == 0:
        return polygons[index]
    list_x, list_y = list(zip(*new_polygons[index - 1]))
    max_point_x = max(list_x)
    current_list_x, current_list_y = list(zip(*polygons[index]))

    if max(current_list_x) + max_point_x < limit_x:
        point_x = max_point_x
    else:
        point_x = 0

    polygons[index] = Polygon.add_number_axis_x_y(polygons[index], point_x, 0, triangles_polygons[index])
    current_list_x, current_list_y = list(zip(*polygons[index]))
    current_list_x = list(current_list_x)
    current_max_point_x = max(current_list_x)
    current_min_point_x = min(current_list_x)

    highest_y_point = Heuristics.return_line_y(new_polygons)
    abstract_polygon = [(current_min_point_x, 0),
                        (current_max_point_x, 0),
                        (current_max_point_x, highest_y_point),
                        (current_min_point_x, highest_y_point)]
    abstract_polygon_triangle = Polygon.ear_clip(abstract_polygon)
    polygons_to_analyze = []
    for i, polygon in enumerate(new_polygons):
        if Polygon.is_overlapping(abstract_polygon_triangle, triangles_polygons[i]):
            polygons_to_analyze.append(polygon)

    original_polygon = polygons[index]
    original_triangles = copy.deepcopy(triangles_polygons[index])
    # original_triangles = cPickle.loads(cPickle.dumps(triangles_polygons[index], -1))
    if Polygon.polygon_overlapping(triangles_polygons[index], polygons_to_analyze):
        polygons_to_analyze = Polygon.sort(polygons_to_analyze, Polygon.minimum_y, False)
        for polygon_overlapped in polygons_to_analyze:
            list_x, list_y = list(zip(*polygon_overlapped))
            max_point_y = max(list_y)
            polygons[index] = original_polygon
            triangles_polygons[index] = copy.deepcopy(original_triangles)
            # triangles_polygons[index] = cPickle.loads(cPickle.dumps(original_triangles, -1))
            polygons[index] = \
                Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y + 0.000001, triangles_polygons[index])
            if not Polygon.polygon_overlapping(triangles_polygons[index], polygons_to_analyze):
                polygons[index] = original_polygon
                # triangles_polygons[index] = cPickle.loads(cPickle.dumps(original_triangles, -1))
                triangles_polygons[index] = copy.deepcopy(original_triangles)
                polygons[index] = \
                    Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y, triangles_polygons[index])
                return polygons[index]
    else:
        return polygons[index]


def placement_bottom_left_greedy(polygons, index, limit_x, placed, triangles_polygons):
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
    # original_triangles = cPickle.loads(cPickle.dumps(triangles_polygons[index], -1))
    original_triangles = copy.deepcopy(triangles_polygons[index])
    possibles_positions = []
    jump = 0
    while not stop:
        polygons[index] = original_polygon
        # triangles_polygons[index] = cPickle.loads(cPickle.dumps(original_triangles, -1))
        triangles_polygons[index] = copy.deepcopy(original_triangles)
        polygons[index] = Polygon.add_number_axis_x_y(polygons[index], jump, 0, triangles_polygons[index])
        current_list_x, current_list_y = list(zip(*polygons[index]))
        if max(current_list_x) > limit_x:
            stop = True
            continue
        jump += jump_value
        jump = int(jump * 100) / 100
        highest_y_point = Heuristics.return_line_y(polygons)
        current_max_point_x = max(current_list_x)
        current_min_point_x = min(current_list_x)
        abstract_polygon = [(current_min_point_x, 0),
                            (current_max_point_x, 0),
                            (current_max_point_x, highest_y_point),
                            (current_min_point_x, highest_y_point)]
        abstract_polygon_triangle = Polygon.ear_clip(abstract_polygon)
        polygons_to_analyze = []
        for i in range(len(polygons)):
            if Polygon.is_overlapping(abstract_polygon_triangle, triangles_polygons[i]) and placed[i] and index != i:
                polygons_to_analyze.append(polygons[i])
        aux_polygon = polygons[index]
        # aux_triangle_polygons = cPickle.loads(cPickle.dumps(triangles_polygons[index], -1))
        aux_triangle_polygons = copy.deepcopy(triangles_polygons[index])
        if not Polygon.polygon_overlapping(triangles_polygons[index], polygons_to_analyze):
            possibles_positions.append(polygons[index])
        else:
            polygons_to_analyze = Polygon.sort(polygons_to_analyze, Polygon.minimum_y, False)
            for polygon_overlapped in polygons_to_analyze:
                list_x, list_y = list(zip(*polygon_overlapped))
                max_point_y = max(list_y)
                polygons[index] = aux_polygon
                # triangles_polygons[index] = cPickle.loads(cPickle.dumps(aux_triangle_polygons, -1))
                triangles_polygons[index] = copy.deepcopy(aux_triangle_polygons)
                polygons[index] = \
                    Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y, triangles_polygons[index])
                if not Polygon.polygon_overlapping(triangles_polygons[index], polygons_to_analyze):
                    polygons[index] = aux_polygon
                    triangles_polygons[index] = copy.deepcopy(aux_triangle_polygons)
                    # triangles_polygons[index] = cPickle.loads(cPickle.dumps(aux_triangle_polygons, -1))
                    polygons[index] = \
                        Polygon.add_number_axis_x_y(polygons[index], 0, max_point_y, triangles_polygons[index])
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
    triangles_aux = [p for p in polygons[index]]
    triangles_polygons[index] = Polygon.ear_clip(triangles_aux)
    polygons[index] = Heuristics.slide_polygon(polygons, placed, index, limit_x, triangles_polygons)
    return polygons[index]
