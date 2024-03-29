# from pyexcel_xls import get_data
import Polygon

# CONSTS
COLUMN_LINE_WIDTH_DATA = 3
INITIAL_LINE_POINTS_DATA = 5


# def polygons_from_xls(file_name, sheet):
#     data = get_data(file_name)
#     array_polygons = []
#     array_points_x = []
#     array_points_y = []
#     for i in range(INITIAL_LINE_POINTS_DATA, len(data[sheet])):
#         for j in range(len(data[sheet][i])):
#             if data[sheet][i][j] == "x":
#                 amount_polygons = data[sheet][i][j - 1]
#                 j = j + 1
#                 while j < len(data[sheet][i]):
#                     array_points_x.append(data[sheet][i][j])
#                     array_points_y.append(data[sheet][i + 1][j])
#                     j = j + 1
#                 i = i + 1
#                 array_points_tuple = list(zip(array_points_x, array_points_y))
#                 array_points_tuple = Polygon.set_points_to_positive(array_points_tuple)
#                 array_points_x = []
#                 array_points_y = []
#                 for _ in range(amount_polygons):
#                     array_polygons.append(array_points_tuple)
#     return array_polygons, return_limits_of_board_xls(file_name, sheet)


def polygons_from_txt(file_name):
    file = open(file_name, "r")
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
            array_points_tuple = Polygon.set_points_to_positive(array_points_tuple)
            for i in range(amount_polygons):
                array_polygons.append(array_points_tuple)
        else:
            line = file.readline().strip()
    file.close()
    return array_polygons, return_limits_of_board_txt(file_name)


def polygons_from_txt_result(file_name):
    file = open(file_name, "r")
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
            array_points_tuple = Polygon.set_points_to_positive(array_points_tuple)
            for i in range(amount_polygons):
                array_polygons.append(array_points_tuple)
        else:
            line = file.readline().strip()
    file.close()
    x, y = return_limits_of_board_txt_result(file_name)
    return array_polygons, x, y


def export_polygons_to_txt(name, polygons, limit_x):
    f = open(name + ".txt", "w")
    f.write(str(limit_x) + "\n")
    for i in range(len(polygons)):
        f.write("PIECE " + str(i + 1) + "\n")
        f.write("QUANTITY\n")
        f.write("1\n")
        f.write("NUMBER OF VERTICES\n")
        f.write(str(len(polygons[i])) + "\n")
        f.write("VERTICES (X,Y)\n")
        for p in polygons[i]:
            f.write(str(p[0]) + "    " + str(p[1]) + "\n")
        f.write("\n")
    f.write("#")


def export_polygons_to_txt_result(name, polygons, limit_x, y_result, instance, time):
    f = open(name + ".txt", "w")
    f.write(instance + "\n")
    f.write(str(limit_x) + "    " + str(y_result) + "    " + str(time) + "\n")
    for i in range(len(polygons)):
        f.write("PIECE " + str(i + 1) + "\n")
        f.write("QUANTITY\n")
        f.write("1\n")
        f.write("NUMBER OF VERTICES\n")
        f.write(str(len(polygons[i])) + "\n")
        f.write("VERTICES (X,Y)\n")
        for p in polygons[i]:
            f.write(str(p[0]) + "    " + str(p[1]) + "\n")
        f.write("\n")
    f.write("#")
    f.close()

# def return_limits_of_board_xls(file_name, sheet):
#     data = get_data(file_name)
#     x_lim = float(data[sheet][COLUMN_LINE_WIDTH_DATA][COLUMN_LINE_WIDTH_DATA])
#     return x_lim


def return_limits_of_board_txt(file_name):
    file = open(file_name, "r")
    line = file.readline()
    x_lim = float(line)
    file.close()
    return x_lim


def return_limits_of_board_txt_result(file_name):
    file = open(file_name, "r")
    line = file.readline()
    line = line.split()
    x_lim = float(line[0])
    y_result = float(line[1])
    file.close()
    return x_lim, y_result
