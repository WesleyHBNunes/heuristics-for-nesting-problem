import File
import BottomLeft
from random import shuffle
from Visualizer import Visualizer


def main():
    polygons, limits = File.polygons_from_xls("Test/han.xls", "Han")
    shuffle(polygons)
    visualizer = Visualizer(BottomLeft.better_initial_solution(polygons, limits[0]),
                            limits[0], limits[1], "Title animation plot")
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
