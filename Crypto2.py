def Codificar(texto):
    Desplazamiento=2
    Cifrado=""
    if texto==texto.upper():lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    else:lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    for caracteres in texto:
        if caracteres in lista:Cifrado += lista[(lista.index(caracteres)+Desplazamiento%(len(lista)))]
        else:Cifrado+=caracteres
    print(Cifrado)
    return Cifrado
def Descodificar(texto):
    Desplazamiento=2
    Descifrado=""
    if texto==texto.upper():lista="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    else:lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    for caracteres in texto:
        if caracteres in lista: Descifrado += lista[(lista.index(caracteres)-Desplazamiento%(len(lista)))]
        else: Descifrado+=caracteres
    print(Descifrado)
    return Descifrado
