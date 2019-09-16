def valInt(*args):
    """Docstring"""
    if len(args)==1:
        if type(args[0]) is int:
            resultado = True
        else:
            resultado = False
    elif len(args)==2:
        if type(args[1]) is not tuple and type(args[1]) is not list:
            raise TypeError("En el segundo argumento se esperaba un tipo lista o tupla, y se introdujo: {}".format(type(args[1])))
        elif (args[1][0]>args[1][1] or (len(args[1])>2 or len(args[1])==0)):
            raise ValueError("El dato pasado en el segundo argumento debe tener dimensiones congruentes, revise la longitud de la lista pasada")
        elif ( (type(args[0]) is int and type(args[1]) is int or tuple) and (args[0]>=args[1][0] and args[0]<=args[1][1]) ):
            resultado = True
        elif not ( (type(args[0]) is int and type(args[1]) is int or tuple) and (args[0]>=args[1][0] and args[0]<=args[1][1]) ):
            resultado= False
    else:
        raise ValueError("Esta funcion solo acepta 1 o 2 argumentos y usted ingreso: {}".format(len(args)))
    return resultado

print(valInt(1,[4,8]))
