import File
import BottomLeft


def main():
    polygons = File.polygons_from_xls("Test/marques.xls", "Marques")
    BottomLeft.initial_solution(polygons)


if __name__ == "__main__":
    main()
