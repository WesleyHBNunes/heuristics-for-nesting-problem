import math
import sys
import copy

EPSILON = math.sqrt(sys.float_info.epsilon)


def set_points_to_positive(polygons_point):
    list_points_x, list_points_y = zip(*polygons_point)
    list_points_x = list(list_points_x)
    list_points_y = list(list_points_y)

    min_x = min(list_points_x)
    min_y = min(list_points_y)

    if min_x >= 0 and min_y >= 0:
        return polygons_point

    if min_x < 0:
        for i in range(len(list_points_x)):
            list_points_x[i] += (min_x * -1)
            list_points_x[i] = list_points_x[i]
            list_points_x[i] = int(list_points_x[i] * 100000) / 100000

    if min_y < 0:
        for i in range(len(list_points_y)):
            list_points_y[i] += (min_y * -1)
            list_points_y[i] = list_points_y[i]
            list_points_y[i] = int(list_points_y[i] * 100000) / 100000
    return list(zip(list_points_x, list_points_y))


def return_to_origin(polygons_point):
    list_points_x, list_points_y = zip(*polygons_point)

    list_points_x = list(list_points_x)
    list_points_y = list(list_points_y)

    min_x = min(list_points_x)
    min_y = min(list_points_y)

    if min_x <= .00000000001 and min_y <= .00000000001:
        return polygons_point

    if min_x > .00000000001:
        for i in range(len(list_points_x)):
            list_points_x[i] -= min_x
            list_points_x[i] = list_points_x[i]
            list_points_x[i] = int(list_points_x[i] * 100000) / 100000

    if min_y > .00000000001:
        for i in range(len(list_points_y)):
            list_points_y[i] -= min_y
            list_points_y[i] = list_points_y[i]
            list_points_y[i] = int(list_points_y[i] * 100000) / 100000

    return list(zip(list_points_x, list_points_y))


def add_number_axis_x_y(polygon, number_x, number_y, triangles):
    list_x, list_y = zip(*polygon)
    list_x = list(list_x)
    list_y = list(list_y)
    n = len(triangles)
    for i in range(len(list_x)):
        list_x[i] = list_x[i] + number_x
        list_x[i] = int(list_x[i] * 100000) / 100000
        list_y[i] = list_y[i] + number_y
        list_y[i] = int(list_y[i] * 100000) / 100000
        if i < n:
            valor_x_0 = triangles[i][0][0] + number_x
            valor_x_0 = int(valor_x_0 * 100000) / 100000
            valor_x_1 = triangles[i][1][0] + number_x
            valor_x_1 = int(valor_x_1 * 100000) / 100000
            valor_x_2 = triangles[i][2][0] + number_x
            valor_x_2 = int(valor_x_2 * 100000) / 100000

            valor_y_0 = triangles[i][0][1] + number_y
            valor_y_0 = int(valor_y_0 * 100000) / 100000
            valor_y_1 = triangles[i][1][1] + number_y
            valor_y_1 = int(valor_y_1 * 100000) / 100000
            valor_y_2 = triangles[i][2][1] + number_y
            valor_y_2 = int(valor_y_2 * 100000) / 100000
            triangles[i] = ((valor_x_0, valor_y_0), (valor_x_1, valor_y_1), (valor_x_2, valor_y_2))
    return list(zip(list_x, list_y))


