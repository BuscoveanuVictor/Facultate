import queue
from queue import Queue
import ListaAdiacenta as LA

def BFS(file):
    lista_adiacenta, firstLine = LA.ListaAdiacenta(file)
    noduri = firstLine[0]
    start = firstLine[2]
    destinatie = firstLine[3]

    q = queue.Queue()
    distanta = [-1] * (noduri + 1)
    tata = [-1] * (noduri + 1)
    vizitat = [False] * (noduri + 1)

    q.put(start)
    vizitat[start] = 1
    distanta[start] = 0

    while not q.empty():
        nod = q.get()
        
        for vecin in lista_adiacenta[nod]:
            if not vizitat[vecin]:
                vizitat[vecin] = True
                distanta[vecin] = distanta[nod] + 1
                tata[vecin] = nod
                q.put(vecin)

                if vecin == destinatie:
                    break

    if distanta[destinatie] == -1:
        print("Nu există drum de la", start , "la", destinatie)
    else:
        drum = []
        nod_curent = destinatie
        
        while nod_curent != -1:
            drum.append(nod_curent)
            nod_curent = tata[nod_curent]
            
        drum.reverse()
        print("Drumul minim de la", start, "la", destinatie, "este:", *drum)
        print("Lungimea drumului este:", distanta[destinatie])

BFS("DateIntrare/bfs.in")