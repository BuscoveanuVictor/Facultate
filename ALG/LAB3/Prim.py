import LA_GrafuriPonderate as LA

def Prim(file, start=1):
    print(file)
    lista_adiacenta, firstLine = LA.ListaAdiacenta(file)
    noduri = firstLine[0]
    muchii = firstLine[1]

    graf_minim = []
    vizitat = [False] * (noduri + 1)

    # Lista de valori pentru fiecare nod care retine costul minim de la nodul 
    # curent la nodul curent la cel mai apropiat nod nevizitat
    valori_noduri_descoperite = [float('inf')] * (noduri + 1)


    # Notatie pentru:
    # Nodul vecin
    vecin = 0
    # Costul muchiei
    pondere = 1

    # Descoperim nodul de start
    valori_noduri_descoperite[start] = 0
    parinte = [-1] * (noduri + 1)
    cost_minim = 0

    # Descoperim noduri pana cand am ajuns la numarul de muchii necesar pentru arborele minim
    for i in range(noduri):

        min_valoare = float('inf')
        
        # Alegem nodul decoperit cu valoarea minima dintre cele nevizitate(pentru a nu se crea un ciclu) 
        for j in range(1,noduri+1):
            if (valori_noduri_descoperite[j] < min_valoare and vizitat[j] == False):
                min_valoare = valori_noduri_descoperite[j]
                nod_curent = j

        # Marchez nodul curent ca fiind vizitat
        vizitat[nod_curent] = True
        # Si in adaug in graf
        graf_minim.append((parinte[nod_curent],nod_curent))
        cost_minim += min_valoare
    
        # Pasul de decoperire a nodurilor vecine
        for muchie in lista_adiacenta[nod_curent]:
            # Descopar pentru fiecar nod vecin nevizitat ponderea minima
            if (vizitat[muchie[vecin]] == False and muchie[pondere] < valori_noduri_descoperite[muchie[vecin]]):
                # Actualizam costul minim de la nodul curent la nodul vecin
                valori_noduri_descoperite[muchie[vecin]] = muchie[pondere]
                # Actualizam parintele nodului vecin
                parinte[muchie[vecin]] = nod_curent

    print(cost_minim)
    for muchie in graf_minim[1:]:
        print(muchie)

Prim("DateIntrare/graf_ponderat.in",3)
