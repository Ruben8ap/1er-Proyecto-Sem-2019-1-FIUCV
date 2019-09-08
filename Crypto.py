Abecedario = 'abcdefghijklmnopqrstuvwxyz_'
def cifrar(cadena, clave): #Funcion para cifrar la cadena de texto plana
    texto_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[modulo])
    return texto_cifrado
def decifrar(cadena, clave): #Funcion para decifrar la cadena de texto plana
    texto_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) - clave
        modulo = int(suma) % len(abc)
        texto_cifrado_cifrado = texto_cifrado + str(abc[modulo])
    return texto_cifrado
def main(): #Funcion principal , donde se ejecuta las dos anteriores funciones.
    c = str(input('Cadena a Cifrar: ')).lower()
    n = int(input('Clave Numerica: '))
    print(cifrar(c,n))
    cc = str(input('Cadena a Decifrar: ')).lower()
    cn = int(input('Clave Numerica: '))
    print(decifrar(cc,cn))
if __name__ == '__main__':

    main()
