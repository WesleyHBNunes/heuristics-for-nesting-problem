import Heuristics
import File
import Polygon
import random
from Visualizer import Visualizer


def main():
    polygons, limit_x = File.polygons_from_txt("Test/blaz.txt")
    random.shuffle(polygons)
    polygons, limit_y = Heuristics.solve_with_new_heuristic(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.ray_polygon,
        reverse=True)
    visualizer = Visualizer(polygons, limit_x, limit_y, "Test of instances")
    print(limit_y)
    # visualizer.plot_polygons()
    visualizer.plot_animation()


# def main():
#     best_fo = 99999999
#     best_solution = None
#     limit_x = 0
#     for i in range(100):
#         polygons, limit_x = File.polygons_from_txt("Test/blaz.txt")
#         random.shuffle(polygons)
#         polygons, limit_y = Heuristics.solve_with_new_heuristic(
#             array_polygons=polygons,
#             x_lim=limit_x,
#             sort_function=Polygon.ray_polygon,
#             reverse=True)
#         print(str(i) + " " + str(limit_y))
#         if limit_y < best_fo:
#             best_fo = limit_y
#             best_solution = polygons
#     visualizer = Visualizer(best_solution, limit_x, best_fo, "Test of instances")
#     print()
#     print(best_fo)
#     # visualizer.plot_polygons()
#     visualizer.plot_animation()

if __name__ == "__main__":
    main()

# Tests with rectangles
# polygon = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (4, 6), (4, 8), (0, 8)]
# polygon2 = [(0, 0), (2, 0), (2, 2), (0, 2)]
# polygon3 = [(0, 0), (6, 0), (6, 2), (0, 2)]
# p_list = [polygon, polygon, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2, polygon2,
# polygon2, polygon2, polygon3]
# limit_x = 10
