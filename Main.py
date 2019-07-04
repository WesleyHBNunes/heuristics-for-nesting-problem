import BottomLeft
import File
import Polygon
from Visualizer import Visualizer


def main():
    # test()
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


def test():

    polygon = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (4, 6), (4, 8), (0, 8)]
    index = 0
    index_p2 = 1
    polygon2 = [(0, 0), (2, 0), (2, 2), (0, 2)]
    # polygon3 = [(3, 3), (5, 3), (5, 5), (3, 5)]
    polygon4 = [(4, 0), (6, 0), (6, 2), (4, 2)]
    p_list = [polygon, polygon2, polygon4]

    real_ifp = Polygon.return_real_ifp_between_two_polygons(p_list, index, index_p2)
    point = Polygon.return_best_point_in_ifp(real_ifp)

    for point in real_ifp:
        p_list[index_p2] = Polygon.move_polygon_by_reference_point(point[0], p_list[index_p2], (point[1], point[2]))
        visualizer = Visualizer(Polygon.create_polygons_to_plot(p_list), 10, 10, "Test of instances")
        visualizer.plot_animation()
    print(real_ifp)


if __name__ == "__main__":
    main()
