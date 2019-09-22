def Codificar(texto):
    """Seccion de Ayuda para la Funcion Codificar en el modulo Modulo_Crypto:

    Descripcion de la Funcion Codificar:

        Esta funcion, tiene como objetivo Cifrar las cadenas de texto con el tipo de cifrado Cesar.

    Funcionamiento de la funcion Codificar:

        La funcion codificar esta basada en el cifrado César, la misma mueve cada letra un determinado número de espacios en el alfabeto.
        Y la va remplazando a medida que va recorriendo la cadena de texto."""
    Desplazamiento=2
    Cifrado=""
    if texto==texto.upper():lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    else:lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    for caracteres in texto:
        if caracteres in lista:Cifrado += lista[(lista.index(caracteres)+Desplazamiento%(len(lista)))]
        else:Cifrado+=caracteres
    return Cifrado
#print("\nSu cadena de texto cifrada es:",Codificar("Estamos emocionados de seguir adelante en la fiucv."))
def Descodificar(texto):
    """Seccion de Ayuda para la Funcion Codificar en el modulo Modulo_Crypto:

    Descripcion de la Funcion Descodificar:

        Esta funcion, tiene como objetivo descodificar las cadenas de texto que hayan sido cifradas con la funcion Codificar.

    Funcionamiento de la funcion Descodificar:

        La funcion descodificar hace la operacion inversa de la funcion Descodificar, remplazando cada letra del mensaje encriptado
        por la letra original, segun su posicion definida en el alfabeto."""
    Desplazamiento=2
    Descifrado=""
    if texto==texto.upper():lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    else:lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    for caracteres in texto:
        if caracteres in lista: Descifrado += lista[(lista.index(caracteres)-Desplazamiento%(len(lista)))]
        else: Descifrado+=caracteres
    return Descifrado
#print("\nSu cadena de texto descifrada es:",Descodificar("Etubnpt fnpdjpñbept ef tfhvjs befmbñuf fñ mb gjvdw."))
