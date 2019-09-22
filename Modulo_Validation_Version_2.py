def valInt(*args):
    """Seccion de Ayuda para la Funcion valInt en el modulo Modulo_Validation:

    Descripcion de la Funcion valInt:

        La funcion valInt tiene como objetivo, validar si el tipo de dato ingresado es un numero entero para el caso de introducir un
        solo argumento y en el caso de dos argumentos, valida si el mismo se encuentra en el intervalo ingresado. Para el caso de un
        argumento la funcion solo acepta tipo de dato "int" y para el caso de dos argumento solo aceptara los de tipos de datos "list o tuple".

    Funciones que se pueden utilizar:

    Un solo Argumento:

        Caso 1: valInt(argumento)

            Retorna el valor Booleano "True" si el tipo de dato ingresado es int, de lo contrario retorna el valor Booleano "False".

    Dos argumentos:

        Caso 1: valInt(argumento, tuple)

            Retorna el valor Booleano "True" si el tipo de dato del primer argumento es int y esta dentro del intervalo descrito por el
            segundo argumento, (Sin incluir los numeros en los extremos), de lo contrario retorna el valor Booleano "False".

        Caso 2: valInt(argumento, list)

             Retorna el valor Booleano "True" si el tipo de dato del primer argumento es int y esta dentro del intervalo descrito por el
             segundo argumento, (Incluyendo los numeros en los extremos), de lo contrario retorna el valor Booleano "False".

        Caso 3: valInt(argumento,list o tuple)

            Salida "TypeError" si el segundo argumento recibe un tipo de dato distinto a list o tuple.

        Caso 4: valInt(argumento,list o tuple)

            Salida "ValueError" si el segundo argumento recibe una list o tuple organizada de manera decreciente o con una 
            dimension incongruente."""

    if len(args)==1:
        if type(args[0]) is int:
            resultado = True
        else:
            resultado = False
    elif len(args)==2:
        if type(args[1]) is not tuple and type(args[1]) is not list:
            raise TypeError("En el segundo argumento se esperaba un tipo list o tuple, y se introdujo: {}".format(type(args[1])))
        elif (args[1][0]>args[1][1] or (len(args[1])>2 or len(args[1])==0)):
            raise ValueError("El dato pasado en el segundo argumento debe tener dimensiones congruentes, revise la longitud de la lista pasada")
        elif  type(args[0]) is int and (type(args[1]) is list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[1]) is tuple and args[0]>args[1][0] and args[0]<args[1][1]):
            resultado = True
        else:
            resultado = False
    else:
        raise ValueError("Esta funcion solo acepta 1 o 2 argumentos y usted ingreso: {}".format(len(args)))
    return resultado

def valFloat(*args):
    """Seccion de Ayuda para la Funcion valFloat en el modulo Modulo_Validation:

    Descripcion de la Funcion valFloat:

        La funcion valFloat tiene como objetivo, validar si el tipo de dato ingresado es un numero decimal para el caso de introducir un
        solo argumento y en el caso de dos argumentos, valida si el mismo se encuentra en el intervalo ingresado. Para el caso de un solo
        argumento la funcion solo acepta tipo de dato "float" y para el caso de dos argumento solo aceptara los de tipos de datos "list o tuple".

    Funciones que se pueden utilizar:

    Un solo Argumento:

        Caso 1: valFloat(argumento)

             Retorna el valor Booleano "True" si el tipo de dato ingresado es float, de lo contrario retorna el valor Booleano "False".

    Dos argumentos:

        Caso 1: valFloat(argumento, tuple)

             Retorna el valor Booleano "True" si el tipo de dato del primer argumento es float y esta dentro del intervalo descrito 
             por el segundo argumento, (Sin incluir los numeros en los extremos), de lo contrario retorna el valor Booleano "False".

        Caso 2: valFloat(argumento, list)

             Retorna el valor Booleano "True" si el tipo de dato del primer argumento es float y esta dentro del intervalo descrito 
             por el segundo argumento, (Incluyendo los numeros en los extremos), de lo contrario retorna el valor Booleano "False".

        Caso 3: valFloat(argumento,list o tuple)

            Salida "TypeError" si el segundo argumento recibe un tipo de dato distinto a list o tuple.

        Caso 4: valFloat(argumento,list o tuple)

            Salida "ValueError" si el segundo argumento recibe una list o tuple organizada de manera decreciente o con una 
            dimension incongruente."""

    if len(args)==1:
        if type(args[0]) is float:
            resultado = True
        else:
            resultado = False
    elif len(args)==2:
        if type(args[1]) is not tuple and type(args[1]) is not list:
            raise TypeError("En el segundo argumento se esperaba un tipo list o tuple, y se introdujo: {}".format(type(args[1])))
        elif (args[1][0]>args[1][1] or (len(args[1])>2 or len(args[1])==0)):
            raise ValueError("El dato pasado en el segundo argumento debe tener dimensiones congruentes, revise la longitud de la lista pasada")
        elif  type(args[0]) is float and (type(args[1]) is list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[1]) is tuple and args[0]>args[1][0] and args[0]<args[1][1]):
            resultado = True
        else:
            resultado = False
    return resultado

