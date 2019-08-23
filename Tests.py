import Heuristics
import File
from Visualizer import Visualizer
import Polygon
import sys
import os
import time


def main():
    # f = open(os.devnull, 'w')
    # sys.stderr = f
    begin = time.time()
    if len(sys.argv) == 5:
        polygons, limit_x = File.polygons_from_txt(sys.argv[1] + ".txt")
        index_sort_function = int(sys.argv[2])
        index_rotate_function = int(sys.argv[3])
        index_heuristic = int(sys.argv[4])
    else:
        polygons, limit_x = File.polygons_from_xls(sys.argv[1] + ".xls", sys.argv[2])
        index_sort_function = int(sys.argv[3])
        index_rotate_function = int(sys.argv[4])
        index_heuristic = int(sys.argv[5])

    sort_functions = [Polygon.area_polygon, Polygon.area_no_used_of_polygon,
                      Polygon.percent_area_no_used_of_polygon, Polygon.ray_polygon,
                      Polygon.rectangle_polygon_area]
    heuristic = ["Bottom-Left", "New-Heuristic"]
    rotate_function = [Heuristics.heuristic_highest_axis, Heuristics.heuristic_highest_side]
    if index_heuristic == 0:
        polygons_to_plot, limit_y = Heuristics.solve_with_bottom_left(
            array_polygons=polygons,
            x_lim=limit_x,
            sort_function=sort_functions[index_sort_function],
            rotate_function=rotate_function[index_rotate_function],
            reverse=True)
        print("Objective Function: " + str(limit_y))
        print("Time: " + str(time.time() - begin))
    else:
        polygons_to_plot, limit_y = Heuristics.solve_with_new_heuristic(
            array_polygons=polygons,
            x_lim=limit_x,
            sort_function=sort_functions[index_sort_function],
            rotate_function=rotate_function[index_rotate_function],
            reverse=True)
        print("Objective Function: " + str(limit_y))
        print("Time: " + str(time.time() - begin))
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instance: " + sys.argv[1]
                            + "  FO: " + str(limit_y))
    sort_method = str(sort_functions[index_sort_function]).split(' ')[1]
    rotate_method = str(rotate_function[index_rotate_function]).split(' ')[1]
    visualizer.save_fig(heuristic[index_heuristic] + "/" + sys.argv[1] + "_" +
                        sort_method + "_" + rotate_method)


if __name__ == "__main__":
    main()
