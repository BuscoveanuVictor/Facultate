def Levenshtein(cuv1,cuv2):
    l1 = len(cuv1)
    l2 = len(cuv2)

    d = [[0] * (l2+1) for _ in range(l1+1)]

    for i in range(l1+1):
        d[i][0] = i

    for j in range(l2+1):
        d[0][j] = j

    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if cuv1[i-1] == cuv2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j],d[i][j-1],d[i-1][j-1]) + 1
    return d[l1][l2]
