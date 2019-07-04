import Heuristics
import File
import Polygon
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/shirts.txt")
    polygons_to_plot, limit_y = Heuristics.solve_with_new_heuristic(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.ray_polygon,
        rotate_function=Heuristics.heuristic_highest_side,
        reverse=True)
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()

# Tests with rectangles
# polygon = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (4, 6), (4, 8), (0, 8)]
# polygon2 = [(0, 0), (2, 0), (2, 2), (0, 2)]
# polygon3 = [(0, 0), (6, 0), (6, 2), (0, 2)]
# p_list = [polygon, polygon, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2,
# polygon2, polygon2, polygon3]
