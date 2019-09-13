def determinante(matriz):
    if type(matriz[0] and type(matriz[1]) and type(matriz))==type(list):
        n=len(matriz)
        if len(matriz)==len(matriz[0]):
            for z in range (n-1):
                for x in range(1, n-z):
                    if (matriz[z][z] != 0 ):
                        p = matriz[x+z][z] / matriz[z][z]
                        for y in range (n):
                            matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
            deter=1
            for x in range (n):
                deter=matriz[x][x]*deter
            print ('\nEl determinante de la matriz es = ',deter)
        else:
            raise ValueError("El determinante es solo para matrices cudradas")
    else:
        raise TypeError("Usted ha ingresado un tipo de dato invalido")
    return matriz
