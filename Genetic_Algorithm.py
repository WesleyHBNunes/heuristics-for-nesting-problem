import Heuristics
import Polygon
import random
import Placements
import copy

# sort_functions = [Polygon.area_polygon]
placement_functions = [Placements.placement_vertex,
                       Placements.placement_bottom_left_greedy]
rotate_axis = [0, 90]  # 0 == Y, 90 == X


def solve(polygons, x_lim, length_population, iterations, percent_elitism, mutation_value, sort_functions):
    polygons = Polygon.sort(polygons, sort_functions, reverse=True)
    triangles_polygons = Polygon.triangulation_all_polygons(polygons)
    sort_functions = [sort_functions]
    initial_population = generate_initial_population(
        polygons, x_lim, length_population, sort_functions, triangles_polygons)
    current_population = initial_population
    for x in range(iterations):
        n = len(current_population)
        elite = int(percent_elitism * n)
        current_population = current_population[:elite]
        amount_new_individual = n - elite
        new_individuals = generate_individual(current_population, amount_new_individual, mutation_value, polygons,
                                              copy.deepcopy(triangles_polygons), x_lim, sort_functions)
        current_population += new_individuals
        current_population.sort(key=lambda tup: tup[2])
    return current_population[0][0], current_population[0][2]


def generate_individual_initial(polygons, x_lim, sort_functions, triangles_polygons):
    n = len(polygons)
    amount_polygons = - 1
    placed = []
    new_polygons = []
    genome = []
    for i in range(n):
        axis_to_rotate = -1
        place_function = random.randint(0, len(placement_functions) - 1)
        # if random.randint(0, n) <= i:
        #     x = random.randint(0, 2)
        #     if i < n - x:
        #         aux = polygons[i + x]
        #         del (polygons[i + x])
        #         polygons.insert(i, aux)
        next_polygon = polygons[i]
        new_polygons.append(next_polygon)
        amount_polygons += 1
        placed.append(False)
        best_fo = 99999999999
        original_polygon = new_polygons[amount_polygons]
        original_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
        final_polygon = new_polygons[amount_polygons]
        final_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
        for k in range(2):
            for j in range(len(new_polygons[amount_polygons])):
                placed[amount_polygons] = False
                new_polygons[amount_polygons] = original_polygon
                triangles_polygons[amount_polygons] = copy.deepcopy(original_triangle)
                angle = Heuristics.rotate_new_heuristic(
                    (new_polygons[amount_polygons][j][0],
                     new_polygons[amount_polygons][(j + 1) % len(new_polygons[amount_polygons])][0]),
                    (new_polygons[amount_polygons][j][1],
                     new_polygons[amount_polygons][(j + 1) % len(new_polygons[amount_polygons])][1]))
                if k == 0:
                    angle += 90
                new_polygons[amount_polygons] = \
                    Polygon.rotate_polygon(new_polygons[amount_polygons], angle, triangles_polygons[amount_polygons])
                place_polygon(new_polygons,
                              amount_polygons, x_lim, placement_functions[place_function], placed, triangles_polygons)
                placed[amount_polygons] = True
                current_fo = Heuristics.calculate_function_objective(new_polygons, placed)
                if current_fo < best_fo:
                    final_polygon = new_polygons[amount_polygons]
                    final_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
                    best_fo = current_fo
                    axis_to_rotate = angle
                elif current_fo == best_fo:
                    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(new_polygons[amount_polygons])
                    min_x, max_x, min_y, max_y2 = Polygon.min_max_points_polygon(final_polygon)
                    if max_y < max_y2:
                        final_polygon = new_polygons[amount_polygons]
                        final_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
        new_polygons[amount_polygons] = final_polygon
        triangles_polygons[amount_polygons] = copy.deepcopy(final_triangle)
        # new_polygons[amount_polygons] = \
        #     place_polygon(new_polygons, amount_polygons, x_lim, placement_functions[place_function], placed)
        new_polygons[amount_polygons] = \
            Heuristics.slide_polygon(new_polygons, placed, amount_polygons, x_lim, triangles_polygons)
        placed[amount_polygons] = True
        genome.append((sort_functions, place_function, axis_to_rotate))
    return new_polygons, genome, Heuristics.calculate_function_objective(new_polygons, placed), triangles_polygons


def generate_initial_population(polygons, x_lim, length_population, sort_functions, triangles_polygons):
    population = []
    for i in range(length_population):
        triangles_copy = copy.deepcopy(triangles_polygons)
        individual, genome, fo_individual, triangles_copy = generate_individual_initial(polygons, x_lim, sort_functions,
                                                                                        triangles_copy)
        population.append((individual, genome, fo_individual, triangles_copy))
    population.sort(key=lambda tup: tup[2])
    return population


