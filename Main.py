import File
import BottomLeft
from Visualizer import Visualizer


def main():
    polygons = File.polygons_from_xls("Test/marques.xls", "Marques")
    limits = File.return_limits_of_board_xls("Test/marques.xls", "Marques")
    visualizer = Visualizer(BottomLeft.initial_solution(polygons), 1*limits[0], limits[1], "Title animation plot")
    # visualizer.plot_polygons()
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
