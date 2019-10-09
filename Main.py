import Heuristics
import File
import Polygon
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_xls("Test/marques.xls", "Marques")
    polygons, limit_y = Heuristics.solve_with_greedy(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.ray_polygon,
        reverse=True,
        rotate_function=Heuristics.heuristic_highest_axis
    )
    visualizer = Visualizer(polygons, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
