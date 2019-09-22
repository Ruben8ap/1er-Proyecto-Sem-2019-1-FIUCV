from Modulo_Validation_Version_2 import valList,valInt,valFloat,valComplex

def Verificacion_1(matriz):
    """Seccion de Ayuda para la Funcion Verificacion_1 en el modulo Modulo_Algebra:

    Descripcion de la Funcion Verificacion_1:

    Funciones que se pueden utilizar:

    Un solo argumento: """
    if type(matriz) is list:
        for i in matriz:
            for j in i:
                if valInt(j) or valFloat(j):
                    Comprobacion = True
                else:
                    raise ValueError("Solo debe ingresar tipo de dato int o float")
        if Comprobacion==True:
            filas = len(matriz)
            columnas = len(matriz[0])
            for i in matriz:
                if not valList(i,columnas,"len"):
                    raise ValueError("El dato pasado debe tener dimensiones congruentes y debe ser tipo lista, revise la longitud de las listas pasadas como argumentos.")
                else:
                    Comprobacion = True
    else:
        raise TypeError("Se como esperaba como entrada un tipo lista y usted ha ingresado un tipo: {}".format(type(matriz)))
    return Comprobacion
#print(Verificacion_1([[4,2,4],[4,5,8],[6,8,4.8]]))

def Arreglo_Matricial(m):
    """Seccion de Ayuda para la Funcion Arreglo_Matricial en el modulo Modulo_Algebra:

    Descripcion de la Arreglo_Matricial:

    Funciones que se pueden utilizar:

    Un solo argumento:"""
    for i in range(0, len(m)): print(m[i])
    return ""

def Producto_Cruz(vector_1,vector_2):
    """Seccion de Ayuda para la Funcion Producto_Cruz en el modulo Modulo_Algebra:

    Descripcion de la Funcion Producto_Cruz:

    Funciones que se pueden utilizar:

    Dos argumentos:"""
    Resultado=[]
    Final=[]
    if Verificacion_1(vector_1) and Verificacion_1(vector_2) and len(vector_1[0])==3 and len(vector_2[0])==3:
        Multiplicacion_i=(vector_1[0][1]*vector_2[0][2])-(vector_1[0][2]*vector_2[0][1])
        Multiplicacion_j=-( (vector_1[0][0]*vector_2[0][2]) - (vector_1[0][2]*vector_2[0][0]) )
        Multiplicacion_k= (vector_1[0][0]*vector_2[0][1]) - (vector_1[0][1]*vector_2[0][0])
        Resultado.append(Multiplicacion_i)
        Resultado.append(Multiplicacion_j)
        Resultado.append(Multiplicacion_k)
        Final.append(Resultado)
        print("\nEl resultado del producto cruz es:\n")
        return Final
    else:
        raise ValueError("La dimension de los vectores debe estar en R3")
#print(Producto_Cruz([[4,3,4]] ,[[4,3,8]]))

def Transpuesta_Matriz(matriz):
    """Seccion de Ayuda para la Funcion Transpuesta_Matriz en el modulo Modulo_Algebra:

    Descripcion de la Funcion Transpuesta_Matriz:

    Funciones que se pueden utilizar:

    Un solo argumento: """
    if Verificacion_1(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        print("\nMatriz Original\n")
        Arreglo_Matricial(matriz)
        Transposicion=[[matriz[j][i] for j in range(filas)] for i in range(columnas)]
        print("\nMatriz Transpuesta\n")
        return Transposicion
#print(Arreglo_Matricial(Transpuesta_Matriz([[4,3,4],[2,3,4]])))

def Determinante_Matriz(matriz):
    """Seccion de Ayuda para la Determinante_Matriz en el modulo Modulo_Algebra:

    Descripcion de la Funcion Determinante_Matriz:

    Funciones que se pueden utilizar:

    Un solo argumento: """
    if Verificacion_1(matriz):
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
            return deter
        else:
            raise ValueError("El determinante solo se le puede calcular a las matrices cudradas")
#print("\nEl Determinante de la matriz es =",Determinante_Matriz([[1,0,0],[0,1,0],[0,0,1]]))

def Producto_Matricial(A,B):
    """Seccion de Ayuda para la Producto_Matricial en el modulo Modulo_Algebra:

    Descripcion de la Funcion Producto_Matricial:

    Funciones que se pueden utilizar:

    Dos argumentos:  """
    if Verificacion_1(A) and Verificacion_1(B):
        fila_A = len(A)
        columna_A = len(A[0])
        fila_B = len(B)
        columna_B = len (B[0])
        if columna_A != fila_B:
            Mensaje = "\nNo se puede realizar la multipicacion de matrices, las dimensiones correspondientes no coinciden"
            return Mensaje
        C = []
        for i in range(len(A)):C.append([0]*(len(B[0])))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)): C [i][j] += A[i][k]*B[k][j]
        return C
