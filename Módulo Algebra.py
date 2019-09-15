def Producto_Matricial(matriz_1,matriz_2):
    """Fución para ejecutar la multiplicación entre dos matrices"""
    aux=[]
    aux_2=[]
    aux_3=[]
    aux_4=[]
    for h in matriz_1: #Iteramos sobre los elementos de la matriz_1
        if type(h)==list:aux.append(h) #Verificamos si cada uno de ellos son de tipo lista y los agregamos la lista aux
        else: raise TypeError("Solo puede ingresar elementos tipo lista dentro de la funcion Producto_Matricial") #Si alguno de ellos no son tipo lista arrojamos este error
        for j in h: #Iteramos sobre los elementos mas internos de la matriz.
            if type(j)==type("str"):aux_2.append(j) #Verificamos si hay algun tipo string y lo agregamos a la lista aux_2
    for q in matriz_2: #Iteramos sobre los elementos de la matriz_2
        if type(q)==list:aux_3.append(q) #Verificamos si cada uno de ellos son de tipo lista y los agregamos la lista aux_3
        else:raise TypeError("Solo puede ingresar  elementos tipo lista dentro de la funcion Producto_Matricial") #Si alguno de ellos no son tipo lista arrojamos este error
        for d in q: #Interamos sobre los elementos de la matriz_2
            if type(d)==type("str"):aux_4.append(d) #Verificamos si hay algun tipo string y lo agregamos a la lista aux_3
    if (len(aux_2)>=1 or len(aux_4)>=1):raise TypeError("No se puede ingresar tipo datos string dentro de la funcion Produto_Matricial") #Planteamos la condicion de error para cuando algunas de las listas aux estan llenas respectivamente
    for g in matriz_1: #Iteramos sobre los elementos de la matriz_1 
        if len(g)!=len(h):raise ValueError("Todas las filas deben tener la misma cantidad de columnas") #Verificamos si para cada elemento "g" y "h" poseen la misma longitud de columnas y arrojamos el errro correspondiente
    for z in matriz_2: #Interamos sobre los elementos de la matriz_2
        if len(z)!=len(q):raise ValueError("Todas las filas deben tener la misma cantidad de columnas") #Verificamos si para cada elemento "z" y "q" poseen la misma longitud de columnas y arrojamos el errro correspondiente
    if (type(matriz_1) and type(matriz_2))==list: #Verificamos que el argumento matriz_1 y matriz_2 sean de tipo lista
        fila_matriz_1 = len(matriz_1) #Definimos la longitud de las filas de la matriz_1
        columna_matriz_1 = len(matriz_1[0]) #Definimos la longitud de las columnas de la matriz_1
        fila_matriz_2 = len(matriz_2) #Definimos la longitud de las filas de la matriz_2
        columna_matriz_2 = len (matriz_2[0]) #Definimos la longitud de las columnas de la matriz_2
        if columna_matriz_1 != fila_matriz_2:raise ValueError("No se puede ejecutar la multipicacion de matrices, el numero de filas de la primera matriz debe ser igual al numero de filas de la segunda matriz") #Verificamos la condicion de multiplicacion de matrices respecto a la filas y columnas
        C = [] #Creamos una lista C que sera el resultado de la mutiplicacion de matrices
        for i in range(len(matriz_1)): #Iteramos por cada elemento de la matriz _1 segun su longitud
            C.append([0]*(len(matriz_2[0])))#Generamos la dimension de la matriz C (filas x columnas) siendo el numero de columnas de la matriz_1 y el numero de filas de la matriz_2
        for i in range(len(matriz_1)): #Iteramos por cada elemento de la matriz_2 segun su longitud 
            for j in range(len(matriz_2[0])): #Iteramos por cada elemento de la matriz_2 en la posicion [0]
                for k in range(len(matriz_2)): C [i][j] += matriz_1[i][k]*matriz_2[k][j]#Multiplicamos cada elemento de las filas de la matriz_1 con cada elemento de las columnas de la matriz_2, sumando cada resultado para generar cada elemento de la matriz C
        print("\nEl resultado de la multiplicaión de matrices es:\n") #Imprimimos el resultado de la multiplicacion de las matrices
        for x in C: print(x) #Iteramos sobre cada elemento de la matriz C
    else:raise TypeError(" La Funcion Producto_Matricial solo acepta como entrada matrices que emulen el arreglo listas de listas") #Si el arreglo de las matrices no son de tipo listas de listas , arrojamos este error
    return matriz_1,matriz_2 
