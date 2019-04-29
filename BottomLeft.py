import Polygon
import numpy as np
import Visualizer

x = 0
y = 1


def initial_solution(array_polygons, x_lim, y_lim):
    new_polygons = []
    for i in range(len(array_polygons)):

        if i == 0:
            new_polygons.append(array_polygons[i])
            continue

        list_x, list_y = list(zip(*new_polygons[i-1]))
        max_point_x = max(list_x)
        new_polygon_list_x, new_polygon_list_y = zip(*array_polygons[i])
        new_polygon_list_x = list(new_polygon_list_x)
        new_polygon_list_y = list(new_polygon_list_y)

        for j in range(len(new_polygon_list_x)):
            new_polygon_list_x[j] = new_polygon_list_x[j] + max_point_x
        new_polygon = list(zip(new_polygon_list_x, new_polygon_list_y))
        new_polygons.append(new_polygon)
    new_polygons_object = []

    for polygon in new_polygons:
        new_polygons_object.append(Polygon.create_polygon(np.array(polygon)))

    Visualizer.plot_polygons(new_polygons_object, "Test initial solution", x_lim, y_lim)


def better_initial_solution(array_polygons, x_lim, y_lim):
    new_polygons = [array_polygons[0]]
    last_polygon_placed = array_polygons[0]
    del array_polygons[0]
    while len(array_polygons) > 0:
        for i in range(len(array_polygons)):
            list_x, list_y = list(zip(last_polygon_placed))
            max_point_y = max(list_y)
            new_polygon_list_x, new_polygon_list_y = zip(*array_polygons[i])
            new_polygon_list_x = list(new_polygon_list_x)
            new_polygon_list_y = list(new_polygon_list_y)
