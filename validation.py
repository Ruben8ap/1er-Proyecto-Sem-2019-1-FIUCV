def valInt(*args):
    """ DocString """
    if len(args)==1:print(isinstance(args[0],int))
    if len(args)==2:
        if args[1][0]<args[1][1]:print("True") if type(args[0])==int and type(args[1])==list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[0])==int and type(args[1])==tuple and args[0]>args[1][0] and args[0]<args[1][1] else print("False")
    if type(args[1])!=list and type(args[1])!=tuple :raise TypeError("El segundo argumento solo recibe tipo lista o tupla y usted ha ingresado: {}".format(type(args[1])))
    if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
    if len(args)>2 or len(args)==0: print("La fauncion vallnt solo acepta 1 o 2 argumentos")
    return args
def valFloat(*args):
    """DocString"""
    if len(args)==1:print(isinstance(args[0],float))
    if len(args)==2:
        print("True") if type(args[0])==float and type(args[1])==list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[0])==float and type(args[1])==tuple and args[0]>args[1][0] and args[0]<args[1][1] else print("False")
        if type(args[1])!=list and type(args[1])!=tuple:raise TypeError("El segundo argumento solo recibe tipo lista o tupla y usted ha ingresado: {}".format(type(args[1])))
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
    if len(args)>2 or len(args)==0:print("La funcion valFloat solo acepta 1 o 2 argumentos")
    return args
def valComplex(*args):
    """DocString"""
    if len(args)==1:print(isinstance(args[0],complex))
    if len(args)==2:
        print("True") if type(args[0])==complex and type(args[1])==list and abs(args[0])>=args[1][0] and abs(args[0])<=args[1][1] or type(args[0])==complex and type(args[1])==tuple and abs(args[0])>args[1][0] and abs(args[0])<args[1][1] else print("False")
        if type(args[1])!=list and type(args[1])!=tuple:raise TypeError("El segundo argumento solo recibe tipo lista o tupla y usted ha ingresado: {}".format(type(args[1])))
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
    if len(args)>2 or len(args)==0:print("La funcion valFloat solo acepta 1 o 2 argumentos")
    return args
def valList(*args):
    """DocString"""
    if len(args)==1:print(isinstance(args[0],list))
    if len(args)==3:
        print("True") if type(args[0])==list and type(args[1])==list and args[2]=="value" and args[0]==args[1] or args[2]=="len" and type(args[0])==list and type(args[1])==int and len(args[0])==args[1] else print("False")
        if type(args[1])!=int and type(args[2])!=type("str") or type(args[2])!=type("str") and type(args[1])!=list: raise TypeError("La combinacion de los argumentos 2 y 3 son invalidos")
        if args[2]!="len" and args[2]!="value": raise ValueError("El tercer argumento solo admite 2 entradas (len ó value) y usted ha ingresado: {}".format(args[2]))
    if len(args)==2 or len(args)>3 or len(args)==0: print("La funcion valList solo acepta 1 o 3 argumentos")
    return args
