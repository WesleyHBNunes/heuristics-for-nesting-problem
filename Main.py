import File
import BottomLeft
import Polygon
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/trousers.txt")
    polygons = Polygon.sort_by_area(polygons)
    polygons_to_plot, limit_y = BottomLeft.better_initial_solution(polygons, limit_x)
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instance trousers.txt")
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
