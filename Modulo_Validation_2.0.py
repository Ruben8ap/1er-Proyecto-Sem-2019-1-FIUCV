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
        elif  type(args[0]) is int and (type(args[1]) is list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[1]) is tuple and args[0]>args[1][0] and args[0]<args[1][1]):
            resultado = True
        else:
            resultado = False
    else:
        raise ValueError("Esta funcion solo acepta 1 o 2 argumentos y usted ingreso: {}".format(len(args)))
    return resultado
#print(valInt(1,[2,9]))

def valFloat(*args):
    if len(args)==1:
        if type(args[0]) is float:
            resultado = True
        else:
            resultado = False
    elif len(args)==2:
        if type(args[1]) is not tuple and type(args[1]) is not list:
            raise TypeError("En el segundo argumento se esperaba un tipo lista o tupla, y se introdujo: {}".format(type(args[1])))
        elif (args[1][0]>args[1][1] or (len(args[1])>2 or len(args[1])==0)):
            raise ValueError("El dato pasado en el segundo argumento debe tener dimensiones congruentes, revise la longitud de la lista pasada")
        elif  type(args[0]) is float and (type(args[1]) is list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[1]) is tuple and args[0]>args[1][0] and args[0]<args[1][1]):
            resultado = True
        else:
            resultado = False
    return resultado
#print(valFloat(1.5,(1.4,9)))

def valComplex(*args):
    if len(args)==1:
        if type(args[0]) is complex:
            resultado = True
        else:
            resultado = False
    elif len(args)==2:
        if type(args[1]) is not tuple and type(args[1]) is not list:
            raise TypeError("En el segundo argumento se esperaba un tipo lista o tupla, y se introdujo: {}".format(type(args[1])))
        elif (args[1][0]>args[1][1] or (len(args[1])>2 or len(args[1])==0)):
            raise ValueError("El dato pasado en el segundo argumento debe tener dimensiones congruentes, revise la longitud de la lista pasada")
        elif  type(args[0]) is complex and (type(args[1]) is list and abs(args[0])>=args[1][0] and abs(args[0])<=args[1][1] or type(args[1]) is tuple and abs(args[0])>args[1][0] and abs(args[0])<args[1][1]):
            resultado = True
        else:
            resultado = False
    return resultado
#print(valComplex(20j+5,"hola"))

def valList(*args):
    """Docstring"""
    if len(args) == 1:
        if type(args[0]) is list:
            resultado = True
        else:
            resultado = False
    if len(args) == 3:
        if ( type(args[1]) is not int or type(args[1]) is not list ) and type(args[2]) is not "str":
            raise TypeError("Los datos ingresados en el segundo argumento y tercer argumento no son validos")
        if args[2]!=("len" or "value"):
            raise ValueError("El tercer argumento solo permite como entrada (value o len) y usted introdujo: {}".format(args[2]))
        elif args[2] == "value" and type(args[0]) is list and type(args[1]) is list and args[0] == args[1]:
            resultado = True
        elif args[2] == "len" and type(args[0]) is list and len(args[0]) == args[1]:
            resultado = True
        #elif args[2] == "value" and (type(args[0]) is not list or type(args[1]) is not list or args[0] != args[1]):
            #resultado = False
        #elif args[2] == "len" and (type(args[0]) is not list or len(args[0]) != args[1]):
            #resultado = False
        else:
            resultado = False
    return resultado
#print(valList([4,2,5],"hola",4))
