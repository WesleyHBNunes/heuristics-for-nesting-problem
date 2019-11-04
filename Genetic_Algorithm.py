import Heuristics
import Polygon
import random
import Placements
import copy

sort_functions = [Polygon.area_polygon, Polygon.area_no_used_of_polygon,
                  Polygon.percent_area_no_used_of_polygon, Polygon.ray_polygon,
                  Polygon.rectangle_polygon_area]
placement_functions = [Placements.placement_bottom_left, Placements.placement_bottom_left_slide,
                       Placements.placement_greedy, Placements.placement_vertex]
rotate_axis = [0, 90]  # 0 == Y, 90 == X


def solve(polygons, x_lim, length_population, iterations):
    initial_population = generate_initial_population(polygons, x_lim, length_population)
    return initial_population[0][0], initial_population[0][1]


def generate_individual(polygons, x_lim):
    n = len(polygons)
    amount_polygons = - 1
    placed = []
    new_polygons = []
    genome = []
    for i in range(n):
        sort_function = random.randint(0, len(sort_functions) - 1)
        place_function = random.randint(0, len(placement_functions) - 1)
        axis_to_rotate = random.randint(0, len(rotate_axis) - 1)
        next_polygon, polygons = return_next_polygon(polygons, sort_functions[sort_function])
        new_polygons.append(next_polygon)
        amount_polygons += 1
        edge_to_rotate = random.randint(0, len(next_polygon) - 1)
        new_polygons[amount_polygons] = \
            rotate_polygon(new_polygons[amount_polygons], edge_to_rotate, rotate_axis[axis_to_rotate])
        placed.append(False)
        new_polygons[amount_polygons] = \
            place_polygon(new_polygons, amount_polygons, x_lim, placement_functions[place_function], placed)
        new_polygons[amount_polygons] = Heuristics.slide_polygon(new_polygons, placed, amount_polygons, x_lim)
        placed[amount_polygons] = True
        genome.append((sort_function, place_function, axis_to_rotate, edge_to_rotate))
    return new_polygons, Heuristics.calculate_function_objective(new_polygons, placed), genome


def generate_initial_population(polygons, x_lim, length_population):
    population = []
    for i in range(length_population):
        individual, fo_individual, genome = generate_individual(polygons, x_lim)
        population.append((individual, genome, fo_individual))
    population.sort(key=lambda tup: tup[2])
    return population


def return_next_polygon(polygons, function_to_sort):
    polygons = Polygon.sort(polygons, function_to_sort, True)
    return polygons.pop(0), polygons


def place_polygon(new_polygons, amount_polygons, x_lim, sort_function, placed):
    if sort_function == Placements.placement_bottom_left_slide:
        return Placements.placement_bottom_left_slide(new_polygons, amount_polygons, x_lim, placed)
    elif sort_function == Placements.placement_bottom_left:
        aux = copy.deepcopy(new_polygons)
        return Placements.placement_bottom_left(aux, amount_polygons, x_lim, new_polygons[:len(new_polygons) - 1])
    elif sort_function == Placements.placement_greedy:
        return Placements.placement_greedy(new_polygons, amount_polygons, x_lim, placed)
    elif sort_function == Placements.placement_vertex:
        return Placements.placement_vertex(new_polygons, amount_polygons, x_lim, placed)
    return new_polygons[amount_polygons]


def rotate_polygon(polygon, edge_to_rotate, axis):
    points_x = (polygon[edge_to_rotate][0], polygon[(edge_to_rotate + 1) % len(polygon)][0])
    points_y = (polygon[edge_to_rotate][1], polygon[(edge_to_rotate + 1) % len(polygon)][1])
    angle = Heuristics.rotate_new_heuristic(points_x, points_y) + axis
    return Polygon.rotate_polygon(polygon, angle)
