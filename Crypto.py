Abecedario = 'abcdefghijklmnopqrstuvwxyz_'
def cifrar(cadena, clave): #Funcion para cifrar la cadena de texto plana
    texto_cifrado = ''
    for letra in cadena:
        suma = Abecedario.find(letra) + clave
        modulo = int(suma) % len(Abecedario)
        texto_cifrado = texto_cifrado + str(abc[modulo])
    return texto_cifrado
def decifrar(cadena, clave): #Funcion para decifrar la cadena de texto plana
    texto_cifrado = ''
    for letra in cadena:
        suma = Abecedario.find(letra) - clave
        modulo = int(suma) % len(Abecedario)
        texto_cifrado_cifrado = texto_cifrado + str(Abecedario[modulo])
    return texto_cifrado
def main(): #Funcion principal , donde se ejecuta las dos anteriores funciones.
    cadena_cifrar = str(input("Ingrese la cadena de texto plano que desea cifrar: ")).lower()
    clave_numerica = int(input("Cree una clave numerica: "))
    print(cifrar(cadena_cifrar,clave_numerica))
    cadena_descrifrar = str(input("Ingrese la cadena de texto plano que desea a decifrar: ")).lower()
    clave_numerica_descifrar = int(input("Ingrese la clave numerica correspondiente: "))
    print(decifrar(cadena_descrifrar,clave_numerica_descifrar))
if __name__ == '__main__':

    main()