def area_polygon(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2.0
    return area


def distances_two_points(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def ray_polygon(polygon):
    min_x, max_x, min_y, max_y = min_max_points_polygon(polygon)
    return math.sqrt((max_x - min_x) ** 2 + (max_y - min_y) ** 2)


def rectangle_polygon_area(polygon):
    min_x, max_x, min_y, max_y = min_max_points_polygon(polygon)
    return (max_x - min_x) * (max_y - min_y)


def area_no_used_of_polygon(polygon):
    return rectangle_polygon_area(polygon) - area_polygon(polygon)


def percent_area_no_used_of_polygon(polygon):
    return ((rectangle_polygon_area(polygon) - area_polygon(polygon)) * 100) / rectangle_polygon_area(polygon)


def minimum_y(polygon):
    list_points_x, list_points_y = zip(*polygon)
    list_points_y = list(list_points_y)
    min_y = min(list_points_y)
    return min_y


def sort(polygons, function, reverse):
    list_areas_index = []
    index = 0
    for polygon in polygons:
        list_areas_index.append((function(polygon), index))
        index += 1
    list_areas_index.sort(key=lambda tup: tup[0], reverse=reverse)
    polygons_sorted = []
    for i in range(len(polygons)):
        polygons_sorted.append(polygons[int(list_areas_index[i][1])])
    return polygons_sorted


# def rotate_polygon(polygon, angle):
#     angle = math.radians(angle)
#     rotated_polygon = []
#     for points in polygon:
#         point_x = points[0] * math.cos(angle) - points[1] * math.sin(angle)
#         point_y = points[0] * math.sin(angle) + points[1] * math.cos(angle)
#         rotated_polygon.append((point_x, point_y))
#     rotated_polygon = set_points_to_positive(rotated_polygon)
#     rotated_polygon = return_to_origin(rotated_polygon)
#     rotated_polygon = truncate_point(rotated_polygon)
#     return rotated_polygon

def set_points_to_positive_triangles(polygons_point, triangles, n):
    list_points_x, list_points_y = zip(*polygons_point)
    list_points_x = list(list_points_x)
    list_points_y = list(list_points_y)

    min_x = min(list_points_x)
    min_y = min(list_points_y)

    if min_x >= 0 and min_y >= 0:
        return polygons_point

    if min_x < 0:
        for i in range(len(list_points_x)):
            list_points_x[i] += (min_x * -1)
            list_points_x[i] = list_points_x[i]
            list_points_x[i] = int(list_points_x[i] * 100000) / 100000
            if i < n:
                x_1 = triangles[i][0][0] + (min_x * -1)
                x_2 = triangles[i][1][0] + (min_x * -1)
                x_3 = triangles[i][2][0] + (min_x * -1)
                t1 = (int(x_1 * 100000) / 100000, triangles[i][0][1])
                t2 = (int(x_2 * 100000) / 100000, triangles[i][1][1])
                t3 = (int(x_3 * 100000) / 100000, triangles[i][2][1])
                triangles[i] = (t1, t2, t3)

    if min_y < 0:
        for i in range(len(list_points_y)):
            list_points_y[i] += (min_y * -1)
            list_points_y[i] = list_points_y[i]
            list_points_y[i] = int(list_points_y[i] * 100000) / 100000
            if i < n:
                y_1 = triangles[i][0][1] + (min_y * -1)
                y_2 = triangles[i][1][1] + (min_y * -1)
                y_3 = triangles[i][2][1] + (min_y * -1)
                t1 = (triangles[i][0][0], int(y_1 * 100000) / 100000)
                t2 = (triangles[i][1][0], int(y_2 * 100000) / 100000)
                t3 = (triangles[i][2][0], int(y_3 * 100000) / 100000)
                triangles[i] = (t1, t2, t3)
    return list(zip(list_points_x, list_points_y))


def return_to_origin_triangles(polygons_point, triangles, n):
    list_points_x, list_points_y = zip(*polygons_point)

    list_points_x = list(list_points_x)
    list_points_y = list(list_points_y)

    min_x = min(list_points_x)
    min_y = min(list_points_y)

    if min_x <= .00000000001 and min_y <= .00000000001:
        return polygons_point

    if min_x > .00000000001:
        for i in range(len(list_points_x)):
            list_points_x[i] -= min_x
            list_points_x[i] = int(list_points_x[i] * 100000) / 100000
            if i < n:
                x_1 = triangles[i][0][0] - min_x
                x_2 = triangles[i][1][0] - min_x
                x_3 = triangles[i][2][0] - min_x
                t1 = (int(x_1 * 100000) / 100000, triangles[i][0][1])
                t2 = (int(x_2 * 100000) / 100000, triangles[i][1][1])
                t3 = (int(x_3 * 100000) / 100000, triangles[i][2][1])
                triangles[i] = (t1, t2, t3)

    if min_y > .00000000001:
        for i in range(len(list_points_y)):
            list_points_y[i] -= min_y
            list_points_y[i] = list_points_y[i]
            list_points_y[i] = int(list_points_y[i] * 100000) / 100000
            if i < n:
                y_1 = triangles[i][0][1] - min_y
                y_2 = triangles[i][1][1] - min_y
                y_3 = triangles[i][2][1] - min_y
                t1 = (triangles[i][0][0], int(y_1 * 100000) / 100000)
                t2 = (triangles[i][1][0], int(y_2 * 100000) / 100000)
                t3 = (triangles[i][2][0], int(y_3 * 100000) / 100000)
                triangles[i] = (t1, t2, t3)

    return list(zip(list_points_x, list_points_y))


def truncate_point_triangles(polygon, triangles, n):
    list_x, list_y = zip(*polygon)
    list_x = list(list_x)
    list_y = list(list_y)
    for i in range(len(list_x)):
        list_x[i] = int(list_x[i] * 100000) / 100000
        list_y[i] = int(list_y[i] * 100000) / 100000
        if i < n:
            x_1 = int(triangles[i][0][0] * 100000) / 100000
            y_1 = int(triangles[i][0][1] * 100000) / 100000

            x_2 = int(triangles[i][1][0] * 100000) / 100000
            y_2 = int(triangles[i][1][1] * 100000) / 100000

            x_3 = int(triangles[i][2][0] * 100000) / 100000
            y_3 = int(triangles[i][2][1] * 100000) / 100000
            triangles[i] = ((x_1, y_1), (x_2, y_2), (x_3, y_3))
    return list(zip(list_x, list_y))


def rotate_polygon(polygon, angle, triangles):
    angle = math.radians(angle)
    rotated_polygon = []
    n = len(triangles)
    for i, points in enumerate(polygon):
        point_x = points[0] * math.cos(angle) - points[1] * math.sin(angle)
        point_y = points[0] * math.sin(angle) + points[1] * math.cos(angle)
        rotated_polygon.append((point_x, point_y))
        if i < n:
            point_x_1 = triangles[i][0][0] * math.cos(angle) - triangles[i][0][1] * math.sin(angle)
            point_y_1 = triangles[i][0][0] * math.sin(angle) + triangles[i][0][1] * math.cos(angle)

            point_x_2 = triangles[i][1][0] * math.cos(angle) - triangles[i][1][1] * math.sin(angle)
            point_y_2 = triangles[i][1][0] * math.sin(angle) + triangles[i][1][1] * math.cos(angle)

            point_x_3 = triangles[i][2][0] * math.cos(angle) - triangles[i][2][1] * math.sin(angle)
            point_y_3 = triangles[i][2][0] * math.sin(angle) + triangles[i][2][1] * math.cos(angle)
            triangles[i] = ((point_x_1, point_y_1), (point_x_2, point_y_2), (point_x_3, point_y_3))
    rotated_polygon = set_points_to_positive_triangles(rotated_polygon, triangles, n)
    rotated_polygon = return_to_origin_triangles(rotated_polygon, triangles, n)
    rotated_polygon = truncate_point_triangles(rotated_polygon, triangles, n)
    return rotated_polygon


def rotate_polygon_no_tri(polygon, angle):
    angle = math.radians(angle)
    rotated_polygon = []
    for i, points in enumerate(polygon):
        point_x = points[0] * math.cos(angle) - points[1] * math.sin(angle)
        point_y = points[0] * math.sin(angle) + points[1] * math.cos(angle)
        rotated_polygon.append((point_x, point_y))
    return rotated_polygon


def rotate_polygon_angle(polygon, angle):
    angle = math.radians(angle)
    rotated_polygon = []
    for i, points in enumerate(polygon):
        point_x = points[0] * math.cos(angle) - points[1] * math.sin(angle)
        point_y = points[0] * math.sin(angle) + points[1] * math.cos(angle)
        rotated_polygon.append((point_x, point_y))
    return rotated_polygon


def polygon_overlapping(polygon, polygons_to_analyze):
    triangles_to_analyze = triangulation_all_polygons(polygons_to_analyze)
    for p in triangles_to_analyze:
        if is_overlapping(polygon, p):
            return True
    return False


def min_max_points_polygon(polygon):
    list_points_x, list_points_y = zip(*polygon)

    list_points_x = list(list_points_x)
    list_points_y = list(list_points_y)

    min_x = min(list_points_x)
    min_y = min(list_points_y)

    max_x = max(list_points_x)
    max_y = max(list_points_y)

    return min_x, max_x, min_y, max_y


def width_height(polygon):

    min_x, max_x, min_y, max_y = min_max_points_polygon(polygon)
    return max_x - min_x, max_y - min_y


def highest_side(polygon):
    final_points_x = ()
    final_points_y = ()
    highest_side_of_polygon = 0
    for i in range(len(polygon)):
        if i == len(polygon) - 1:
            point1 = polygon[i]
            point2 = polygon[0]
        else:
            point1 = polygon[i]
            point2 = polygon[i + 1]

        if point1[0] > point2[0]:
            x_min = point2[0]
            x_max = point1[0]
        else:
            x_min = point1[0]
            x_max = point2[0]

        if point1[1] > point2[1]:
            y_min = point2[1]
            y_max = point1[1]
        else:
            y_min = point1[1]
            y_max = point2[1]

        value = math.sqrt((x_max - x_min) ** 2 + (y_max - y_min) ** 2)

        if value > highest_side_of_polygon:
            highest_side_of_polygon = value
            final_points_x = (x_max, x_min)
            final_points_y = (y_max, y_min)

    return final_points_x, final_points_y


def move_polygon_by_reference_point(index, polygon, point_to_move, triangles):
    point = polygon[index]
    movements_x = point_to_move[0] - point[0]
    movements_y = point_to_move[1] - point[1]
    polygon_moved = []
    n = len(triangles)
    for i, p in enumerate(polygon):
        point_x = p[0] + movements_x
        point_x = int(point_x * 100000) / 100000
        point_y = p[1] + movements_y
        point_y = int(point_y * 100000) / 100000
        polygon_moved.append((point_x, point_y))
        if i < n:
            valor_x_0 = triangles[i][0][0] + movements_x
            valor_x_0 = int(valor_x_0 * 100000) / 100000
            valor_x_1 = triangles[i][1][0] + movements_x
            valor_x_1 = int(valor_x_1 * 100000) / 100000
            valor_x_2 = triangles[i][2][0] + movements_x
            valor_x_2 = int(valor_x_2 * 100000) / 100000

            valor_y_0 = triangles[i][0][1] + movements_y
            valor_y_0 = int(valor_y_0 * 100000) / 100000
            valor_y_1 = triangles[i][1][1] + movements_y
            valor_y_1 = int(valor_y_1 * 100000) / 100000
            valor_y_2 = triangles[i][2][1] + movements_y
            valor_y_2 = int(valor_y_2 * 100000) / 100000
            triangles[i] = ((valor_x_0, valor_y_0), (valor_x_1, valor_y_1), (valor_x_2, valor_y_2))
    return polygon_moved


def negative_point(polygon):
    for p in polygon:
        if p[0] < 0 or p[1] < 0:
            return True
    return False


def calculate_ifp_between_two_polygons(polygons, index_fixed_polygon, index, placed, limit_x, triangles):
    polygon = polygons[index_fixed_polygon]
    polygon2 = polygons[index]
    triangles2 = copy.deepcopy(triangles[index])
    inner_fit_polygon = []
    for p in polygon:
        for i in range(len(polygon2)):
            polygon2 = move_polygon_by_reference_point(i, polygon2, p, triangles2)
            list_points_x, list_points_y = zip(*polygon2)
            if is_overlapping(triangles2, triangles[index_fixed_polygon]) \
                    or negative_point(polygon2) or max(list_points_x) > limit_x:
                continue
            else:
                overlapping = False
                for j in range(len(polygons)):
                    if not placed[j]:
                        break
                    if index != j and index_fixed_polygon != j:
                        if is_overlapping(triangles2, triangles[j]):
                            overlapping = True
                            break
                if not overlapping:
                    inner_fit_polygon.append((i, p[0], p[1]))
    return inner_fit_polygon


def return_best_point_in_ifp(ifp):
    if not ifp:
        return ()
    point = ifp[0]
    for p in ifp:
        if p == ():
            continue
        if p[2] < point[2]:
            point = p
        elif p[2] == point[2] and p[1] < point[1]:
            point = p
    return point


def truncate_point(polygon):
    list_x, list_y = zip(*polygon)
    list_x = list(list_x)
    list_y = list(list_y)
    for i in range(len(list_x)):
        list_x[i] = int(list_x[i] * 100000) / 100000
        list_y[i] = int(list_y[i] * 100000) / 100000
    return list(zip(list_x, list_y))


def pre_process_overlap(polygon_1, polygon_2):
    min_x1, max_x1, min_y1, max_y1 = min_max_points_polygon(polygon_1)
    min_x2, max_x2, min_y2, max_y2 = min_max_points_polygon(polygon_2)

    if min_x1 >= max_x2:
        return False
    elif min_x2 >= max_x1:
        return False
    elif min_y1 >= max_y2:
        return False
    elif min_y2 >= max_y1:
        return False
    return True


def ear_clip(polygon_original):
    polygon = [p for p in polygon_original]
    """
    Simple ear clipping algorithm for a given polygon p.
    polygon is expected to be an array of 2-tuples of the cartesian points of the polygon
    For a polygon with n points it will return n-2 triangles.
    The triangles are returned as an array of 3-tuples where each item in the tuple is a 2-tuple of the cartesian point.
    e.g
    [((1, 0), (0, 1), (-1, 0)), ((1, 0), (-1, 0), (0, -1))]
    Implementation Reference:
        - https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf
    """
    ear_vertex = []
    triangles = []

    # if is_clockwise(polygon):
    #     polygon.reverse()

    point_count = len(polygon)
    for i in range(point_count):
        prev_index = i - 1
        prev_point = polygon[prev_index]
        point = polygon[i]
        next_index = (i + 1) % point_count
        next_point = polygon[next_index]

        if is_ear(prev_point, point, next_point, polygon):
            ear_vertex.append(point)

    while ear_vertex and point_count >= 3:
        ear = ear_vertex.pop(0)
        i = polygon.index(ear)
        prev_index = i - 1
        prev_point = polygon[prev_index]
        next_index = (i + 1) % point_count
        next_point = polygon[next_index]

        polygon.remove(ear)
        point_count -= 1
        triangles.append(((prev_point[0], prev_point[1]), (ear[0], ear[1]), (next_point[0], next_point[1])))
        if point_count > 3:
            prev_prev_point = polygon[prev_index - 1]
            next_next_index = (i + 1) % point_count
            next_next_point = polygon[next_next_index]

            groups = [
                (prev_prev_point, prev_point, next_point, polygon),
                (prev_point, next_point, next_next_point, polygon),
            ]
            for group in groups:
                p = group[1]
                if is_ear(*group):
                    if p not in ear_vertex:
                        ear_vertex.append(p)
                elif p in ear_vertex:
                    ear_vertex.remove(p)
    return triangles


def is_clockwise(polygon):
    s = 0
    polygon_count = len(polygon)
    for i in range(polygon_count):
        point = polygon[i]
        point2 = polygon[(i + 1) % polygon_count]
        s += (point2[0] - point[0]) * (point2[1] + point[1])
    return s > 0


def is_convex(prev, point, next_point):
    return triangle_sum(prev[0], prev[1], point[0], point[1], next_point[0], next_point[1]) < 0


def is_ear(p1, p2, p3, polygon):
    ear = contains_no_points(p1, p2, p3, polygon) and \
          is_convex(p1, p2, p3) and \
          triangle_area(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]) > 0
    return ear


def contains_no_points(p1, p2, p3, polygon):
    for pn in polygon:
        if pn in (p1, p2, p3):
            continue
        elif is_point_inside(pn, p1, p2, p3):
            return False
    return True


def is_point_inside(p, a, b, c):
    area = triangle_area(a[0], a[1], b[0], b[1], c[0], c[1])
    area1 = triangle_area(p[0], p[1], b[0], b[1], c[0], c[1])
    area2 = triangle_area(p[0], p[1], a[0], a[1], c[0], c[1])
    area3 = triangle_area(p[0], p[1], a[0], a[1], b[0], b[1])
    area_dif = abs(area - sum([area1, area2, area3])) < EPSILON
    return area_dif


def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def triangle_sum(x1, y1, x2, y2, x3, y3):
    return x1 * (y3 - y2) + x2 * (y1 - y3) + x3 * (y2 - y1)


def return_all_polygons_triangulated(polygons):
    triangles = []
    for p in polygons:
        p = ear_clip(p)
        for triangle in p:
            triangles.append(triangle)
    return triangles


def is_overlapping(polygon1, polygon2):
    for triangle_1 in polygon1:
        for triangle_2 in polygon2:
            if is_overlapping_decider(triangle_1, triangle_2):
                return True
    return False


def is_overlapping3(polygon1, polygon2):
    if not pre_process_overlap(polygon1, polygon2):
        return False

    triangles_1 = ear_clip(polygon1)
    triangles_2 = ear_clip(polygon2)

    for triangle_1 in triangles_1:
        for triangle_2 in triangles_2:
            if is_overlapping_decider(triangle_1, triangle_2):
                return True

    # for triangle_1 in polygon1:
    #     for triangle_2 in polygon2:
    #         if is_overlapping_decider(triangle_1, triangle_2):
    #             return True
    return False


def is_overlapping_decider(polygon_1, polygon_2):
    if not pre_process_overlap(polygon_1, polygon_2):
        return False
    if polygon_1 == polygon_2:
        return True
    for i in range(len(polygon_1)):
        for j in range(len(polygon_2)):
            seg1 = (polygon_1[i], polygon_1[(i + 1) % len(polygon_1)])
            medium_point_seg1 = ((seg1[0][0] + seg1[1][0]) / 2, (seg1[0][1] + seg1[1][1]) / 2)
            point_in_polygon(medium_point_seg1, polygon_2)
            seg2 = (polygon_2[j], polygon_2[(j + 1) % len(polygon_2)])
            medium_point_seg2 = ((seg2[0][0] + seg2[1][0]) / 2, (seg2[0][1] + seg2[1][1]) / 2)
            point_in_polygon(medium_point_seg2, polygon_1)
            if intersection_two_lines_segments(seg1, seg2) or \
                    point_in_polygon(medium_point_seg2, polygon_1) or point_in_polygon(medium_point_seg1, polygon_2):
                return True
    for p in polygon_2:
        if point_in_polygon(p, polygon_1):
            return True
    for p in polygon_1:
        if point_in_polygon(p, polygon_2):
            return True

    if point_in_any_segments(polygon_1[0], polygon_2) and point_in_any_segments(polygon_1[1], polygon_2) \
            and point_in_any_segments(polygon_1[2], polygon_2):
        return True

    if point_in_any_segments(polygon_2[0], polygon_1) and point_in_any_segments(polygon_2[1], polygon_1) \
            and point_in_any_segments(polygon_2[2], polygon_1):
        return True

    return False


def intersection_two_lines_segments(seg1, seg2):
    if point_in_segment(seg1[0], seg2) or point_in_segment(seg1[1], seg2) or \
            point_in_segment(seg2[0], seg1) or point_in_segment(seg2[1], seg1):
        return False

    """
    Check that two line segments meet
    Algorithm based in http://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    :param seg1: segment one
    :param seg2: segment two
    :return: if exist intersection or not
    """
    o1 = points_orientation(seg1[0], seg1[1], seg2[0])
    o2 = points_orientation(seg1[0], seg1[1], seg2[1])
    o3 = points_orientation(seg2[0], seg2[1], seg1[0])
    o4 = points_orientation(seg2[0], seg2[1], seg1[1])

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and point_in_segment(seg2[0], seg1):
        return True
    if o2 == 0 and point_in_segment(seg2[1], seg1):
        return True
    if o3 == 0 and point_in_segment(seg1[0], seg2):
        return True
    if o4 == 0 and point_in_segment(seg1[1], seg2):
        return True

    return False


def point_in_segment(c, s):
    return distances_two_points(s[0], c) + distances_two_points(s[1], c) == distances_two_points(s[0], s[1])


def points_orientation(p, q, r):
    value = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if value == 0:
        return 0
    elif value > 0:
        return 1
    else:
        return 2


def point_in_polygon(p, polygon):
    if len(polygon) < 3 or point_in_any_segments(p, polygon):
        return False

    area_original = triangle_area_with_triangle(polygon)
    a1 = triangle_area_with_triangle([polygon[0], polygon[1], p])
    a2 = triangle_area_with_triangle([polygon[1], polygon[2], p])
    a3 = triangle_area_with_triangle([polygon[0], polygon[2], p])
    if a1 + a2 + a3 <= area_original + 0.000001:
        return True
    return False


def triangle_area_with_triangle(triangle):
    x1, y1 = triangle[0][0], triangle[0][1]
    x2, y2 = triangle[1][0], triangle[1][1]
    x3, y3 = triangle[2][0], triangle[2][1]
    return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))


def point_in_any_segments(p, polygon):
    for i in range(len(polygon)):
        seg1 = (polygon[i], polygon[(i + 1) % len(polygon)])
        if point_in_segment(p, seg1):
            return True


def triangulation_all_polygons(polygons):
    triangles_list = []
    for polygon in polygons:
        triangles = [p for p in polygon]
        triangles = ear_clip(triangles)
        triangles_list.append(triangles)
    return triangles_list
