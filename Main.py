import File
import BottomLeft
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/trousers.txt")
    polygons_to_plot, limit_y = BottomLeft.sorted_by_ray_solution(polygons, limit_x)
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instance trousers.txt")
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