def valComplex(*args):
    """Seccion de Ayuda para la Funcion valComplex en el modulo Modulo_Validation:

    Descripcion de la Funcion valFloat:

        La funcion valComplex tiene como objetivo, validar si el tipo de dato ingresado es un numero complejo para el caso de introducir un
        solo argumento y en el caso de dos argumentos, valida si el mismo se encuentra en el intervalo ingresado. Para el caso de un solo
        argumento la funcion solo acepta tipo de dato "complex" y para el caso de dos argumento solo aceptara los de tipos de datos "list o tuple".

    Funciones que se pueden utilizar:

    Un solo Argumento:

        Caso 1: valComplex(argumento)

             Retorna el valor Booleano "True" si el tipo de dato ingresado es complex, de lo contrario retorna el valor Booleano "False".

    Dos argumentos:

        Caso 1: valComplex(argumento, tuple)

            Retorna el valor Booleano "True" si el tipo de dato del primer argumento es complex y esta dentro del intervalo descrito por el
            segundo argumento, (Sin incluir los numeros en los extremos), de lo contrario retorna el valor Booleano "False".

        Caso 2: valComplex(argumento, list)

             Retorna el valor Booleano "True" si el tipo de dato del primer argumento es complex y esta dentro del intervalo descrito por el
             segundo argumento, (Incluyendo los numeros en los extremos), de lo contrario la salida Booleana se "False".

        Caso 3: valComplex(argumento,list o tuple)

            Salida "TypeError" si el segundo argumento recibe un tipo de dato distinto a list o tuple.

        Caso 4: valComplex(argumento,list o tuple)

             Salida "ValueError" si el segundo argumento recibe una list o tuple organizada de manera decreciente o con una 
             dimension incongruente."""

    if len(args)==1:
        if type(args[0]) is complex:
            resultado = True
        else:
            resultado = False
    elif len(args)==2:
        if type(args[1]) is not tuple and type(args[1]) is not list:
            raise TypeError("En el segundo argumento se esperaba un tipo list o tuple, y se introdujo: {}".format(type(args[1])))
        elif (args[1][0]>args[1][1] or (len(args[1])>2 or len(args[1])==0)):
            raise ValueError("El dato pasado en el segundo argumento debe tener dimensiones congruentes, revise la longitud de la lista pasada")
        elif  type(args[0]) is complex and (type(args[1]) is list and abs(args[0])>=args[1][0] and abs(args[0])<=args[1][1] or type(args[1]) is tuple and abs(args[0])>args[1][0] and abs(args[0])<args[1][1]):
            resultado = True
        else:
            resultado = False
    return resultado
def valList(*args):
    """Seccion de Ayuda para la Funcion valList en el modulo Modulo_Validation:

    Descripcion de la Funcion valList:

        La funcion valComplex tiene como objetivo, validar si el tipo de dato ingresado es una list para el caso de introducir un
        solo argumento y en el caso de 3 argumentos el mismo valida si el segundo y primer argumento son iguales en caso de que el
        tercer argumento sea igual a "value" y si el tercer argumento es "len" el mismo validara que la longitud del primer argumento
        coincida con el numero introducido en el segundo argumento.

    Funciones que se pueden utilizar:

    Un solo Argumento:

        Caso 1: valList(argumento)

             Retorna el valor Booleano "True" si el tipo de dato ingresado es list, de lo contrario retorna el valor Booleano "False".

    Tres argumentos:

        Caso 1: valList(argumento,argumento,"value")

            Retorna el valor Booleano "True" si el primer y segundo argumento son iguales, y a su vez son del tipo de dato list, 
            de lo contrario retorna el valor Booleano "False". En el caso del tercer argumento este debe ser igual a "value".

        Caso 2: valList(argumento,argumento,"len")

             Retorna el valor Booleano "True" si el tipo de dato del primer argumento es list y su longitud coincide con el 
             segundo argumento, de lo contrario retorna el valor Booleano "False". En el caso del tercer argumento 
             este debe ser igual a "len".

        Caso 3: valList(argumento,argumento,float)

            Salida "TypeError" si el segundo argumento y el tercer argumento recibe un tipo de dato distinto a int y str respectivamente.

        Caso 4: valList(argumento,argumento,int)

            Salida "TypeError" si el segundo argumento y el tercer argumento recibe un tipo de dato distinto a list y str respectivamente.

        Caso 5: valList(argumento,argumento,"hola")

            Salida "ValueError" si el tercer argumento sea distinto a "value" o "len"."""

    if len(args) == 1:
        if type(args[0]) is list:
            resultado = True
        else:
            resultado = False
    if len(args) == 3:
        if args[2] == "value":
            if type(args[0]) is list and type(args[1]) is list and args[0] == args[1]:
                resultado = True
            else:
                resultado = False
        if args[2] == "len":
            if type(args[0]) is list and len(args[0]) == args[1]:
                resultado = True
            else:
                resultado = False
        elif (type(args[1])!=type(4) and type(args[2])!=type("a")) or (type(args[1])!=type([4,6]) and type(args[2])!=type("a")):
            raise TypeError("Los datos ingresados en el segundo argumento y tercer argumento no son validos")
        elif args[2]!=("value" and "value"):
            raise ValueError("El tercer argumento solo permite como entrada (value o len) y usted introdujo: {}".format(args[2]))
    return resultado
