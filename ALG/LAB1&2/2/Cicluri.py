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


def Cicluri(file):
    lista_adiacenta, firstLine = ListaAdiacenta(file)
    noduri = firstLine[0]

    vizitat = [0] * (noduri + 1)
    stiva = []
    in_stiva = [0] * (noduri + 1)
    ciclu_gasit = []
    
    def AlgoritmDfs(nod):
        stiva.append(nod)
        in_stiva[nod] = 1
        vizitat[nod] = 1
        
        for vecin in lista_adiacenta[nod]:
            if not vizitat[vecin]:
                return AlgoritmDfs(vecin)     
            elif in_stiva[vecin] and (len(stiva) < 2 or vecin != stiva[-2]):
                idx = stiva.index(vecin)
                ciclu_gasit.extend(stiva[idx:])
                return True
        
        stiva.pop()
        in_stiva[nod] = 0
        return False
   
    if AlgoritmDfs(1):
        print("Ciclul găsit este:", *ciclu_gasit, ciclu_gasit[0])
    else:
        print("Nu exista cicluri")

Cicluri("DateIntrare/cicluri.in")