import ListaAdiacenta as LA

def DFS(file):
    lista_adiacenta, firstLine = LA.ListaAdiacenta(file)
    noduri = firstLine[0]

    vizitat = [False] * (noduri + 1)
    parinte = [-1] * (noduri + 1)
    muchii_de_intoarcere = []
    
    def AlgoritmDfs(nod, parinte_curent=-1):
        vizitat[nod] = True
        parinte[nod] = parinte_curent
        
        for vecin in lista_adiacenta[nod]:
            if not vizitat[vecin]:
                AlgoritmDfs(vecin, nod)
            elif vecin != parinte_curent and nod < vecin:
                muchii_de_intoarcere.append((nod, vecin))
    AlgoritmDfs(1)

    print("Muchiile de întoarcere sunt: ", muchii_de_intoarcere)


DFS("DateIntrare/cicluri.in")