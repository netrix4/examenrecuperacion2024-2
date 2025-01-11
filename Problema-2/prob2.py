import re

def SeparaParesDeDigitos(bitsEntrada2):
    respuesta = re.findall('[0-9][0-9]', bitsEntrada2)
    return respuesta

def SeparaArchivoEnPalabras():
    archivo = open('diccionario.txt').read()

    # respuesta = re.findall('([áéíóúÁÉÍÓÚ]?\w[áéíóú]?)+',archivo)
    respuesta = re.findall('\w+',archivo)
    # print(f'Longitud del archivo de entrada: {respuesta.__len__()}')
    return respuesta

def CodificarCadena(todosDigitos):
    respuesta=''

    for digito in todosDigitos:
        print(f'Digito: {int(digito)} Palabra: {totalPalabrasDeArchivo[int(digito)]}')
        respuesta += totalPalabrasDeArchivo[int(digito)] + ' '

    return respuesta

if (__name__ == "__main__"):
    elInputEsCorrecto = False
    # totalPalabrasDeArchivo =''


    while(elInputEsCorrecto == False):
        bitsEntrada = input('Dame el numero entero (pares de digitos): ')

        if(bitsEntrada.__len__()%2 == 0):
            elInputEsCorrecto = True

            totalPalabrasDeArchivo = SeparaArchivoEnPalabras()
            paresDigitos = SeparaParesDeDigitos(bitsEntrada)

            cadenaCodificada = CodificarCadena(paresDigitos)

            print(f'La frase resultante de la codificacion es la siguiente: \n{cadenaCodificada}')

        else:
            print("El numero de digitos de tu entrada  NO es par, reingresa un numero par\n")
