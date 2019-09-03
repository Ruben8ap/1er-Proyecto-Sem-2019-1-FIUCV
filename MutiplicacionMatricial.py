def ProductoMatricial (A,B):
    fila_A = len(A)
    columna_A = len(A[0])
    fila_B = len(B)
    columna_B = len (B[0])

    if columna_A != fila_B:
        print ('No se puede ejecutar la multipicacion de matrices')
        return

    C = []
    for i in range(len(A)):
        C.append([0]*(len(B[0])))

    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(B[0])):
                C [i] [j] += A[i][k]*B[k][j]

    print (C)

A = [[9, 4], [5, 4]]       # matriz 2x2
B = [[1, 2, 3], [9, 5, 6]]   # matriz 2x3
ProductoMatricial(A,B)
