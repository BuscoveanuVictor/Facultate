def citeste_graf(nume_fisier):
    with open(nume_fisier) as f:
        n, m = map(int, f.readline().split())
        muchii = []
        for _ in range(m):
            i, j, cost = map(int, f.readline().split())
            muchii.append((i, j, cost))
    return n, m, muchii

def bellman_ford(n, muchii, start):
    # Initializare
    distante = [float('inf')] * (n + 1)
    # Marcam nodul de start cu distanta 0
    # ca la prima iteratie sa putem relaxa muchiile
    distante[start] = 0
    parinti = [-1] * (n + 1)
    
    distante_initiale = []
    for _ in range(n - 1):
        # La fiecare iteratie in final vor fi relaxate toate muchiile
        for u, v, cost in muchii:
            # La fiecare iteratie se relaxeaza muchiile pe rand
            # si se actualizeaza lista de distante
            if distante[u] != float('inf') and distante[u] + cost < distante[v]:
                distante[v] = distante[u] + cost
                parinti[v] = u
        # La prima iteratie, salvam distante
        if distante_initiale == []:
            distante_initiale = distante
        # Daca distante nu se modifica, atunci algoritmul se opreste
        if distante == distante_initiale:
            break
    
    # Verificam daca exista circuite negative
    circuit_negativ = None
    for u, v, cost in muchii:
        if distante[u] != float('inf') and distante[u] + cost < distante[v]:
            # Daca am gasit o muchie care produce o distanta mai mica
            # inseamna ca am gasit un circuit negativ
            # Reconstruim circuitul
            vizitat = [False] * (n + 1)
            circuit = []
            nod_curent = v
            
            while not vizitat[nod_curent]:
                circuit.append(nod_curent)
                vizitat[nod_curent] = True
                nod_curent = parinti[nod_curent]
            
            # Gasim unde începe circuitul
            start_circuit = nod_curent
            circuit.append(start_circuit)
            while circuit[0] != start_circuit:
                circuit.pop(0)
            
            circuit_negativ = circuit[::-1]  # Inversam pentru a avea ordinea corecta
            break
    
    return distante, parinti, circuit_negativ

def reconstruieste_drum(parinti, destinatie):
    drum = []
    nod_curent = destinatie
    while nod_curent != -1:
        drum.append(nod_curent)
        nod_curent = parinti[nod_curent]
    return drum[::-1]  # Inversam pentru a avea ordinea corecta

def main():
    n, m, muchii = citeste_graf("DateIntrare/grafpond.in")
    start = int(input("Introduceti nodul de start: "))
    
    distante, parinti, circuit_negativ = bellman_ford(n, muchii, start)
    
    if circuit_negativ:
        print("Graful contine un circuit negativ:")
        print(" -> ".join(map(str, circuit_negativ)))
    else:
        print(f"Drumuri minime de la nodul {start}:")
        for nod in range(1, n + 1):
            if nod != start and distante[nod] != float('inf'):
                drum = reconstruieste_drum(parinti, nod)
                print(f"Pana la nodul {nod}: {' -> '.join(map(str, drum))} (cost: {distante[nod]})")

if __name__ == "__main__":
    main()