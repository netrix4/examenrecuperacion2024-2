import re 
archivo = open('texto.txt').read()
# separadassss = archivo.split('\n\n')
print(archivo)
limpiadoEnPalabras = re.split(r'\W+', archivo)
print(limpiadoEnPalabras)

copiado = list(limpiadoEnPalabras)

limpiadoEnPalabras.sort()

print(limpiadoEnPalabras, 'ordenado??')

final =''
for palabra  in limpiadoEnPalabras:
    final+= palabra+' '

print(final)