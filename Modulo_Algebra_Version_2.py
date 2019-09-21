from Modulo_Validation_Version_2 import valList,valInt,valFloat,valComplex

def Verificacion_1(matriz):
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
#print(Verificacion_1([[4,2,4],[4,5,8],[6,8,"hola"]]))

#def Arreglo_Matricial(m):
    #for i in range(0, len(m)): print(m[i])

def Producto_Cruz(vector_1,vector_2):
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
    if Verificacion_1(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        print("\nMatriz Original\n")
        print(matriz)
        Transposicion=[[matriz[j][i] for j in range(filas)] for i in range(columnas)]
        print("\nMatriz Transpuesta\n")
        return Transposicion
#print(Transpuesta_Matriz([[4,3,4],[2,3,4]]))

def Determinante_Matriz(matriz):
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
            resultado=(("\nEl determinante de la matriz es = {}  ").format(deter))
            return resultado
        else:
            raise ValueError("El determinante solo se le puede calcular a las matrices cudradas")
#print(Determinante_Matriz([[4,2,3],[8,6,4]]))

def Producto_Matricial(A,B):
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
        print("\nEl resultado de la multiplicaión de matrices es:\n")
        return C
#print(Producto_Matricial([[4,5,3]],[[0,1,0],[0,0,1]]))

def crearUno(fila, pos):
	divisor = fila[pos] * 1.0
	for e in range(0, len(fila)):
		fila[e] = fila[e] / divisor
	return fila #Se debe agregar la descripcion de tal funcion

def crearCero(fila, filaPivote, pos):
	multiplicador = -fila[pos] * 1.0
	for e in range(0, len(fila)):
		fila[e] = (filaPivote[e] * multiplicador) + fila[e]
	return fila #Se debe agregar la descripcion de tal funcion

def Matriz_Inversa(matriz):
    if Verificacion_1(matriz):
    	# Se crea la matriz identidad con el mismo orden que la matriz.
    	mIdentidad = [[0 for i in range(0, len(matriz))]
    	              for j in range(0, len(matriz))]
    	for i in range(0, len(mIdentidad)): mIdentidad[i][i] = 1

    	# Se amplia la matriz original para incluir la matriz identidad (A la derecha).
    	for i in range(0, len(matriz)): matriz[i].extend(mIdentidad[i])

    	# Se lleva a cabo el metodo de Gauss-Jordan. Mediante la creacion de unos y ceros, se "mueve" los valores de la matriz identidad
    	# a la izquierda. Al terminar de moverlos todos, los valores de la derecha seran los valores de la matriz inv.
    	for i in range(0, len(matriz)):
    		matriz[i] = crearUno(matriz[i], i)
    		for j in range(0, len(matriz)):
    			if i != j: matriz[j] = crearCero(matriz[j], matriz[i], i)

    	# Se eliminan los valores de la izquierda (Los de la matriz identidad). Asi, en la matriz quedan solo los valores de la inv.
    	for i in range(0, len(matriz)):
    		for j in range(0, len(matriz)): matriz[i].pop(0)

    	# Los valores estan representados con punto decimal, se convierten a un String indicando la fraccion correspondiente.
    	for i in range(0, len(matriz)):
    		for j in range(0, len(matriz)): matriz[i][j] = float(matriz[i][j])
    	print("\nMatriz Inversa:\n")

    	# La funcion regresa la matriz inv de la matriz parametro.
    	return matriz
#print(Matriz_Inversa([[1,0,0],[0,1,0],[0,0,1]]))

def Resolucion_Sistema_de_Ecuaciones(matriz_A,matriz_B):
    if Verificacion_1(matriz_A) and Verificacion_1(matriz_B):
        Resultado = Producto_Matricial(Matriz_Inversa(matriz_A),matriz_B)
        print("\n El resultado del sistema de ecuaciones es:\n")
        return Resultado
#print(Resolucion_Sistema_de_Ecuaciones([[1,2,4],[3,4,5],[5,6,5]],[[2],[1],[3]]))
