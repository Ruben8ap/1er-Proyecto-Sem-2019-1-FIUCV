from Modulo_Validation import valList,valInt,valFloat,valComplex

def Verificacion_1(matriz):
    """Seccion de Ayuda para la Funcion Verificacion_1 en el modulo Modulo_Algebra:

    Descripcion de la Funcion Verificacion_1:

        El objetivo de la funcion Verificacion_1 es validar los tipos de datos ingresados como datos, asi como la verifiacion de
        que el argumento introducido tenga dimensiones congruentes en el ambito matematico.

    Funcionamiento de la funcion Verificacion_1:

    Un solo argumento:

        Caso 1: Verificacion_1(matriz)

            Caracteristicas principales de matriz:

                *Tipo de dato list
                *Igual longitud entre todas las listas ingresadas.
                *Los elementos de cada una de las listas ingresadas son de tipo "int" o "float".

                La funcion retornara el valor Booleano "True" asignada a la variable Comprobacion.

        Caso 2: Verificacion_1(matriz)

            Caracteristicas principales de matriz:

                *Los elementos de cada una de las listas ingresadas son distintas a los tipos
                 de datos "int" o "float".

                 La funcion tendra como salida un ValueError.

        Caso 3: Verificacion_1(matriz)

            Caracteristicas principales de matriz:

                *Los elementos de cada una de las listas ingresadas son de tipo "int" o "float"
                *Distintas longitudes entre todas las listas ingresadas.

                La funcion tendra como salida un ValueError.

        Caso 4: Verificacion_1(matriz)

            Si matriz es de tipo lista, la funcion tendra como salida un TypeError."""
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

        El objetivo de la función Arreglo_Matricial es proporcionar un arreglo fila por fila de la matriz ingresada por el usuario"""
    for i in range(0, len(m)): print(m[i])
    return ""

def Producto_Cruz(vector_1,vector_2):
    """Seccion de Ayuda para la Funcion Producto_Cruz en el modulo Modulo_Algebra:

    Descripcion de la Funcion Producto_Cruz:

        El objetivo de la funcion Producto_Cruz, es proporcionar el resultado de la operacion matematica Producto Vectorial, aplicada
        a vector_1 y a vector_2.

    Funcionamiento de la funcion Producto_Cruz:

    Dos argumentos:

        Caso 1: Producto_Cruz(vector_1,vector_2)

            Si vector_1 y vector_2 son aprobadas por la funcion Verificacion_1 y la longitud de las mismos son igual 3
            entonces se retornara la variable Final (resultado matematico del producto cruz).

        Caso 2: Producto_Cruz(vector_1,vector_2)

            Si vector_1 y vector_2 no son aprobadas por la funcion Verificacion_1 o la longitud de las mismas son distintas a 3
            entonces se tendra como salida un ValueError."""
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

        El objetivo de la funcion Transpuesta_Matriz, es proporcionar al usuario la matriz transpuesta del argumento matriz.

    Funcionamiento de la funcion Transpuesta_Matriz:

    Un solo argumento:

        Caso 1: Transpuesta_Matriz(matriz)

            Si matriz es aprobada por la funcion Verificacion_1, entonces la funcion retornara la variable Transposicion
            (resultado matematico de la matriz transpuesta).

        Caso 2: Transpuesta_Matriz(matriz)

            Si matriz no es aprobada por la funcion Verificacion_1, entonces la funcion retornara el caso correspondiente
            segun los lineamientos de la misma."""
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

        El objetivo de la funcion Determinante_Matriz es mostrar el determinante del argumento matriz.

    Funcionamiento de la funcion Determinante_Matriz:

    Un solo argumento:

        Caso 1: Determinante_Matriz(matriz)

            Si matriz es aprobada por la funcion Verificacion_1 y la longitud de matriz es igual a la longitud  del primer elemento
            de matriz, entonces la funcion retornara a deter (resultado, determinante de la matriz)

        Caso 2: Determinante_Matriz(matriz)

            Si matriz es aprobada por la funcion Verificacion_1 pero la longitud de matriz es distinta a la longitud  del primer elemento
            de matriz, entonces la funcion tendra como salida un ValueError.

        Caso 3: Determinante_Matriz(matriz)

            Si matriz no es aprobada por la funcion Verificacion_1, la misma retornara el caso correspondiente a los lineamientos
            de la misma."""
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
    """Seccion de Ayuda para la Funcion Producto_Matricial en el modulo Modulo_Algebra:

    Descripcion de la Funcion Producto_Matricial:

        El objetivo de la funcion Producto_Matricial, es proporcionar el resutado de la multiplicacion de matrices entre A y B.

    Funcionamiento de la funcion Producto_Matricial:

    Dos argumentos:

        Caso 1: Producto_Matricial(A,B)

            Si A y B son aprobadas por la funcion Verificacion_1, y las columnas de A son igual a las filas de B, entonces
            la funcion retornara la variable C , la cual es el resultado de la multiplicacion matricial.

        Caso 2: Producto_Matricial(A,B)

            Si A y B son aprobadas por la funcion Verificacion_1, pero las columnas de A son distintas a las filas de B,
            entonces la funcion retornata la variable Mensaje.

        Caso 3: Producto_Matricial(A,B)

            Si A y B no son aprobadas por la funcion Verificacion_1,la misma retornara el caso correspondiente a los lineamientos
            de la misma.
            """
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

        El objetivo de la función crearUno es introducir "unos" en la diagonal principal de la matriz proporcionada
        por el usuario en la función de Matriz_Inversa a traves de operaciones algebraicas.

    Funcionamiento de la funcion crearUno:

    Dos argumentos:

        Caso 1: crearUno(fila,pos)

        Si la función de la Matriz_Inversa(matriz) es aprobada por la función Determinante_Matriz y Verificacion_1, entonces
        la función retornara las filas modificadas para el método de Gauss Jordan"""
    divisor=fila[pos] * 1.0
    for e in range(0, len(fila)):
        fila[e] = fila[e] / divisor
    return fila