#print("\nResultado de la multiplicaión de matrices\n",Arreglo_Matricial(Producto_Matricial([[1,0,0],[0,0,0],[0,0,0]],[[1,0,0],[0,1,0],[0,0,1]])))

def crearUno(fila, pos):
    """Seccion de Ayuda para la Funcion crearUno en el modulo Modulo_Algebra:

    Descripcion de la Funcion crearUno:

    Funciones que se pueden utilizar:

    Dos argumentos: """
	divisor = fila[pos] * 1.0
	for e in range(0, len(fila)):
		fila[e] = fila[e] / divisor
	return fila

def crearCero(fila, filaPivote, pos):
    """Seccion de Ayuda para la Funcion crearCero en el modulo Modulo_Algebra:

    Descripcion de la Funcion crearCero:

    Funciones que se pueden utilizar:

    Dos argumentos:  """
	multiplicador = -fila[pos] * 1.0
	for e in range(0, len(fila)):
		fila[e] = (filaPivote[e] * multiplicador) + fila[e]
	return fila

def Matriz_Inversa(matriz):
    """Seccion de Ayuda para la Funcion Matriz_Inversa en el modulo Modulo_Algebra:

    Descripcion de la Funcion Matriz_Inversa:

    Funciones que se pueden utilizar:

    Un solo argumento: """
    if Determinante_Matriz(matriz)!=0:
        if Verificacion_1(matriz):
        	mIdentidad = [[0 for i in range(0, len(matriz))]
        	              for j in range(0, len(matriz))]
        	for i in range(0, len(mIdentidad)): mIdentidad[i][i] = 1
        	for i in range(0, len(matriz)): matriz[i].extend(mIdentidad[i])
        	for i in range(0, len(matriz)):
        		matriz[i] = crearUno(matriz[i], i)
        		for j in range(0, len(matriz)):
        			if i != j: matriz[j] = crearCero(matriz[j], matriz[i], i)
        	for i in range(0, len(matriz)):
        		for j in range(0, len(matriz)): matriz[i].pop(0)
        	for i in range(0, len(matriz)):
        		for j in range(0, len(matriz)): matriz[i][j] = int(matriz[i][j])
        return matriz
    else:
        raise ValueError("La matriz ingresada no posee inversa, debido a que su determinante es igual a cero.")
#print("\nMatriz Inversa",Arreglo_Matricial(Matriz_Inversa([[1,0,0],[0,1,0],[0,0,1]])))

def Resolucion_Sistema_de_Ecuaciones(matriz_A,matriz_B):
    """Seccion de Ayuda para la Funcion Resolucion_Sistema_de_Ecuaciones en el modulo Modulo_Algebra:

    Descripcion de la Funcion Resolucion_Sistema_de_Ecuaciones:

    Funciones que se pueden utilizar:

    Dos argumentos: """
    if Verificacion_1(matriz_A) and Verificacion_1(matriz_B):
        print("\nEl resultado del sistema de ecuaciones es:\n")
        return Producto_Matricial(Matriz_Inversa(matriz_A),matriz_B)
#print(Resolucion_Sistema_de_Ecuaciones([[1,2,4],[3,4,5],[5,6,5]],[[2],[1],[3]]))
