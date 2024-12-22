def floyd_warshall(n, matrix):
    # k reprezinta nodul intermediar
    # iar cand calculam matrice[i][j]
    # este ca si cum l-am taia pe k si
    # l-am aduna la drumul de la i la j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(matrix[i][j]>matrix[i][k]+matrix[k][j]):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    
    # Verificam daca exista circuite negative
    for i in range(n):
        if matrix[i][i] < 0:
            # Daca exista drum de la i la i cu pondere negativa
            # atunci graful contine circuit negativ si returnam None
            return None 
    
    return matrix

def main():
    with open("DateIntrare/floyd.in") as f:
        n, m = map(int, f.readline().split())
        
        # Initializam matricea de distante 
        matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
            
        for _ in range(m):
            x, y, cost = map(int, f.readline().split())
            matrix[x-1][y-1] = cost
    
    result = floyd_warshall(n, matrix)

    if result is None:
        print("Graful contine circuit negativ!")
    else:
        print("Matricea distantelor minime:")
        for row in result:
            print([x if x != float('inf') else "INF" for x in row])

if __name__ == "__main__":
    main()