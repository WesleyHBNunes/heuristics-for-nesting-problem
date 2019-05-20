import math
import matplotlib.patches
import numpy as np
import shapely.geometry


def create_polygon(polygons_points):
    polygon = matplotlib.patches.Polygon(polygons_points, True)
    return polygon


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

    if min_y < 0:
        for i in range(len(list_points_y)):
            list_points_y[i] += (min_y * -1)

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
    return (rectangle_polygon_area(polygon) - area_polygon(polygon) * 100) / rectangle_polygon_area(polygon)


def sort(polygons, function):
    list_areas_index = []
    index = 0
    for polygon in polygons:
        list_areas_index.append((function(polygon), index))
        index += 1
    list_areas_index.sort(key=lambda tup: tup[0], reverse=True)
    polygons_sorted = []
    for i in range(len(polygons)):
        polygons_sorted.append(polygons[int(list_areas_index[i][1])])
    return polygons_sorted


def rotate_polygon(polygon, angle):
    angle = math.radians(angle)
    rotated_polygon = []
    for points in polygon:
        rotated_polygon.append((points[0] * math.cos(angle) - points[1] * math.sin(angle),
                                points[0] * math.sin(angle) + points[1] * math.cos(angle)))

    rotated_polygon = set_points_to_positive(rotated_polygon)
    return rotated_polygon


def is_overlapping(current_polygon, polygon):
    current_polygon = shapely.geometry.Polygon(current_polygon)
    polygon = shapely.geometry.Polygon(polygon)
    return current_polygon.intersects(polygon)


def create_polygons_to_plot(polygons):
    polygons_object = []
    for polygon in polygons:
        polygons_object.append(create_polygon(np.array(polygon)))
    return polygons_object


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
