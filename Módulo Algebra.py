def Producto_Matricial(matriz_1,matriz_2):
    aux=[]
    aux_2=[]
    aux_3=[]
    aux_4=[]
    for h in matriz_1:
        if type(h)==list:aux.append(h)
        else: raise TypeError("Solo puede ingresar elementos tipo lista dentro de la funcion Producto_Matricial")
        for j in h:
            if type(j)==type("str"):aux_2.append(j)
    for q in matriz_2:
        if type(q)==list:aux_3.append(q)
        else:raise TypeError("Solo puede ingresar  elementos tipo lista dentro de la funcion Producto_Matricial")
        for d in q:
            if type(d)==type("str"):aux_4.append(d)
    if (len(aux_2)>=1 or len(aux_4)>=1):raise TypeError("No se puede ingresar tipo datos string dentro de la funcion Produto_Matricial")
    for g in matriz_1:
        if len(g)!=len(h):raise ValueError("Todas las filas deben tener la misma cantidad de columnas")
    for z in matriz_2:
        if len(z)!=len(q):raise ValueError("Todas las filas deben tener la misma cantidad de columnas")
    if (type(matriz_1) and type(matriz_2))==list:
        fila_matriz_1 = len(matriz_1)
        columna_matriz_1 = len(matriz_1[0])
        fila_matriz_2 = len(matriz_2)
        columna_matriz_2 = len (matriz_2[0])
        if columna_matriz_1 != fila_matriz_2:raise ValueError("No se puede ejecutar la multipicacion de matrices, el numero de filas de la primera matriz debe ser igual al numero de filas de la segunda matriz")
        C = []
        for i in range(len(matriz_1)):C.append([0]*(len(matriz_2[0])))
        for i in range(len(matriz_1)):
            for j in range(len(matriz_2[0])):
                for k in range(len(matriz_2)): C [i][j] += matriz_1[i][k]*matriz_2[k][j]
        print("\nEl resultado de la multiplicaión de matrices es:\n")
        for x in C: print(x)
    else:raise TypeError(" La Funcion Producto_Matricial solo acepta como entrada matrices que emulen el arreglo listas de listas")
    return matriz_1,matriz_2
def Producto_Cruz(vectores):
    Final= []
    Resultado=[]
    aux=[]
    for j in vectores[0] and vectores[1]:
        if type(j)==type("str"):
            aux.append(j)
    if len(aux)>=1:
        raise  TypeError("No se puede ingresar el tipo dato string, dentro de funcion Producto_Cruz")
    if len(vectores)==2:
        if (type(vectores[0]) and type(vectores[1]) and type(vectores))==list:
            if len(vectores[0])==3 and len(vectores[1])==3:
                Multiplicacion_i=(vectores[0][1]*vectores[1][2])-(vectores[0][2]*vectores[1][1])
                Multiplicacion_j=-( (vectores[0][0]*vectores[1][2]) - (vectores[0][2]*vectores[1][0]) )
                Multiplicacion_k=  (vectores[0][0]*vectores[1][1]) - (vectores[0][1]*vectores[1][0])
                Resultado.append(Multiplicacion_i)
                Resultado.append(Multiplicacion_j)
                Resultado.append(Multiplicacion_k)
                Final.append(Resultado)
                print("\nEl resultado de la multiplicacion vectorial es: {}".format(Final))
            else:raise ValueError("La funcion Producto_Cruz solo acepta vectores con 3 componentes")
        else:raise TypeError("La funcion Producto_Cruz solo acepta vectores, que emulen el arreglo listas de listas")
    else:raise ValueError("La funcion Producto_Cruz solo permite la entrada de dos vectores")
    return vectores
def Transpuesta(matriz):
    if type(matriz)==list:
        aux=[]
        aux_2=[]
        for h in matriz:
            if type(h)==list:aux.append(h)
            else:raise TypeError("Los elementos de la funcion Transpuesta deben ser de tipo lista")
            for j in h:
                if type(j)==type("str"):aux_2.append(j)
        for g in matriz:
            if len(g)!=len(h):raise ValueError("Todas las filas deben tener la misma cantidad de columnas")
        if len(aux_2)>=1:raise TypeError("No se puede ingresar tipo datos string dentro de la funcion Transpuesta")
        if len(aux_2)==0:
            if len(matriz)!=len(aux):print("\nLa funcion traspuesta, solo acepta elementos del tipo lista")
            if len(matriz)==len(aux):
                filas = len(matriz)
                columnas = len(matriz[0])
                print("\nMatriz Original\n")
                for x in matriz:print(x)
                Transposicion=[[matriz[j][i] for j in range(filas)] for i in range(columnas)]
                print("\nMatriz Transpuesta\n")
                for k in Transposicion:print(k)
    else:print("La funcion traspuesta, solo permite la entrada de matrices que emulen el arreglo listas de listas")
    return matriz
def Determinante(matriz):
    aux=[]
    aux_2=[]
    for h in matriz:
        if type(h)==list:aux.append(h)
        else:raise TypeError("La funcion Determinante solo permite la entrada tipo lista dentro de la funcion")
        for j in h:
            if type(j)==type("str"):aux_2.append(j)
    for g in matriz:
        if len(g)!=len(h):raise ValueError("Todas las filas deben tener la misma cantidad de columnas")
    if len(aux_2)>=1:raise TypeError("No se puede ingresar tipo datos string dentro de la funcion Determinante")
    if len(aux_2)==0:
        if len(matriz)!=len(aux):print("\nLa funcion determinante, solo acepta elementos del tipo lista")
    if type(matriz)==list:
        if len(matriz)==len(aux):
            n=len(matriz)
            if len(matriz)==len(matriz[0]):
                for z in range (n-1):
                    for x in range(1, n-z):
                        if (matriz[z][z] != 0 ):
                            p = matriz[x+z][z] / matriz[z][z]
                            for y in range (n):matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                deter=1
                for x in range (n):deter=matriz[x][x]*deter
                print ('\nEl determinante de la matriz es = ',deter)
            else: raise ValueError("El determinante es solo para matrices cudradas")
    else: raise TypeError("La funcion determinante solo acepta matrices que emulen el arreglo listas de listas")
    return matriz
