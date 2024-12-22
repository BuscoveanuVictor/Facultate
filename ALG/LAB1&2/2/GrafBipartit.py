import queue
   
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


def impartire_echipe(file):
    lista_adiacenta, firstLine = ListaAdiacenta(file)
    noduri = firstLine[0]
   
    echipa = [-1] * (noduri+ 1)
    
    def bfs(start):
        q = queue.Queue()
        q.put(start)
        echipa[start] = 1  
        while not q.empty():
            nod = q.get()
            # Fiecare vecin al nodului curent 
            # daca nu e vizitat il vom pune in 
            # echipa opusa
            for vecin in lista_adiacenta[nod]:
                if echipa[vecin] == -1:  
                    echipa[vecin] = 1 if echipa[nod] == 2 else 2 
                    q.put(vecin)
                # Daca gasim un vecin al nodului curent 
                # care a fost vizitat si care face parte din 
                # aceasi echipa inseamna ca graful nu e bipatit si iesim
                elif echipa[vecin] == echipa[nod]:  
                    return False  
        return True
    
    # Facem for pentru toate nodurile din graf
    # intrcat nu stim daca graful dat este conex 
    # adica pot exista mai multe componente conexe 
    # din care sa obtinem 2 echipe
    for nod in range(1, noduri+ 1):
        if echipa[nod] == -1:
            if not bfs(nod):
                return "IMPOSIBIL"
    
    print(*echipa[1:])

impartire_echipe("DateIntrare/teams.in")
