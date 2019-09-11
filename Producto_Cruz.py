def ProductoCruz(*args):
    Final=[]
    Resultado=[]
    if (type(args[0]) and type(args[0][0]) and type(args[0][1]))==list:
        if len(args[0])==2:
            if len(args[0][0])==3 and len(args[0][1])==3:
                Multiplicacion_i=(args[0][0][1]*args[0][1][2])-(args[0][0][2]*args[0][1][1])
                Multiplicacion_j=-( (args[0][0][0]*args[0][1][2]) - (args[0][0][2]*args[0][1][0]) )
                Multiplicacion_k=  (args[0][0][0]*args[0][1][1]) - (args[0][0][1]*args[0][1][0])
                Resultado.append(Multiplicacion_i)
                Resultado.append(Multiplicacion_j)
                Resultado.append(Multiplicacion_k)
                Final.append(Resultado)
                print("\nEl resultado de la multiplicacion vectorial es: {}".format(Final))
            else:print("\nUsted debe ingresar vectores con 3 componentes")
        else:print("\nUsted debe ingresar unicamente dos vectores.")
    else:print("\nLa funcion solo acepta vectores, que emulen un arreglo de listas de listas")
    return args
