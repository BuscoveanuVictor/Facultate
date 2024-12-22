import heapq

def citeste_date(nume_fisier):
    f = open(nume_fisier)
    n, m = [int(elem) for elem in f.readline().split()]
    
    graf = dict()
    for _ in range(m):
        i, j, p = [int(elem) for elem in f.readline().split()]       
        graf.setdefault(i, []).append((j, p))
    
    return n, graf

def drum_siguranta_maxima(n, graf, start, destinatie):
    # Distante este un vector care retine distanta minima de la nodul de start la fiecare nod din graf
    # Se initializeaza cu infinit pentru a putea fi comparat cu costurile muchiilor
    distanta_drum_catre = [float('inf')] * (n + 1)
    # Distanta de la nodul de start la el insusi este 0
    distanta_drum_catre[start] = 0
    # Parinti este un vector care retine parintele fiecarui nod in arborele de drum minim
    parinti = [-1] * (n + 1)
    
    # Coada(min heap) este o lista de prioritati care retine valoarea si nodul
    # Coada avand prop de min heap putem aplica heapq.heappop care
    # va intoarce nodul cu distanta minima(care va fi marcat ca procesat)
    coada = [(0, start)]
    while coada:
        dist_catre_nodul_curent, nod = heapq.heappop(coada)
        
        if nod == destinatie:
            break
            
        # Daca din nodul curent 'ies' mai multe arce, vom alege pe cel cu distanta minima
        # ca sa putem pune in coada configuratia cu distanta minima
        # astfel mai jos putem sa dam 'skip' la nodul curent daca distanta
        # catre el e mai mare decat pe care o avem pana acum in vectorul de distante
        if dist_catre_nodul_curent > distanta_drum_catre[nod]:
            continue
        
        # Parcurgem toti vecinii nodului curent(procesat)
        for vecin, cost in graf[nod]:
            # iar pentru fiecare vecin vedem ce distanta 
            # am putea avea daca am trece prin el
            dist_noua = distanta_drum_catre[nod] + cost
            
            # Daca distanta noua este mai mica decat cea din vectorul de distante
            # atunci actualizam distanta si parintele
            if dist_noua <  distanta_drum_catre[vecin]:
                distanta_drum_catre[vecin] = dist_noua
                parinti[vecin] = nod
                # Adaugam in coada noua configuratie
                heapq.heappush(coada, (dist_noua, vecin))
    
    # Reconstruim drumul
    drum = []
    nod_curent = destinatie
    while nod_curent != start:
        drum.append(nod_curent)
        nod_curent = parinti[nod_curent]
    drum.append(start)
    drum.reverse()
    
    return drum

def main():
    n, graf = citeste_date("DateIntrare/retea.in")
    start = int(input("Nod start: "))
    destinatie = int(input("Nod destinatie: "))

    #print(graf)
    drum = drum_siguranta_maxima(n, graf, start, destinatie)
    print(drum)

    if drum is None:
        print(f"Nu există drum de la {start} la {destinatie}")
    else:
        print(f"Drumul de siguranță maximă: {' -> '.join(map(str, drum))}")
        print(f"Probabilitatea de funcționare: 2^{-sum(drum)}")

if __name__ == "__main__":
    main()