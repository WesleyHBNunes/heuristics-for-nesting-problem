import File
import BottomLeft


def main():
    polygons = File.polygons_from_xls("Test/marques.xls", "Marques")
    limits = File.return_limits_of_board_xls("Test/marques.xls", "Marques")
    BottomLeft.initial_solution(polygons, limits[0], limits[1])

    # BottomLeft.better_initial_solution(polygons, limits[0], limits[1])


if __name__ == "__main__":
    main()
