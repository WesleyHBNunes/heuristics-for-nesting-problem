import Heuristics
import Genetic_Algorithm
import File
import Polygon
import time
import os
# import sys

GENERATIONS = 50
INDIVIDUALS = 15
MUTATION_PERCENT = .25
ELITISM_PERCENT = .25


def main():
    all_instances = ["albano", "blaz", "dighe2", "han", "jakobs", "jakobs2", "mao", "marques", "poly1a", "shapes",
                     "shirts", "trousers"]

    sort_functions = [Polygon.area_polygon, Polygon.area_no_used_of_polygon, Polygon.rectangle_polygon_area,
                      Polygon.ray_polygon, Polygon.percent_area_no_used_of_polygon]

    rotate_function = [Heuristics.heuristic_highest_axis, Heuristics.heuristic_highest_side]

    print("Bottom-Left")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            for j in range(len(rotate_function)):
                begin = time.time()
                polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
                polygons, limit_y = Heuristics.solve_with_bottom_left(
                    array_polygons=polygons,
                    x_lim=limit_x,
                    sort_function=sort_functions[i],
                    reverse=True,
                    rotate_function=rotate_function[j])
                final_time = time.time() - begin
                File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                                   instance, final_time)
                string_sort_function = str(sort_functions[i]).split()[1]
                string_rotate_function = str(rotate_function[j]).split()[1]
                os.system("python3 Visualizer_Module/Visualizer.py " + "Bottom-Left " +
                          string_sort_function + " " + string_rotate_function)
        print()

    print("Bottom-Left-Greedy")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            begin = time.time()
            polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
            polygons, limit_y = Heuristics.solve_with_bottom_left_greedy(
                array_polygons=polygons,
                x_lim=limit_x,
                sort_function=sort_functions[i],
                reverse=True)
            final_time = time.time() - begin
            File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                               instance, final_time)
            string_sort_function = str(sort_functions[i]).split()[1]
            os.system("python3 Visualizer_Module/Visualizer.py " + "Bottom-Left-Greedy " + string_sort_function)
        print()

    print("Bottom-Left-Slide")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            for j in range(len(rotate_function)):
                begin = time.time()
                polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
                polygons, limit_y = Heuristics.solve_with_bottom_left_slide(
                    array_polygons=polygons,
                    x_lim=limit_x,
                    sort_function=sort_functions[i],
                    reverse=True,
                    rotate_function=rotate_function[j])
                final_time = time.time() - begin
                File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                                   instance, final_time)
                string_sort_function = str(sort_functions[i]).split()[1]
                string_rotate_function = str(rotate_function[j]).split()[1]
                os.system("python3 Visualizer_Module/Visualizer.py " + "Bottom-Left-Slide " +
                          string_sort_function + " " + string_rotate_function)
        print()

    print("Greedy")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            for j in range(len(rotate_function)):
                begin = time.time()
                polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
                polygons, limit_y = Heuristics.solve_with_greedy(
                    array_polygons=polygons,
                    x_lim=limit_x,
                    sort_function=sort_functions[i],
                    reverse=True,
                    rotate_function=rotate_function[j])
                final_time = time.time() - begin
                File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                                   instance, final_time)
                string_sort_function = str(sort_functions[i]).split()[1]
                string_rotate_function = str(rotate_function[j]).split()[1]
                os.system("python3 Visualizer_Module/Visualizer.py " + "Greedy " +
                          string_sort_function + " " + string_rotate_function)
        print()

    print("New-Heuristic-Modified")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            begin = time.time()
            polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
            polygons, limit_y = Heuristics.solve_with_new_heuristic_modified(
                array_polygons=polygons,
                x_lim=limit_x,
                sort_function=sort_functions[i],
                reverse=True)
            final_time = time.time() - begin
            File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                               instance, final_time)
            string_sort_function = str(sort_functions[i]).split()[1]
            os.system("python3 Visualizer_Module/Visualizer.py " + "New-Heuristic-Modified " + string_sort_function)
        print()

    print("Heuristic_Multiples_Placements")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            begin = time.time()
            polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
            polygons, limit_y = Heuristics.solve_with_heuristic_multiples_placements(
                array_polygons=polygons,
                x_lim=limit_x,
                sort_function=sort_functions[i],
                reverse=True)
            final_time = time.time() - begin
            File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                               instance, final_time)
            string_sort_function = str(sort_functions[i]).split()[1]
            os.system("python3 Visualizer_Module/Visualizer.py " +
                      "Heuristic_Multiples_Placemeychnts " + string_sort_function)
        print()

    print("Heuristic_Multiples_Placements_Random")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            begin = time.time()
            polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
            polygons, limit_y = Heuristics.solve_with_heuristic_multiples_placements_random(
                array_polygons=polygons,
                x_lim=limit_x,
                sort_function=sort_functions[i],
                reverse=True,
                iteration=10000)
            final_time = time.time() - begin
            File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                               instance, final_time)
            string_sort_function = str(sort_functions[i]).split()[1]
            heuristic = "Heuristic_Multiples_Placements_Random"
            os.system("python3 Visualizer_Module/Visualizer.py " + heuristic + " "
                      + string_sort_function)
        print()

    print("Genetic-Algorithm")
    for instance in all_instances:
        print(instance)
        for i in range(len(sort_functions)):
            begin = time.time()
            polygons, limit_x = File.polygons_from_txt("Test/" + instance + ".txt")
            polygons, limit_y = Genetic_Algorithm.solve(
                polygons, limit_x, INDIVIDUALS, GENERATIONS, ELITISM_PERCENT, MUTATION_PERCENT, sort_functions[i])
            final_time = time.time() - begin
            File.export_polygons_to_txt_result("Visualizer_Module/polygons", polygons, limit_x, limit_y,
                                               instance, final_time)
            string_sort_function = str(sort_functions[i]).split()[1]
            os.system("python3 Visualizer_Module/Visualizer.py " + "Genetic-Algorithm " + string_sort_function)
        print()


if __name__ == "__main__":
    main()
