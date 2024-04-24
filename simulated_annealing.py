import random
import math
import time


def generate_random_solution(num_cities):
    cities = list(range(1, num_cities + 1))
    random.shuffle(cities)
    return cities


def calculate_distance(city1, city2):
    x1, y1 = city1[1], city1[2]
    x2, y2 = city2[1], city2[2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def tsp_fitness(solution, cities):
    total_distance = 0.0
    num_cities = len(solution)
    for i in range(num_cities):
        current_city = cities[solution[i] - 1]
        next_city = cities[solution[(i + 1) % num_cities] - 1]
        total_distance += calculate_distance(current_city, next_city)
    return total_distance


def two_opt_swap(solution):
    new_solution = solution[:]

    i, j = random.sample(range(len(solution)), 2)
    i, j = min(i, j), max(i, j)

    new_solution[i:j+1] = reversed(new_solution[i:j+1])

    return new_solution


def simulated_annealing(cities, initial_temperature, cooling_rate, stopping_temperature):
    current_solution = generate_random_solution(len(cities))
    current_value = tsp_fitness(current_solution, cities)
    best_solution = current_solution
    best_value = current_value
    temperature = initial_temperature

    start_time = time.perf_counter()

    while temperature > stopping_temperature:
        neighbor_solution = two_opt_swap(current_solution)
        neighbor_value = tsp_fitness(neighbor_solution, cities)
        delta = neighbor_value - current_value

        if delta > 0 or random.random() < math.exp(delta / temperature):
            current_solution = neighbor_solution
            current_value = neighbor_value

            if current_value > best_value:
                best_solution = current_solution
                best_value = current_value

        temperature *= cooling_rate

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    return best_solution, best_value, exec_time
