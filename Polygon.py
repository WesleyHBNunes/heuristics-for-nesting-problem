from matplotlib.patches import Polygon
import math


def create_polygon(polygons_points):
    polygon = Polygon(polygons_points, True)
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


def area_polygon(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def sort_by_area(polygons):
    list_areas_index = []
    index = 0
    for polygon in polygons:
        list_areas_index.append((area_polygon(polygon), index))
        index += 1
    list_areas_index.sort(key=lambda tup: tup[0])
    polygons_sorted = []
    for i in range(len(polygons)):
        polygons_sorted.append(polygons[int(list_areas_index[i][1])])
    return polygons_sorted


def rotate_polygon(polygon, angle):
    angle = math.radians(angle)
    rotated_polygon = []
    for points in polygon:
        rotated_polygon.append((points[0]*math.cos(angle)-points[1]*math.sin(angle),
                                points[0]*math.sin(angle)+points[1]*math.cos(angle)))

    return rotated_polygon