def Producto_Cruz(vectores):
    """Función para ejecutar el Producto Cruz entre dos vectores"""
    Final= []
    Resultado=[]
    aux=[]
    for j in vectores[0] and vectores[1]: #Iteramos sobre los elementos de los 2 vectores
        if type(j)==type("str"): #Verificamos si hay algun string dentro de ambos vectores
            aux.append(j) #Si se encuentra un string lo anexamos a la lista aux
    if len(aux)>=1: #Condicion para cuando la lista aux se llena 
        raise  TypeError("No se puede ingresar el tipo dato string, dentro de funcion Producto_Cruz") #Error correspondiente producto de que la lista aux se llene
    if len(vectores)==2: #Condiciones a ejecutar cuando la longitud del argumento es igual a  2 
        if (type(vectores[0]) and type(vectores[1]) and type(vectores))==list: #Condiciones a ejecutar cuando los elementos del argumento vectores son de tipo lista
            if len(vectores[0])==3 and len(vectores[1])==3: #Condiciones a ejecutar cuando los elementos [0] y [1] del argumento vectores son de tipo lista
                #Procedimiento matematico del producto cruz
                Multiplicacion_i=(vectores[0][1]*vectores[1][2])-(vectores[0][2]*vectores[1][1])
                Multiplicacion_j=-( (vectores[0][0]*vectores[1][2]) - (vectores[0][2]*vectores[1][0]) )
                Multiplicacion_k=  (vectores[0][0]*vectores[1][1]) - (vectores[0][1]*vectores[1][0])
                #Anexando cada uno de los resultados anteriores a la lista resultado
                Resultado.append(Multiplicacion_i)
                Resultado.append(Multiplicacion_j)
                Resultado.append(Multiplicacion_k)
                #Anexando resultado a la lista final para poder expresar la salida como una arreglo de lista de listas
                Final.append(Resultado)              
                print("\nEl resultado de la multiplicacion vectorial es: {}".format(Final)) #Imprimimos el resultado del Producto Cruz
            else:raise ValueError("La funcion Producto_Cruz solo acepta vectores con 3 componentes") #Error correspondiente 
        else:raise TypeError("La funcion Producto_Cruz solo acepta vectores, que emulen el arreglo listas de listas")  #Error correspondiente 
    else:raise ValueError("La funcion Producto_Cruz solo permite la entrada de dos vectores")#Error correspondiente 
    return vectores
def Transpuesta(matriz):
    """Función para ejecutar la matriz traspuesta de una matriz"""
    if type(matriz)==list: #Verificamos si el argumento matriz es de tipo lista
        aux=[]
        aux_2=[]
        for h in matriz: #Iteramos sobre cada elemento del argumento matriz
            if type(h)==list:aux.append(h) #Verificamos que cada elemento del argumento matriz sea de tipo lista y lo agregamos a la lista aux
            else:raise TypeError("Los elementos de la funcion Transpuesta deben ser de tipo lista") #Si la anterior condicion no se cumple arrojamos este error
            for j in h:  #Interamos sobre cada los elementos mas internos de la funcion matriz
                if type(j)==type("str"):aux_2.append(j) #Verificamos si hay un elemento de tipo string y lo anexamos a la lista aux_2
        for g in matriz: #Iteramos sobre cada elemento del argumento matriz
            if len(g)!=len(h):raise ValueError("Todas las filas deben tener la misma cantidad de columnas") #Planteamos la condicion de que las longitudes de cada elemento iterasado sean iguales 
        if len(aux_2)>=1:raise TypeError("No se puede ingresar tipo datos string dentro de la funcion Transpuesta") #Condicion para cuando la lista aux_2 es llenada
        if len(aux_2)==0: #Condicion a ejecutar para cuando la lista aux_2 no es llenada 
            if len(matriz)!=len(aux):print("\nLa funcion traspuesta, solo acepta elementos del tipo lista") #Condicion para cuando la longitud de matriz y aux son distintas
            if len(matriz)==len(aux): #Condicionj para cuando la longitud de  matriz y aux son iguales 
                filas = len(matriz) # Definimos las filas de matriz
                columnas = len(matriz[0]) #Definimos las columnas de la matriz
                print("\nMatriz Original\n") #Imprimimos la matriz original 
                for x in matriz:print(x) #Iteramos para mostrar el arreglo en forma de listas de listas e imprimimos
                Transposicion=[[matriz[j][i] for j in range(filas)] for i in range(columnas)]#Iteramos por cada elemento de las filas y columnas de la matriz trasponiendolas respectivamente
                print("\nMatriz Transpuesta\n") #Imprimimos encabezado
                for k in Transposicion:print(k) #Iteramos para mostrar el arreglo en forma de listas de listas e imprimimos
    else:print("La funcion traspuesta, solo permite la entrada de matrices que emulen el arreglo listas de listas") #Error correspondiente para cuando no seas un arreglo de listas de listas
    return matriz
