import Heuristics
import File
import Polygon
from Visualizer import Visualizer
import time
# import Genetic_Algorithm


def main():
    begin = time.time()
    polygons, limit_x = File.polygons_from_xls("Test/dighe.xls", "Dighe2")
    polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.ray_polygon,
        reverse=True
    )
    # polygons, limit_y = Genetic_Algorithm.generate_individual(polygons, limit_x)
    visualizer = Visualizer(polygons, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    print(time.time() - begin)
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
