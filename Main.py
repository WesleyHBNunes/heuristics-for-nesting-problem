import Heuristics
import Polygon
# import cProfile
import time
import File
# import Genetic_Algorithm
import os


def main():
    begin = time.time()
    polygons, limit_x = File.polygons_from_txt("Test/blaz.txt")
    print("Blaz")
    polygons, limit_y = Heuristics.solve_with_greedy(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.rectangle_polygon_area,
        reverse=True,
        rotate_function=Heuristics.heuristic_highest_side)
    # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.rectangle_polygon_area)
    final_time = time.time() - begin
    print(final_time)
    print(limit_y)
    File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "blaz", final_time)
    os.system("python3 Visualizer_Module/Visualizer.py")
    print()


if __name__ == "__main__":
    main()
    # cProfile.run(statement='run()', filename='out.cprof')
