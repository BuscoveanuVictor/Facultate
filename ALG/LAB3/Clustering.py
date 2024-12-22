import Levenshtein as Lv
import Kruskal as Kr

def Clustering(file):
    f = open(file)

    cuvinte = f.read().split()
    noduri = len(cuvinte)
    print(noduri)
   
    dict_graf = {}
    for i in range(len(cuvinte)):
        #print(i+1,cuvinte[i])
        for j in range(i+1,len(cuvinte)):
            distanta_cuvinte = Lv.Levenshtein(cuvinte[i],cuvinte[j])
            print(distanta_cuvinte,cuvinte[i],cuvinte[j])
            dict_graf[distanta_cuvinte] = dict_graf.get(distanta_cuvinte,[])
            dict_graf[distanta_cuvinte].append((i+1,j+1))

    #print(dict_graf) #dictionarul grafului cu ponderile ca si keys
    print(Kr.Kruskal(dict_graf,noduri,3))

    # lista_adiacenta, cost, reprezentanti = Kr.Kruskal(dict_graf,noduri,3)
    # print(reprezentanti)
    
    # for nod in reprezentanti:
    #     print(nod)
    # f.close()

Clustering("DateIntrare/cuvinte.in")
