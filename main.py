from citeste_fisier import citeste_rucsac_din_fisier, citeste_tsp_din_fisier
from simulated_annealing import simulated_annealing
from tabu_search import tabu_search


def main():
    rucsac_file = "rucsac-20.txt"  # Numele fișierului cu datele problemei rucsacului
    obiecte, W = citeste_rucsac_din_fisier(rucsac_file)

    tsp_file = "kroC100.tsp"  # Numele fișierului cu datele tsp
    cities = citeste_tsp_din_fisier(tsp_file)

    def afisare_meniu():
        print("Meniu:")
        print("1. Tabu search pentru problema rucsacului")
        print("2. Simulated annealing pentru tsp")
        print("x. Exit")

    while True:
        afisare_meniu()
        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            best_sol, best_val, avg_valid_val, exec_time = tabu_search(obiecte, W, max_iter=1000, tabu_size=5)
            print("Cea mai bună soluție:", best_sol)
            print("Valoarea cea mai bună:", best_val)
            print("Media valorilor valide:", avg_valid_val)
            print("Timpul de execuție al programului:", exec_time, "secunde")
        elif optiune == "2":
            best_sol, best_val, exec_time = simulated_annealing(cities, initial_temperature=1000, cooling_rate=0.99, stopping_temperature=0.1)
            print("Cea mai bună soluție:", best_sol)
            print("Valoarea cea mai bună:", best_val)
            print("Timpul de execuție al programului:", exec_time, "secunde")
        elif optiune == "x":
            break
        else:
            print("Opțiune invalidă! Vă rugăm să selectați din nou.")


if __name__ == "__main__":
    main()
