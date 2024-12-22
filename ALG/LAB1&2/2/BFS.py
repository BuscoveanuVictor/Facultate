import queue

# BFS (cautare in latime)
# 0. algortim care lucreaza iterative, viziteaza toata nodurile si muchiile ( O(m+n))
# 1. se stocheaza nodurile care trebuie vizitate pe o queue, iar cele vizitate 
# sunt marcate ca atare intr-o lista 
# 2. dupa ce un nod este procesat se scoate de pe queue
# 3. odata scos de pe queue se adauga vecinii acestui
# p. putem determina drumul de distanta minimi de la nodul de start la celelalte noduri 
# prin folosirea unui vector de tati si lista de distante 

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

def BFS(file):
    lista_adiacenta,firstLine = ListaAdiacenta(file)
    noduri = firstLine[0]
    start = firstLine[2]
    

    distanta = [-1]*(noduri+1)
    tata = [0]*(noduri+1)

    vizitat = [0]*(noduri+1)
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        nod = q.get()
        vizitat[nod] = 1
        distanta[nod] = distanta[tata[nod]] + 1

        for copil in lista_adiacenta[nod]:
            if vizitat[copil] == 0 :
                q.put(copil)
                tata[copil] = nod

    print(distanta[1:])

BFS("DateIntrare/bfs.in")