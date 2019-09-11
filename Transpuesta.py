def traspuesta(A):
    if len(A)==len(A[0])-1:
        if type(A)==list:
            aux=[]
            aux_2=[]
            for h in A:
                if type(h)==list:
                    aux.append(h)
                else:
                    raise TypeError("Solo puede ingresar tipo lista dentro de la funcion")
                for j in h:
                    if type(j)==type("str"):
                        aux_2.append(j)
            if len(aux_2)>=1:
                raise TypeError("No se puede ingresar tipo datos string dentro de esta funcion")
            if len(aux_2)==0:
                if len(A)!=len(aux):
                    print("\nLa funcion traspuesta, solo acepta elementos del tipo lista")
                if len(A)==len(aux):
                    filas = len(A)
                    columnas = len(A[0])
                    print("\nMatriz Original\n")
                    for x in A:print(x)
                    Transposicion=[[A[j][i] for j in range(filas)] for i in range(columnas)]
                    print("\nMatriz Transpuesta\n")
                    for k in Transposicion:print(k)
                    print(columnas)
                    print(filas)
        else:
            print("La funcion traspuesta, solo permite la entrada de tipo lista")
    else:
        raise ValueError("Ha ingresado datos invalidos")
    return A
