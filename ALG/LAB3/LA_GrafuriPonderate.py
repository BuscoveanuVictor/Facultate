# index = 0 daca vrem sa avem ca si key nodurile
# index = 1 daca vrem sa avem ca si key ponderea 
def ListaAdiacenta(file, neorientat=True, index=0):
    f = open(file)

    firstLine = [int(elem) for elem in f.readline().split()]
    lista_fisier = [int(elem) for elem in f.read().split()]
    lista_adiacenta = dict()
    for i in range(0, len(lista_fisier), 3):
        nod = lista_fisier[i]
        vecin = lista_fisier[i + 1]
        pondere = lista_fisier[i + 2]
        if index :
            lista_adiacenta[pondere] = lista_adiacenta.get(pondere,[])
            lista_adiacenta[pondere].append((nod,vecin))
        else :
            lista_adiacenta[nod] = lista_adiacenta.get(nod,[])
            lista_adiacenta[nod].append((vecin,pondere))
            if neorientat:
                lista_adiacenta[vecin] = lista_adiacenta.get(vecin,[])
                lista_adiacenta[vecin].append((nod,pondere))

    f.close()
    return lista_adiacenta, firstLine