def return_next_polygon(polygons, function_to_sort):
    polygons = Polygon.sort(polygons, function_to_sort, True)
    return polygons.pop(0), polygons


def place_polygon(new_polygons, amount_polygons, x_lim, sort_function, placed, triangles):
    if sort_function == Placements.placement_bottom_left_slide:
        return Placements.placement_bottom_left_slide(new_polygons, amount_polygons, x_lim, placed, triangles)
    elif sort_function == Placements.placement_bottom_left:
        aux = copy.deepcopy(new_polygons)
        return Placements.placement_bottom_left(
            aux, amount_polygons, x_lim, new_polygons[:len(new_polygons) - 1], triangles)
    elif sort_function == Placements.placement_greedy:
        return Placements.placement_greedy(new_polygons, amount_polygons, x_lim, placed, triangles)
    elif sort_function == Placements.placement_vertex:
        return Placements.placement_vertex(new_polygons, amount_polygons, x_lim, placed, triangles)
    elif sort_function == Placements.placement_bottom_left_greedy:
        return Placements.placement_bottom_left_greedy(new_polygons, amount_polygons, x_lim, placed, triangles)
    return new_polygons[amount_polygons]


def generate_individual(current_population, amount_new_individual,
                        mutation_value, original_polygons, original_triangles, x_lim, sort_functions):
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
                new_genome[j] = make_mutation(new_genome[j], sort_functions)
        new_individual = apply_changes(new_genome, original_polygons, x_lim, original_triangles)
        new_individuals.append(new_individual)
    return new_individuals


def apply_changes(genome, polygons, x_lim, triangles_polygons):
    n = len(polygons)
    amount_polygons = - 1
    placed = []
    new_polygons = []
    for i in range(n):
        place_function = genome[i][1]
        # if random.randint(0, n) <= i:
        #     x = random.randint(0, 2)
        #     if i < n - x:
        #         aux = polygons[i + x]
        #         del (polygons[i + x])
        #         polygons.insert(i, aux)
        next_polygon = polygons[i]
        new_polygons.append(next_polygon)
        amount_polygons += 1
        placed.append(False)
        placed.append(False)
        best_fo = 99999999999
        original_polygon = new_polygons[amount_polygons]
        original_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
        final_polygon = new_polygons[amount_polygons]
        final_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
        for k in range(2):
            for j in range(len(new_polygons[amount_polygons])):
                placed[amount_polygons] = False
                new_polygons[amount_polygons] = original_polygon
                triangles_polygons[amount_polygons] = copy.deepcopy(original_triangle)
                angle = Heuristics.rotate_new_heuristic(
                    (new_polygons[amount_polygons][j][0],
                     new_polygons[amount_polygons][(j + 1) % len(new_polygons[amount_polygons])][0]),
                    (new_polygons[amount_polygons][j][1],
                     new_polygons[amount_polygons][(j + 1) % len(new_polygons[amount_polygons])][1]))
                if k == 0:
                    angle += 90
                new_polygons[amount_polygons] = \
                    Polygon.rotate_polygon(new_polygons[amount_polygons], angle, triangles_polygons[amount_polygons])
                place_polygon(new_polygons,
                              amount_polygons, x_lim, placement_functions[place_function], placed, triangles_polygons)
                placed[amount_polygons] = True
                current_fo = Heuristics.calculate_function_objective(new_polygons, placed)
                if current_fo < best_fo:
                    final_polygon = new_polygons[amount_polygons]
                    final_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
                    best_fo = current_fo
                elif current_fo == best_fo:
                    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(new_polygons[amount_polygons])
                    min_x, max_x, min_y, max_y2 = Polygon.min_max_points_polygon(final_polygon)
                    if max_y < max_y2:
                        final_polygon = new_polygons[amount_polygons]
                        final_triangle = copy.deepcopy(triangles_polygons[amount_polygons])
        new_polygons[amount_polygons] = final_polygon
        triangles_polygons[amount_polygons] = copy.deepcopy(final_triangle)
        # new_polygons[amount_polygons] = \
        #     place_polygon(new_polygons, amount_polygons, x_lim, placement_functions[place_function], placed)
        new_polygons[amount_polygons] = \
            Heuristics.slide_polygon(new_polygons, placed, amount_polygons, x_lim, triangles_polygons)
        placed[amount_polygons] = True
    return new_polygons, genome, Heuristics.calculate_function_objective(new_polygons, placed), triangles_polygons


def make_mutation(genome, sort_functions):
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
