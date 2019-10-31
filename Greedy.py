import Heuristics
import Polygon


def solve(array_polygons, x_lim, sort_function, rotate_function, reverse):
    if x_lim > 1000:
        jump = 10
    else:
        jump = 1
    array_polygons = Polygon.sort(array_polygons, sort_function, reverse)
    new_polygons = []
    placed = [False for _ in array_polygons]
    for i in range(len(array_polygons)):
        array_polygons[i] = Heuristics.rotate_polygon_heuristic(array_polygons[i], rotate_function)
        if i == 0:
            new_polygons.append(array_polygons[i])
            placed[i] = True
            continue
        overlapping = True
        while overlapping:
            array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], jump, 0)
            list_x, list_y = list(zip(*array_polygons[i]))
            max_point_x = max(list_x)
            min_point_x = min(list_x)
            if max_point_x > x_lim:
                array_polygons[i] = Polygon.add_number_axis_x_y(array_polygons[i], -min_point_x, jump)
            for j in range(len(array_polygons)):
                overlapping = False
                if placed[j] and i != j:
                    if Polygon.is_overlapping(array_polygons[i], array_polygons[j]):
                        overlapping = True
                        break

        array_polygons[i] = Heuristics.slide_polygon(array_polygons, placed, i)
        new_polygons.append(array_polygons[i])
        placed[i] = True

    return new_polygons, Heuristics.calculate_function_objective(array_polygons, placed)
