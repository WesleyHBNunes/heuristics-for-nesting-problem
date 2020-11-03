import Heuristics
import Polygon
# import cProfile
import time
import File
# import Genetic_Algorithm
import os


def main():
    begin = time.time()
    polygons, limit_x = File.polygons_from_txt("Test/albano.txt")
    print("Albano")
    polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
        array_polygons=polygons,
        x_lim=limit_x,
        sort_function=Polygon.rectangle_polygon_area,
        reverse=True)
    # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 15, 50, .25, .25, Polygon.rectangle_polygon_area)
    final_time = time.time() - begin
    print(final_time)
    print(limit_y)
    File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "blaz", final_time)
    os.system("python3 Visualizer_Module/Visualizer.py")
    print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/blaz.txt")
    # print("Blaz")
    # polygons, limit_y = Heuristics.solve_with_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.rectangle_polygon_area,
    #     reverse=True,
    #     rotate_function=Heuristics.heuristic_highest_side)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.rectangle_polygon_area)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "blaz", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/dighe2.txt")
    # print("Dighe2")
    # polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.percent_area_no_used_of_polygon,
    #     reverse=True)
    # # polygons, limit_y = \
    # #     Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.percent_area_no_used_of_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "Dighe2", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/han.txt")
    # print("Han")
    # polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.area_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "han", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/jakobs.txt")
    # print("Jakobs")
    # polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 10, 10, .3, .3, Polygon.area_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "jakobs", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/jakobs2.txt")
    # print("Jakobs2")
    # polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.ray_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 10, 10, .3, .3, Polygon.ray_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "jakobs2", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/mao.txt")
    # print("Mao")
    # polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.area_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "mao", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/marques.txt")
    # print("Marques")
    # polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_no_used_of_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.area_no_used_of_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "marques", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/poly1a.txt")
    # print("poly1a")
    # polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_no_used_of_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 10, .3, .3, Polygon.area_no_used_of_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "poly1a", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/shapes.txt")
    # print("Shapes")
    # polygons, limit_y = Heuristics.solve_with_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_no_used_of_polygon,
    #     reverse=True,
    #     rotate_function=Heuristics.heuristic_highest_side)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 50, .3, .3, Polygon.area_no_used_of_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "shapes", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/shirts.txt")
    # print("Shirts")
    # polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.ray_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 50, .3, .3, Polygon.ray_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "shirts", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/swim.txt")
    # print("Swin")
    # polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 50, .3, .3, Polygon.area_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "swim", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()
    #
    # begin = time.time()
    # polygons, limit_x = File.polygons_from_txt("Test/trousers.txt")
    # print("Trousers")
    # polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
    #     array_polygons=polygons,
    #     x_lim=limit_x,
    #     sort_function=Polygon.area_polygon,
    #     reverse=True)
    # # polygons, limit_y = Genetic_Algorithm.solve(polygons, limit_x, 50, 50, .3, .3, Polygon.area_polygon)
    # final_time = time.time() - begin
    # print(final_time)
    # print(limit_y)
    # File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y, "trousers", final_time)
    # os.system("python3 Visualizer_Module/Visualizer.py")
    # print()


if __name__ == "__main__":
    main()
    # cProfile.run(statement='run()', filename='out.cprof')
