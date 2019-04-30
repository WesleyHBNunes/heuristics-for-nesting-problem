from matplotlib.patches import Polygon


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
