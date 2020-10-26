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


def polygons_from_txt_result(file_name):
    file = open(file_name, "r")
    instance = file.readline()
    line = file.readline()
    array_polygons = []
    amount_polygons = 0
    while line != "#":
        if line == "QUANTITY":
            amount_polygons = int(file.readline())
            line = amount_polygons
        elif line == "VERTICES (X,Y)":
            line = file.readline()
            array_points_tuple = []
            while line != "\n":
                points = line.split()
                array_points_tuple.append((float(points[0]), float(points[1])))
                line = file.readline()
            array_points_tuple = set_points_to_positive(array_points_tuple)
            for i in range(amount_polygons):
                array_polygons.append(array_points_tuple)
        else:
            line = file.readline().strip()
    file.close()
    x, y, time = return_limits_of_board_txt_result(file_name)
    return array_polygons, x, y, instance.split()[0], time


def return_limits_of_board_txt_result(file_name):
    file = open(file_name, "r")
    file.readline()
    line = file.readline()
    line = line.split()
    x_lim = float(line[0])
    y_result = float(line[1])
    time = float(line[2])
    file.close()
    return x_lim, y_result, time
