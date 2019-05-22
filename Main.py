import BottomLeft
import File
import Polygon
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/trousers.txt")
    polygons_to_plot, limit_y = BottomLeft.solve(polygons, limit_x, BottomLeft.better_solution,
                                                 Polygon.percent_area_no_used_of_polygon, True)
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
