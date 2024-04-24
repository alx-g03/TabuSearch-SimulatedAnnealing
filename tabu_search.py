import random
import time


def generare_sol_aleatoare(n):
    return [random.randint(0, 1) for _ in range(n)]


def validare_sol(sol, obiecte, W):
    greutate_totala = sum(sol[i] * obiecte[i][2] for i in range(len(sol)))
    return greutate_totala <= W


def calitate_sol(sol, obiecte):
    return sum(sol[i] * obiecte[i][1] for i in range(len(sol)))


def tabu_search(obiecte, W, max_iter, tabu_size):
    n = len(obiecte)

    current_sol = generare_sol_aleatoare(n)
    current_val = calitate_sol(current_sol, obiecte)
    best_sol = current_sol.copy()
    best_val = current_val
    tabu_list = []
    total_valid_val = 0
    num_valid_solutions = 0

    start_time = time.perf_counter()

    for _ in range(max_iter):
        neighbors = []
        for i in range(n):
            new_sol = current_sol.copy()
            new_sol[i] = 1 - new_sol[i]
            if validare_sol(new_sol, obiecte, W) and (new_sol not in tabu_list or calitate_sol(new_sol, obiecte) > best_val):
                neighbors.append(new_sol)
                total_valid_val += calitate_sol(new_sol, obiecte)
                num_valid_solutions += 1

        if not neighbors:
            continue

        best_neighbor = None
        best_neighbor_val = -float('inf')
        for neighbor in neighbors:
            neighbor_val = calitate_sol(neighbor, obiecte)
            if neighbor_val > best_neighbor_val:
                best_neighbor = neighbor
                best_neighbor_val = neighbor_val

        if best_neighbor_val > current_val or best_neighbor_val == current_val and sum(new_sol) < sum(current_sol):
            current_sol = best_neighbor
            current_val = best_neighbor_val

            if current_val > best_val:
                best_sol = current_sol.copy()
                best_val = current_val

        tabu_list.append(current_sol.copy())
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    avg_valid_val = total_valid_val / num_valid_solutions if num_valid_solutions > 0 else 0

    return best_sol, best_val, avg_valid_val, exec_time
