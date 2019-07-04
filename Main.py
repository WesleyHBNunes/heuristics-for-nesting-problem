import BottomLeft
import File
import Polygon
from Visualizer import Visualizer


def main():
    test()
    # polygons, limit_x = File.polygons_from_txt("Test/trousers.txt")
    # polygons_to_plot, limit_y = BottomLeft.solve(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     function=BottomLeft.solution,
    #     sort_function=Polygon.rectangle_polygon_area,
    #     rotate_function=BottomLeft.heuristic_highest_side,
    #     reverse=True)
    # visualizer = Visualizer(polygons_to_plot, limit_x, limit_y, "Test of instances")
    # print(limit_y)
    # # visualizer.plot_polygons()
    # visualizer.plot_animation()


def test():
    # polygon = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (4, 6), (4, 8), (0, 8)]
    # polygon2 = [(0, 0), (2, 0), (2, 2), (0, 2)]
    # polygon3 = [(0, 0), (6, 0), (6, 2), (0, 2)]
    # p_list = [polygon, polygon, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2,
    #           polygon2, polygon2, polygon3]
    p_list, limit_x = File.polygons_from_txt("Test/shirts.txt")
    p_list = Polygon.sort(p_list, Polygon.ray_polygon, reverse=True)
    placed = [False for _ in range(len(p_list))]
    for i in range(len(p_list)):
        print(i)
        p_list[i] = BottomLeft.rotate_polygon_heuristic(p_list[i], BottomLeft.heuristic_highest_side)
        p_list[i] = Polygon.decide_best_position(p_list, i, limit_x, placed)
        placed[i] = True
    limit_y = BottomLeft.return_line_y(p_list)
    print(limit_y)
    visualizer = Visualizer(Polygon.create_polygons_to_plot(p_list),
                            limit_x, BottomLeft.return_line_y(p_list), "Test of instances")
    visualizer.plot_animation()


if __name__ == "__main__":
    main()