def crearCero(fila, filaPivote, pos):
    """Seccion de Ayuda para la Funcion crearCero en el modulo Modulo_Algebra:

    Descripcion de la Funcion crearCero:

        El objetivo de la función crearCero, es introducir "ceros" arriba y debajo de los "unos" usados como pivotes en
        las filas de la matriz proporcionada por el usuario en la función Matriz_Inversa a traves de operaciones algebraicas

    Funcionamiento de la funcion crearCero:

    Tres argumentos:

        Caso 1: crearCero(fila, filaPivote, pos)

            Si la función de la Matriz_Inversa(matriz) es aprobada por la función Determinante_Matriz y Verificacion_1, entonces
            la función retornara las filas modificadas para el método de Gauss Jordan"""
    multiplicador = -fila[pos] * 1.0
    for e in range(0, len(fila)):
        fila[e] = (filaPivote[e] * multiplicador) + fila[e]
    return fila

def Matriz_Inversa(matriz):
    """Seccion de Ayuda para la Funcion Matriz_Inversa en el modulo Modulo_Algebra:

    Descripcion de la Funcion Matriz_Inversa:

        El ojetivo de la funcion Matriz_Inversa, es proporcionar al usuario la matriz inversa del argumento matriz.

    Funcionamiento de la funcion Matriz_Inversa:

    Un solo argumento:

        Caso 1: Matriz_Inversa(matriz)

            Si la funcion Determinante_Matriz y la funcion Verificacion_1 aprueban a matriz, entonces la funcion retornara
            a matriz (matriz inversa).

        Caso 2: Matriz_Inversa(matriz)

            Si la funcion Determinante_Matriz no aprueba a matriz, entonces la funcion tendra como salida un ValueError.

        Caso 3: Matriz_Inversa(matriz)

            Si matriz no es aprobada por la funcion Verificacion_1,la misma retornara el caso correspondiente a los lineamientos
            de la misma."""
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
#print("\nMatriz Inversa",Arreglo_Matricial(Matriz_Inversa([["hola",0,0],[0,1,0],[0,0,1]])))

def Resolucion_Sistema_de_Ecuaciones(matriz_A,matriz_B):
    """Seccion de Ayuda para la Funcion Resolucion_Sistema_de_Ecuaciones en el modulo Modulo_Algebra:

    Descripcion de la Funcion Resolucion_Sistema_de_Ecuaciones:

        El objetivo de la funcion Resolucion_Sistema_de_Ecuaciones, es dar el resultado del sistema ecuaciones ingresado
        en forma matricial, es decir matriz_A y matriz_B.

    Funcionamiento de la funcion Resolucion_Sistema_de_Ecuaciones:

    Dos argumentos:

        Caso 1: Resolucion_Sistema_de_Ecuaciones(matriz_A,matriz_B)

            Si la funcion Verificacion_1 aprueba a matriz_A y matriz_B, entonces la funcion retornara la funcion Producto_Matricial
            aplicada a matriz_A (la cual tiene aplicada la funcion Matriz_Inversa) y a matriz_B.

        Caso 2: Resolucion_Sistema_de_Ecuaciones(matriz_A,matriz_B)

            Si matriz_A y matriz_B no son aprobadas por la funcion Verificacion_1,la misma retornara el caso correspondiente a los lineamientos
            de la misma.

        Caso 3: Resolucion_Sistema_de_Ecuaciones(matriz_A,matriz_B)

            Si matriz_A y matriz_B  son aprobadas por la funcion Verificacion_1, pero no son aprobadas por la funcion Producto_Matricial
            o la funcion Matriz_Inversa, las mismas retornaran el caso correspondiente a los lineamientos de la cada una de ellas."""
    if Verificacion_1(matriz_A) and Verificacion_1(matriz_B):
        return Producto_Matricial(Matriz_Inversa(matriz_A),matriz_B)
#print("\nEl resultado del sistema de ecuaciones es:",Resolucion_Sistema_de_Ecuaciones([[1,1,4],[3,1,5],[5,9,5]],[[2],[1],[3]]))
