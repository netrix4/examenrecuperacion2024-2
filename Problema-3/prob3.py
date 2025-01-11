import re 

contador = 0
archivo = open('texto.txt').read()
renglones = archivo.splitlines()

renglones.remove('')

print(f'Estos son los renglones de todo el archivo ({renglones.__len__()}):\n{renglones}')


for renglon in renglones:
    print(f'== Renglon {contador+1} ==')
    palabrasDeRenglon = re.split(r'\W+', renglon)
    # palabrasDeRenglon = renglon.split(' ')

    palabrasDeRenglon.remove('')
    palabrasDeRenglon.sort()
    print(f'Palabras del renglon actual ordenadas: ({palabrasDeRenglon.__len__()}):\n {palabrasDeRenglon}')

    contador+=1
