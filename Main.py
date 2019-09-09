import Heuristics
import File
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/blaz.txt")
    polygons, limit_y = Heuristics.solve_with_new_heuristic_modified_random(
        array_polygons=polygons,
        x_lim=limit_x,
        iteration=5)
    visualizer = Visualizer(polygons, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
