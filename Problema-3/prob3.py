import re 

contador =0
archivo = open('texto.txt').read()
# separadassss = archivo.split('\n\n')
renglones = archivo.splitlines()
for renglon in renglones:
    limpiadoEnPalabras = re.split(r'\W+', renglon)
    limpiadoEnPalabras.sort()

    print(f"Hello, {contador}!")


limpiadoEnPalabras = re.split(r'\W+', archivo)
print(limpiadoEnPalabras)

copiado = list(limpiadoEnPalabras)

limpiadoEnPalabras.sort()

print(limpiadoEnPalabras)

final =''
for palabra  in limpiadoEnPalabras:
    final+= palabra+' '

print(final)