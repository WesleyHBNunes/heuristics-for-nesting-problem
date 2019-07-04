import BottomLeft
import File
import Polygon
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/trousers.txt")
    polygons_to_plot, limit_y = BottomLeft.solve(
        array_polygons=polygons,
        x_lim=limit_x,
        function=BottomLeft.better_solution,
        sort_function=Polygon.rectangle_polygon_area,
        rotate_function=BottomLeft.heuristic_highest_side,
        reverse=True)
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
