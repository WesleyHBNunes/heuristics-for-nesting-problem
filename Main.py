import Heuristics
import Polygon
import cProfile
import time
import File
import Genetic_Algorithm
from Visualizer import Visualizer


def main():
    begin = time.time()
    polygons, limit_x = File.polygons_from_xls("Test/dighe.xls", "Dighe2")
    polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.ray_polygon,
        reverse=True
    )
    # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 10, 10)
    visualizer = Visualizer(polygons, limit_x, limit_y, "Test of instances")
    print(limit_y)
    print(time.time() - begin)
    visualizer.plot_animation()


def run():
    polygons, limit_x = File.polygons_from_xls("Test/marques.xls", "Marques")
    polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.area_polygon,
        reverse=True
    )
    # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 10, 10)
    print(limit_y)


if __name__ == "__main__":
    main()
    # cProfile.run(statement='run()', filename='out.cprof')
