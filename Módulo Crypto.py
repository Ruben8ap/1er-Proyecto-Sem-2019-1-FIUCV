#Se le debe preguntar al Prof. si es necesario la encriptación de los números en las cadenas de texto
def Codificar(texto):
    """Funcion para Cifrar un texto, con el Cifrado Cesar"""
    Desplazamiento=2 #Indicamos el desplazamiento que se ejecutara para cada letra 
    Cifrado="" #Creamos la cadena de texto cifrado 
    if texto==texto.upper():lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z" #Verificamos que cada elemento de texto este integrado a esta lista
    else:lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z" #De no ser asi entonces lo arrojamos a la lista de las letras minusculas
    for caracteres in texto: #Verificamos sobre cada caracteres del argumento texto
        #Planteamos la condicion de que cada caracter que se encuentra en la lista se agregue a cifrado , buscandolo en la lista correspondiente sea mayuscula o minuscula con la condicion del desplazamiento. 
        if caracteres in lista:Cifrado += lista[(lista.index(caracteres)+Desplazamiento%(len(lista)))] 
        #De no cumplirse y no estar en la lista anteriormente mencionada dejamos tal cual los cacteres indicaos en texto   
        else:Cifrado+=caracteres
    print(Cifrado)#Imprimimos el mensaje cifrado 
    return Cifrado
def Descodificar(texto):
    """Funcion para Descodificar un texto, con el Cifrado Cesar"""
    Desplazamiento=2 #Indicamos el desplazamiento que se ejecutara para cada letra 
    Descifrado="" #Creamos la cadena de texto descifrado 
    if texto==texto.upper():lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z" #Verificamos que cada elemento de texto este integrado a esta lista
    else:lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z" #De no ser asi entonces lo arrojamos a la lista de las letras minusculas
    for caracteres in texto: #Verificamos sobre cada caracteres del argumento texto
        if caracteres in lista: Descifrado += lista[(lista.index(caracteres)-Desplazamiento%(len(lista)))] #Realizamos la operacion inversa a la funcion cifrado 
        else: Descifrado+=caracteres #De no cumplirse y no estar en la lista anteriormente mencionada dejamos tal cual los cacteres indicaos en texto   
    print(Descifrado) #Imprimimos el mensaje descifrado 
    return Descifrado
