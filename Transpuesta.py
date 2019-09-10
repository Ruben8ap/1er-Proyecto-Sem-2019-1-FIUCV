def traspuesta(A):
    if type(A)==list:
        """Funcion para Trasponer una Matriz"""
        filas = len(A)
        columnas = len(A[0])
        print("Matriz Original")
        for x in A:print(x)
        Transposicion=[[A[j][i] for j in range(filas)] for i in range(columnas)]
        print("Matriz Transpuesta")
        for k in Transposicion:print(k)
    else:
        print("El tipo de arreglo para la matrices debe ser de la forma listas de listas")
    return A
