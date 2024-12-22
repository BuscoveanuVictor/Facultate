def ListaAdiacenta(file, neorientat=True):
    f = open(file)

    firstLine = [int(elem) for elem in f.readline().split()]
    lista_fisier = [int(elem) for elem in f.read().split()]
    lista_adiacenta = dict()
    for i in range(0, len(lista_fisier), 2):
        nod = lista_fisier[i]
        vecin = lista_fisier[i + 1]
        lista_adiacenta[nod] = lista_adiacenta.get(nod,[])
        lista_adiacenta[nod].append(vecin)
        if neorientat:
            lista_adiacenta[vecin] = lista_adiacenta.get(vecin,[])
            lista_adiacenta[vecin].append(nod)

    f.close()
    return lista_adiacenta, firstLine

def sortare_topologica(fisier):
    lista_adiacenta, firstLine = ListaAdiacenta(fisier)
    noduri = firstLine[0]

    vizitat = [0]*(noduri+1)
    stack = []

    print(lista_adiacenta)

    # 1 = Nod in curs de procesare(vizitat)
    # 2 = Nod procesat
    def dfs(nod):
        # Daca ne intoarce la un nod care e in curs 
        # de procesare inseamna ca am gasit un ciclu
        if vizitat[nod] == 1:
            return "IMPOSIBIL"

        # Daca am ajuns la un nod deja procesat
        # putem sa ne oprim
        if vizitat[nod] == 2:
            return 

        # Marcam nodul curent ca vizitat
        # iar apoi ii luam primu vecin (dfs)
        vizitat[nod] = 1   
        for vecin in lista_adiacenta[nod]:
            if vizitat[vecin] != 2:
                dfs(vecin)

        # odata ce s-a iesit din recursivitatea pt nodul dat
        # adica am ajuns la dead end marcam nodul ca fiind procesat
        vizitat[nod] = 2  
        stack.append(nod)
    
    for nod in range(1, noduri + 1):
        if vizitat[nod] != 2:
            dfs(nod)
    
    # Se returneaza stack-ul inversat 
    # doarece sortarea topologica se 
    # bazeaza tot timpul pe gasirea ultimului nod
    # care poate fi adugat a.i. sa obtinem o ordine valida
    return stack[::-1]  

print(sortare_topologica('DateIntrare/sort.in'))
