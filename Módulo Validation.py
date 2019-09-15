def valInt(*args):
    """Funcion valInt"""
    #Verificamos que el tipo de dato sea int para cuando se ingresa solo un argumento
    
    if len(args)==1:print(isinstance(args[0],int))
        
    #Verificaciones para cuando se ingresan dos argumentos  
    
    if len(args)==2:
        
        #Verificamos las condiciones e imprimimos la salidas respectivas para el caso de que sea True o False
        
        if args[1][0]<args[1][1]:print("True") if type(args[0])==int and type(args[1])==list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[0])==int and type(args[1])==tuple and args[0]>args[1][0] and args[0]<args[1][1] else print("False")
        
        #Verificamos que el tipo de dato del segundo argumento sea lista o tupla y arrojamos el error correspondiente 
        
        if type(args[1])!=list and type(args[1])!=tuple :raise TypeError("El segundo argumento solo recibe tipo lista o tupla y usted ha ingresado: {}".format(type(args[1])))
        
        #Verificamos que el segundo argumento este ordenando de manera creciente y arrojamos el error correspondiente
        
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
    
    #Verificacion para el caso que hallan mas de 2 o no haya ningun argumento en la funcion
    
    if len(args)>2 or len(args)==0: print("La fauncion vallnt solo acepta 1 o 2 argumentos")
    
    return args
def valFloat(*args):
    """Funcion valFloat"""
    
    #Verificamos que el tipo de dato sea float para cuando se ingresa solo un argumento
    
    if len(args)==1:print(isinstance(args[0],float))
    
    #Verificaciones para cuando se ingresan dos argumentos  
    
    if len(args)==2:
        
        #Verificamos las condiciones e imprimimos la salidas respectivas para el caso de que sea True o False     
        
        if args[1][0]<args[1][1]:print("True") if type(args[0])==float and type(args[1])==list and args[0]>=args[1][0] and args[0]<=args[1][1] or type(args[0])==float and type(args[1])==tuple and args[0]>args[1][0] and args[0]<args[1][1] else print("False")
        
        #Verificamos que el tipo de dato del segundo argumento sea lista o tupla y arrojamos el error correspondiente        
        
        if type(args[1])!=list and type(args[1])!=tuple:raise TypeError("El segundo argumento solo recibe tipo lista o tupla y usted ha ingresado: {}".format(type(args[1])))
        
        #Verificamos que el segundo argumento este ordenando de manera creciente y arrojamos el error correspondiente
        
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
    
    #Verificacion para el caso que hallan mas de 2 o no haya ningun argumento en la funcion
    
    if len(args)>2 or len(args)==0:print("La funcion valFloat solo acepta 1 o 2 argumentos")
    
    return args
def valComplex(*args):
    """Funcion valComplex"""
    
    #Verificamos que el tipo de dato sea complex para cuando se ingresa solo un argumento
    
    if len(args)==1:print(isinstance(args[0],complex))
    
    #Verificaciones para cuando se ingresan dos argumentos  
    
    if len(args)==2:
        
        #Verificamos las condiciones e imprimimos la salidas respectivas para el caso de que sea True o False            
        
        if args[1][0]<args[1][1]:print("True") if type(args[0])==complex and type(args[1])==list and abs(args[0])>=args[1][0] and abs(args[0])<=args[1][1] or type(args[0])==complex and type(args[1])==tuple and abs(args[0])>args[1][0] and abs(args[0])<args[1][1] else print("False")
        
        #Verificamos que el tipo de dato del segundo argumento sea lista o tupla y arrojamos el error correspondiente    
        
        if type(args[1])!=list and type(args[1])!=tuple:raise TypeError("El segundo argumento solo recibe tipo lista o tupla y usted ha ingresado: {}".format(type(args[1])))
        
        #Verificamos que el segundo argumento este ordenando de manera creciente y arrojamos el error correspondiente
        
        if args[1][0]>args[1][1] or len(args[1])>2: raise ValueError("El segundo argumento no puede estar ordenado de manera decreciente")
    
    #Verificacion para el caso que hallan mas de 2 o no haya ningun argumento en la funcion
    
    if len(args)>2 or len(args)==0:print("La funcion valFloat solo acepta 1 o 2 argumentos")
    
    return args
def valList(*args):
    """Funcion valList"""
    
    #Verificamos que el tipo de dato sea lista para cuando se ingresa solo un argumento
    
    if len(args)==1:print(isinstance(args[0],list))
    
    #Verificaciones para cuando se ingresan tres argumentos 
    
    if len(args)==3:
        
        #Verificamos las condiciones e imprimimos la salidas respectivas para el caso de que sea True o False            
        
        print("True") if type(args[0])==list and type(args[1])==list and args[2]=="value" and args[0]==args[1] or args[2]=="len" and type(args[0])==list and type(args[1])==int and len(args[0])==args[1] else print("False")
        
        #Verificamos las condiciones e imprimimos los errores correspondientes          
        
        if type(args[1])!=int and type(args[2])!=type("str") or type(args[2])!=type("str") and type(args[1])!=list: raise TypeError("La combinacion de los argumentos 2 y 3 son invalidos")
        
        #Verificamos las condiciones e imprimimos los errores correspondientes          
        
        if args[2]!="len" and args[2]!="value": raise ValueError("El tercer argumento solo admite 2 entradas (len ó value) y usted ha ingresado: {}".format(args[2]))
    
    #Verificacion para el caso que hallan 2 o mas de 3 argumento en la funcion
    
    if len(args)==2 or len(args)>3 or len(args)==0: print("La funcion valList solo acepta 1 o 3 argumentos")
    
    return args
