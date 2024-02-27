# Manipulación de archivos 

## Manipulación 

Para manipular archivos con python, principalmente se realiza por medio de la función open()

Esta función recibe 2 parámetros:
filename: "Nombre o ruta del archivo"
mode: "Modo (o método) de aprtura"

# Modos de apertura

"r" (read)
Abre un archivo en modo lectura, arroja error si el archivo no existe. Este es el valor default

"a" (append) 
Abre un archivo para adicionar contenido, crea el archivo si no existe

"w" (write)
Abre un archivo para sobreescribir el contenido, crea el archivo si no existe

"x" (create)
Crea el archivo especificado, devuelve un error si el archivo ya existe

## Leer archivos 

Para leer un archivo, solo es necesario abrirlo especificando el nombre (o ruta) del archivo, ya que el modo default es "r".

La función open() regresa un objeto de tipo lector de archivo. 
Con este objeto aacedemos al método .read()

en open se debe especificar la ruta del archivo, caso contrario si solo se pone el titulo entocnes el archivo se deberá encontrar en el mismo sitio que el script
### Es posible leer partes del archivo 

El método .read() acepta un argumento, que representa el número de caracteres que se desea leer

### Es posible leer linea por linea
El método .readline() permite leer linea por linea el archivo

LLamando varias veces este método podemos ir accediendo al contenido una linea a la vez

### Leer por lineas 
El archivo es iterable, por lo que también es posible utilizar una esttructura for para acceder al contenido línea por linea

## Cerrar el archivo
Dentro de las buenas prácticas es necesario incluir un momento en el que se cierre el archivo cuando ya no se necesite.

Para este efecto se utiliza el método .close()

##Escribir contenido
Al abrir un archivo con el modo 'a' es posible adicionar contenido al final de un archivo 
Para escribir en el archivo se utiliza el método .write()

## Escribir contenido 
Al abrir un archivo con el modo 'w' significa que sobreescribirá todo el contenido del archivo.

De igual manera para escribir en el archivo se utiliza el m+etodo .write()

## Crear un archivo 

Para crear un nuevo archivo de texto sin contenido, es poisble utilizar el modo 'x'

## Palabra reservada with