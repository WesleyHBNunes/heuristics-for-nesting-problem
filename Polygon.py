import math
import shapely.geometry


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

    if min_y < 0:
        for i in range(len(list_points_y)):
            list_points_y[i] += (min_y * -1)
            list_points_y[i] = list_points_y[i]

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

    if min_y > .00000000001:
        for i in range(len(list_points_y)):
            list_points_y[i] -= min_y
            list_points_y[i] = list_points_y[i]

    return list(zip(list_points_x, list_points_y))


def add_number_axis_x_y(polygon, number_x, number_y):
    list_x, list_y = zip(*polygon)
    list_x = list(list_x)
    list_y = list(list_y)
    for i in range(len(list_x)):
        list_x[i] = list_x[i] + number_x
        list_y[i] = list_y[i] + number_y
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


def ray_polygon(polygon):
    min_x, max_x, min_y, max_y = min_max_points_polygon(polygon)
    return math.sqrt((max_x - min_x) ** 2 + (max_y - min_y) ** 2)


def rectangle_polygon_area(polygon):
    min_x, max_x, min_y, max_y = min_max_points_polygon(polygon)
    return (max_x - min_x) * (max_y - min_y)


def area_no_used_of_polygon(polygon):
    return rectangle_polygon_area(polygon) - area_polygon(polygon)


def percent_area_no_used_of_polygon(polygon):
    return (rectangle_polygon_area(polygon) - area_polygon(polygon) * 100000) / rectangle_polygon_area(polygon)


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


def rotate_polygon(polygon, angle):
    angle = math.radians(angle)
    rotated_polygon = []
    for points in polygon:
        point_x = points[0] * math.cos(angle) - points[1] * math.sin(angle)
        point_y = points[0] * math.sin(angle) + points[1] * math.cos(angle)
        rotated_polygon.append((point_x, point_y))

    rotated_polygon = set_points_to_positive(rotated_polygon)
    rotated_polygon = return_to_origin(rotated_polygon)
    return rotated_polygon


def is_overlapping(current_polygon, polygon):
    try:
        polygon1 = shapely.geometry.Polygon(current_polygon)
        polygon2 = shapely.geometry.Polygon(polygon)
        if polygon1.touches(polygon2):
            return False
        return polygon1.intersects(polygon2)
    except:
        current_polygon = truncate_point(current_polygon)
        polygon = truncate_point(polygon)
        polygon1 = shapely.geometry.Polygon(current_polygon)
        polygon2 = shapely.geometry.Polygon(polygon)
        if polygon1.touches(polygon2):
            return False
        return polygon1.intersects(polygon2)


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


def move_polygon_by_reference_point(index, polygon, point_to_move):
    point = polygon[index]
    movements_x = point_to_move[0] - point[0]
    movements_y = point_to_move[1] - point[1]
    polygon_moved = []
    for p in polygon:
        point_x = p[0] + movements_x
        point_y = p[1] + movements_y
        polygon_moved.append((point_x, point_y))

    return polygon_moved


def negative_point(polygon):
    for p in polygon:
        if p[0] < 0 or p[1] < 0:
            return True
    return False


def calculate_ifp_between_two_polygons(polygon, polygon2):
    inner_fit_polygon = []
    for p in polygon:
        for i in range(len(polygon2)):
            polygon2 = move_polygon_by_reference_point(i, polygon2, p)
            if is_overlapping(polygon2, polygon) or negative_point(polygon2):
                continue
            else:
                inner_fit_polygon.append((i, p[0], p[1]))
    return inner_fit_polygon


def return_real_ifp_between_two_polygons(polygons, index, index_p2, placed):
    ifp = calculate_ifp_between_two_polygons(polygons[index], polygons[index_p2])
    real_ifp = []

    for p in ifp:
        aux = move_polygon_by_reference_point(p[0], polygons[index_p2], (p[1], p[2]))
        overlapping = False
        for i in range(len(polygons)):
            if i != index and i != index_p2:
                if is_overlapping(aux, polygons[i]):
                    if placed[i]:
                        overlapping = True
                        break
        if not overlapping:
            real_ifp.append(p)
    return real_ifp


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
