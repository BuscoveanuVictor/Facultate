from collections import defaultdict, deque

def citire_date(nume_fisier):
    f = open(nume_fisier)
    n = int(f.readline())
    durate = list(map(int, f.readline().split()))
    m = int(f.readline())

    graf = defaultdict(list)
    graf_inversat = defaultdict(list)
    for _ in range(m):
        i, j = map(int, f.readline().split())
        graf[i].append(j)
        graf_inversat[j].append(i)
    
    return n, durate, graf, graf_inversat

def calculeaza_timpii_minimi(n, durate, graf):
    # Calculăm gradele de intrare pentru fiecare nod
    grade_intrare = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graf[i]:
            grade_intrare[j] += 1
    
    # Timpii cei mai devreme de începere
    timp_devreme = [0] * (n + 1)
    coada = deque([i for i in range(1, n + 1) if grade_intrare[i] == 0])
    
    while coada:
        nod = coada.popleft()
        for vecin in graf[nod]:
            timp_devreme[vecin] = max(timp_devreme[vecin], 
                                    timp_devreme[nod] + durate[nod-1])
            grade_intrare[vecin] -= 1
            if grade_intrare[vecin] == 0:
                coada.append(vecin)
    
    return timp_devreme

def drum_critic(n, durate, graf, graf_inversat):
    timp_devreme = calculeaza_timpii_minimi(n, durate, graf)
    
    # Calculăm timpul total minim
    timp_total = max(timp_devreme[i] + durate[i-1] for i in range(1, n + 1))
    
    # Calculăm timpii cei mai târzii de terminare
    timp_tarziu = [timp_total] * (n + 1)
    for i in range(1, n + 1):
        if not graf[i]:  # noduri finale
            timp_tarziu[i] = timp_devreme[i] + durate[i-1]
    
    # Mergem înapoi prin graf pentru a calcula timpii târzii
    for i in range(n, 0, -1):
        for predecesor in graf_inversat[i]:
            timp_tarziu[predecesor] = min(timp_tarziu[predecesor],
                                        timp_tarziu[i] - durate[predecesor-1])
    
    # Găsim activitățile critice (unde timpul de început devreme = timpul târziu)
    activitati_critice = []
    for i in range(1, n + 1):
        if timp_devreme[i] == timp_tarziu[i]:
            activitati_critice.append(i)
    
    # Construim intervalele pentru fiecare activitate
    intervale = []
    for i in range(1, n + 1):
        intervale.append((timp_devreme[i], timp_devreme[i] + durate[i-1]))
    
    return timp_total, activitati_critice, intervale

def main():
    n, durate, graf, graf_inversat = citire_date("activitati.in")
    timp_total, activitati_critice, intervale = drum_critic(n, durate, graf, graf_inversat)
    
    print(f"Timp minim {timp_total}")
    print(f"Activitati critice: {' '.join(map(str, activitati_critice))}")
    for i in range(n):
        print(f"{i+1}: {intervale[i][0]} {intervale[i][1]}")

if __name__ == "__main__":
    main()