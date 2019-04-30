import File
import BottomLeft
from random import shuffle
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/shirts.txt")
    shuffle(polygons)
    polygons_to_plot, limit_y = BottomLeft.better_initial_solution(polygons, limit_x)
    visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Title animation plot")
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
