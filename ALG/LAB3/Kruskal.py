import LA_GrafuriPonderate as LA

def f_Kruskal(file):
    lista_adiacenta, firstLine = LA.ListaAdiacenta(file,1,1)
    noduri = firstLine[0]
    muchii = firstLine[1]
    return Kruskal(lista_adiacenta,noduri)

def Kruskal(lista_adiacenta_ponderiKey,noduri,pasi_inainte_de_oprire=1):

    # Sortam lista(dict) dupa costul muchiilor
    lista_adiacenta_sortata = dict(sorted(lista_adiacenta_ponderiKey.items()))
    # Marcam reprezentantii fiecarui nod (fiecare nod este reprezentat de el insusi)
    culoare_reprezentant = [0] * (noduri+1)
    for i in range(1,noduri+1):
        culoare_reprezentant[i] = i

    muchii_vizitate = 0 # Contorul de muchii vizitate pentru a verifica daca am ajuns la numarul de muchii necesar
    cost_minim = 0 # Costul minim al arborelui
    graf_minim = [] # Lista de muchii din arborele minim

    ponderi = list(lista_adiacenta_sortata.keys())
    print(ponderi)

    # Parcurgem lista sortata dupa ponderea muchiilor
    for cost in ponderi:
        # Parcurgem lista de muchii cu acel cost
        for muchie in lista_adiacenta_sortata[cost]:
            nod1 = muchie[0]
            nod2 = muchie[1]
            # Daca nodurile nu au acelasi reprezentant, adaugam muchia in arborele minim
            if(culoare_reprezentant[nod1] != culoare_reprezentant[nod2]): 
                # Adaugam costul muchiei la costul minim
                cost_minim += cost
                # Incrementam contorul de muchii vizitate
                muchii_vizitate += 1 
                # Adaugam muchia in arborele minim
                graf_minim.append(muchie)
                
                # Actualizam reprezentantul nodului 1 cu reprezentantul nodului 2
                culoare_reprezentant[nod2] = culoare_reprezentant[nod1]
                for i in range(1,len(culoare_reprezentant)):
                    if culoare_reprezentant[i] == nod2:
                            culoare_reprezentant[i] = culoare_reprezentant[nod1]

                # Daca am ajuns la numarul de muchii necesar am gasit arborele minim si iesim din for
                if muchii_vizitate == noduri - pasi_inainte_de_oprire:
                     return graf_minim, cost_minim, culoare_reprezentant[1:]
                
    return graf_minim, cost_minim, culoare_reprezentant[1:]
    
   
    

