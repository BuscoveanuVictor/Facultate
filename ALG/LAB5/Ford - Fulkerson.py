from collections import defaultdict
from queue import Queue

def citeste_retea(file_path):
    with open(file_path) as file:
        nr_noduri = int(file.readline().strip())
        s, t = map(int, file.readline().strip().split())
        nr_arce = int(file.readline().strip())
        muchii = []
        for _ in range(nr_arce):
            u, v, capacity, flow = map(int, file.readline().strip().split())
            muchii.append((u, v, capacity, flow))
    return nr_noduri, s, t, muchii


def verifica_flux(n, s, t, muchii):
   
    inflow = defaultdict(int)
    outflow = defaultdict(int)
    
    for u, v, capacitate, flux in muchii:
        if flux > capacitate:
            return f'Fluxul depaseste capacitatea pe muchia ({u}, {v})'
        # Fluxul care iese din nodul sursa u
        outflow[u] += flux
        # Fluxul care intra in nodul destinatie v
        inflow[v] += flux
    

    for node in range(1, n + 1):
        # Daca nodul nu este sursa sau destinatie si fluxul care intra este diferit de fluxul care iese
        # atunci fluxul nu este valid
        if node != s and node != t and inflow[node] != outflow[node]:
            return f"Conservarea fluxului nu este respectata la nodul {node}"
    
    return "Fluxul este valid"


def ford_fulkerson(n, s, t, muchii):
    
    # u nod din care iese flux
    # v nod in care intra flux

    # Cream graful rezidual
    graful_rezidual = defaultdict(lambda: defaultdict(int))
    for u, v, capacitate, flux in muchii:
        graful_rezidual[u][v] = capacitate - flux    #fluxul care mai poate trece prin muchia (u, v)
        graful_rezidual[v][u] = flux                 # Capacitatea inversa pentru fluxul existent

    def bfs_find_augmenting_path():
        parinti = {s: -1}
        queue = Queue()
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            # Parcurgem vecinii nodului u
            for v in graful_rezidual[u]:
                # Daca nodul v nu a fost deja vizitat si 
                # muchia (u, v) are capacitate pozitiva
                if v not in parinti and graful_rezidual[u][v] > 0:
                    parinti[v] = u
                    # Daca am ajuns la nodul destinatie, am gasit un drum de crestere
                    if v == t:
                        return parinti
                    queue.put(v)
        return None

    max_flow = 0
    while True:
        parent = bfs_find_augmenting_path()
        # Daca nu am gasit un drum de crestere, iesim din bucla
        if not parent:
            break

        # Determinam care este fluxul maxim pe care il 
        # putem trimite pe drumul de crestere
        path_flow = float('Inf')

        # Pornim de la nodul destinatie si 
        # mergem inapoi pana la nodul sursa
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graful_rezidual[u][v])
            v = u
        max_flow += path_flow

        # Actualizam capacitatile in graful rezidual
        # Parcurgem drumul de crestere si actualizam capacitatile
        v = t
        while v != s:
            u = parent[v]
            # scadem fluxul de pe muchia (u, v)
            # astfel ramanem cu capacitatea care mai poate trece prin muchia (u, v)
            graful_rezidual[u][v] -= path_flow 
            # adaugam fluxul de pe muchia (v, u)
            # sugereaza fluxul pe care il avem deja pe muchia (v, u)
            # si pe care il putem 'retrage'
            graful_rezidual[v][u] += path_flow  
            # mergem inapoi la nodul parinte
            v = u


    # Odata finalizat algoritmul Fork-Furlkerson
    # Calculam tăietura minimă
 
    vizitat = set()
    def bfs_for_min_cut():
        queue = Queue()
        queue.put(s)
        vizitat.add(s)
        while not queue.empty():
            u = queue.get()
            for v in graful_rezidual[u]:
                if v not in vizitat and graful_rezidual[u][v] > 0:
                    vizitat.add(v)
                    queue.put(v)

    bfs_for_min_cut()

    # Calculam fluxul pe fiecare arc si taietura minima
    flux_pe_muchie = []
    muchii_taietura_minima = []

    # Prin urmare parcurgem nodurile si muchiile grafului rezidual
    for u in range(1, n + 1):
        for v in graful_rezidual[u]:
            # Verificam daca muchia (u, v) face parte din taietura minima
            if u in vizitat and v not in vizitat and graful_rezidual[u][v] == 0:
                muchii_taietura_minima.append((u, v))
            # Calculam fluxul pe muchia (u, v)
    
    # Afla fluxul pe fiecare muchie
    for edge in muchii:
        u, v, capacitate_initiala, _ = edge    
        flux_actual = capacitate_initiala - graful_rezidual[u][v]
        flux_pe_muchie.append((u, v, flux_actual))

    capacitate_taietura_minima = 0
    for u, v, capacitate, _ in muchii:
        if (u, v) in muchii_taietura_minima:
            capacitate_taietura_minima += capacitate


    return max_flow, flux_pe_muchie, capacitate_taietura_minima, muchii_taietura_minima
if __name__ == "__main__":
    n, s, t, muchii = citeste_retea('DateIntrare/retea.in')
    max_flow, flux_pe_muchie, capacitate_taietura_minima, muchii_taietura_minima = ford_fulkerson(n, s, t, muchii)
    message = verifica_flux(n, s, t, muchii)
    print(message)
    print(f"Fluxul maxim: {max_flow}")
    print(f"Fluxul pe fiecare muchie: {flux_pe_muchie}")
    print(f"Capacitatea tăieturii minime: {capacitate_taietura_minima}")
    print(f"Muchii tăieturii minime: {muchii_taietura_minima}")



