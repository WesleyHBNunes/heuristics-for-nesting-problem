import Heuristics
import File
import Polygon
import sys
import time


def main():
    begin = time.time()
    if len(sys.argv) == 4:
        polygons, limit_x = File.polygons_from_txt(sys.argv[1])
        index_sort_function = int(sys.argv[2])
        index_rotate_function = int(sys.argv[3])
    else:
        polygons, limit_x = File.polygons_from_xls(sys.argv[1], sys.argv[2])
        index_sort_function = int(sys.argv[3])
        index_rotate_function = int(sys.argv[4])

    sort_functions = [Polygon.area_polygon, Polygon.area_no_used_of_polygon,
                      Polygon.percent_area_no_used_of_polygon, Polygon.ray_polygon,
                      Polygon.rectangle_polygon_area]

    rotate_function = [Heuristics.heuristic_highest_axis, Heuristics.heuristic_highest_side]
    polygons_to_plot, limit_y = Heuristics.solve_with_bottom_left(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=sort_functions[index_sort_function],
        rotate_function=rotate_function[index_rotate_function],
        reverse=True)
    print("Objective Function: " + str(limit_y))
    print("Time: " + str(time.time() - begin))


if __name__ == "__main__":
    main()
