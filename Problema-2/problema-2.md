## **D.Codificador**

### **Objetivo:**
Desarrollar un programa que decodifique un texto numérico basado en un diccionario de palabras almacenado en un archivo de texto.

### **Instrucciones:**

1. **Entrada:**
    * <u>Número_ de entrada</u>: El programa recibirá un número entero como entrada, compuesto por pares de dígitos.
    * <u>Archivo de diccionario</u>: El programa cargará un archivo de texto que contiene un diccionario. Cada parrafo del archivo tendrá el formato: 
    
        * **número de dos dígitos** <u> parrafo </u> 
        * **número de dos dígitos** <u> palabra <u/>

2. **Procesamiento:**

    <u>Dividir el número de entrada</u>: El número de entrada se dividirá en pares de dígitos.

    <u>Buscar en el diccionario</u>: Cada par de dígitos se utilizará como clave para buscar la palabra correspondiente en el archivo de diccionario.
    
    <u>Construir la frase</u>: Las palabras encontradas se concatenarán para formar la frase decodificada.

3. **Salida:**
   * El programa imprimirá la frase decodificada.

### **Ejemplo:**

#### Archivo de diccionario (diccionario.txt):

Número de entrada: 0106010702040622


#### Salida:

la vida es angustia


### **Consideraciones Adicionales:**

* **Manejo de excepciones:** El programa debe validar que el usuario ingrese un número entero positivo.
* **Eficiencia:** Se valorará la eficiencia del algoritmo utilizado.
* **Modularidad:** Se recomienda dividir el programa en funciones más pequeñas para mejorar la legibilidad y mantenibilidad.
* **Documentación:** El código debe estar bien documentado con comentarios explicativos.

### **Entrega:**
* **Repositorio de Git:** Hacer un Fork de este repositorio y dejarlo publico para su entrega.
* **Commits:** Se revisara la frecuencia y calidad de los commits "no se permitira un commit con todo el codigo, debera existir evidencia del desarrollo.
* **Archivos a entregar:**
  * `main.py || main.js` (o el archivo principal en el lenguaje elegido)
  * `README.md`: Un archivo que explique cómo ejecutar el programa y cualquier decisión de diseño tomada, asi como los datos del alumno (Matricula, Nombre Completo, Materia y Fecha).


**Lenguajes de Programación:**

Este ejercicio puede ser implementado en los siguientes lenguajes de programación, como Python, JavaScript, Typescript.