def Determinante(matriz):
    """Función para ejecutar el determiante de una matriz"""
    aux=[]
    aux_2=[]
    for h in matriz: #Iteramos para cada elemento del argumento matriz
        if type(h)==list:aux.append(h) #Verificamos que cada elemento del argumento matriz sea de tipo lista y lo agregamos a la lista aux
        else:raise TypeError("La funcion Determinante solo permite la entrada tipo lista dentro de la funcion") #Errro para cuando no se cumple la condicion anterior
        for j in h: #Iteramos los elementos mas internos del argumentos matriz
            if type(j)==type("str"):aux_2.append(j) #Verificamos si hay algun elemento de tipo string y lo agregamos a la lista aux_2
    for g in matriz: #Iteramos sobre cada elemento del argumento matriz
        if len(g)!=len(h):raise ValueError("Todas las filas deben tener la misma cantidad de columnas") # Condicion planteada para que si cada iteracion tiene diferente longitud arroja el error correspondiente
    if len(aux_2)>=1:raise TypeError("No se puede ingresar tipo datos string dentro de la funcion Determinante") #Error correspondiente para cuando la lista aux_2 es llenada 
    if len(aux_2)==0: #Condiciona ejecutar para cuando la longitud de matriz y aux son distintas
        if len(matriz)!=len(aux):print("\nLa funcion determinante, solo acepta elementos del tipo lista")
    if type(matriz)==list: #Verificamos el tipo de dato del argumento matriz
        if len(matriz)==len(aux): #Condicion a ejecutar cuando la longitud de matriz y aux son iguales 
            n=len(matriz) #Definimos a "n" como la longitud del argumento matriz
            if len(matriz)==len(matriz[0]): #Planteamos condicion para cuando la matriz es cuadrada
                for z in range (n-1): #Iteramos por cada elemento de la matriz hasta la longitud de la matriz menos la ultima posicion
                    for x in range(1, n-z): #Iteramos por cada elemento de la matriz desde la segunda posicion hasta la longitud de la matriz menos la iteracion en "z"
                        if (matriz[z][z] != 0 ): #Condicion que se cumplira solo cuando la matriz en su posicion [z][z] sea distinta de cero
            #Procedimiento matemático para el cálculo del determinante usando el metodo de triangulación superior
                            p = matriz[x+z][z] / matriz[z][z] #Operacion para implantar los respectivos pivotes (unos) de forma escalonada en la matriz
                            for y in range (n):matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)#Operacion para implantar ceros debajo de los pivotes
                deter=1
                for x in range (n):deter=matriz[x][x]*deter
                print ('\nEl determinante de la matriz es = ',deter) #Imprimimos el resultado 
            else: raise ValueError("El determinante es solo para matrices cudradas") #Error correspondiente para cuando la matriz no es cuadrada
    else: raise TypeError("La funcion determinante solo acepta matrices que emulen el arreglo listas de listas") #Error correspondiente para cuando el argumento matriz no es tipo lista
    return matriz
