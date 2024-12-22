# DFS (cautare in adancime)
# 0. algoritm iterativ(cu stack) dar de preferat recursiv O(m+n)
# 1. se lucreaza recursiv, procesand de fiecare data primul vecin gasit al fiecarui nod
# p. se foloseste pentru decoperirea componentelor conexe grafurilor si pt detectarea de ciclurie
  
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


def DFS(file):
    lista_adiacenta, firstLine = ListaAdiacenta(file)
    noduri = firstLine[0]

    vizitat = [0]*(noduri+1)
    componente = 0

    def AlgoritmDfs(i):
        vizitat[i] = 1
        for nod in lista_adiacenta[i]:
            if vizitat[nod] == 0:
                AlgoritmDfs(nod)

    for i in range(1,noduri+1):
        if vizitat[i] == 0:
            componente+=1;
            AlgoritmDfs(i)

    print(componente)


DFS("bfs.in")