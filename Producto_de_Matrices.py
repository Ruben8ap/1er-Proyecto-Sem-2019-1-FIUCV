def productoMatricial (A,B):
    if type(A)==list and type(B)==list:
        """productoMatricial"""
        fila_A = len(A)
        columna_A = len(A[0])
        fila_B = len(B)
        columna_B = len (B[0])
        if columna_A != fila_B:
            print ("No se puede ejecutar la multipicacion de matrices")
            return
        C = []
        for i in range(len(A)):C.append([0]*(len(B[0])))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)): C [i][j] += A[i][k]*B[k][j]
        print("El resultado de la multiplicaión de matrices es:")
        for x in C: print(x)
    else:
        print("Debe ingresar las matrices como un arreglo de listas de lista")
    return A,B
