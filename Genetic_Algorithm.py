import Heuristics
import Polygon
import random
import Placements
import copy

sort_functions = [Polygon.area_polygon, Polygon.area_no_used_of_polygon,
                  Polygon.percent_area_no_used_of_polygon, Polygon.ray_polygon,
                  Polygon.rectangle_polygon_area]
placement_functions = [Placements.placement_bottom_left, Placements.placement_bottom_left_slide,
                       Placements.placement_greedy, Placements.placement_vertex, Placements.placement_bottom_left_greedy]
rotate_axis = [0, 90]  # 0 == Y, 90 == X


def solve(polygons, x_lim, length_population, iterations, percent_elitism, mutation_value):
    initial_population = generate_initial_population(polygons, x_lim, length_population)
    current_population = initial_population
    for _ in range(iterations):
        n = len(current_population)
        elite = int(percent_elitism * n)
        current_population = current_population[:elite]
        amount_new_individual = n - elite
        new_individuals = \
            generate_individual(current_population, amount_new_individual, mutation_value, polygons, x_lim)
        current_population += new_individuals
        current_population.sort(key=lambda tup: tup[2])
    return current_population[0][0], current_population[0][2]


def generate_individual_initial(polygons, x_lim):
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
        genome.append((sort_function, place_function, axis_to_rotate))
    return new_polygons, genome, Heuristics.calculate_function_objective(new_polygons, placed)


def generate_initial_population(polygons, x_lim, length_population):
    population = []
    for i in range(length_population):
        individual, genome, fo_individual = generate_individual_initial(polygons, x_lim)
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
    elif sort_function == Placements.placement_bottom_left_greedy:
        return Placements.placement_bottom_left_greedy(new_polygons, amount_polygons, x_lim, placed)
    return new_polygons[amount_polygons]


def rotate_polygon(polygon, edge_to_rotate, axis):
    points_x = (polygon[edge_to_rotate][0], polygon[(edge_to_rotate + 1) % len(polygon)][0])
    points_y = (polygon[edge_to_rotate][1], polygon[(edge_to_rotate + 1) % len(polygon)][1])
    angle = Heuristics.rotate_new_heuristic(points_x, points_y) + axis
    return Polygon.rotate_polygon(polygon, angle)


def generate_individual(current_population, amount_new_individual, mutation_value, original_polygons, x_lim):
    new_individuals = []
    for i in range(amount_new_individual):
        father = random.randint(0, len(current_population) - 1)
        mother = random.randint(0, len(current_population) - 1)
        father = current_population[father]
        mother = current_population[mother]
        new_genome = []
        length_new_individual = len(current_population[0][0])
        for j in range(length_new_individual):
            random_number = random.randint(0, 1)
            if random_number == 0:
                new_genome.append(mother[1][j])
            else:
                new_genome.append(father[1][j])
            mutation_chance = random.uniform(0, 1)
            if mutation_chance < mutation_value:
                new_genome[j] = make_mutation(new_genome[j])
        new_individual = apply_changes(new_genome, original_polygons, x_lim)
        new_individuals.append(new_individual)
    return new_individuals


def apply_changes(genome, polygons, x_lim):
    n = len(polygons)
    amount_polygons = - 1
    placed = []
    new_polygons = []
    for i in range(n):
        sort_function = genome[i][0]
        place_function = genome[i][1]
        axis_to_rotate = genome[i][2]
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
    return new_polygons, genome, Heuristics.calculate_function_objective(new_polygons, placed)


def make_mutation(genome):
    index_of_genome = random.randint(0, 2)
    if index_of_genome == 0:
        sort_function = random.randint(0, len(sort_functions) - 1)
        new_genome = (sort_function, genome[1], genome[2])
        return new_genome
    elif index_of_genome == 1:
        place_function = random.randint(0, len(placement_functions) - 1)
        new_genome = (genome[0], place_function, genome[2])
        return new_genome
    elif index_of_genome == 2:
        axis_to_rotate = random.randint(0, len(rotate_axis) - 1)
        new_genome = (genome[0], genome[1], axis_to_rotate)
        return new_genome
    return None
