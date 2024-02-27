file = open ('texto.txt','w')#w método write va a sobreescribir el contenido

file.write('Este es el primer contenido \n')
file.close()

file = open ('texto.txt','a')
file.write('Este es el ultimo contenido\n')
file.close()


file = open ('texto.txt','r')
print(file.read())
file.close()


#file_name sería obviamente el nombre de tu archivo a realizar la operación
with open('texto.txt', 'w') as file: #Con la función 'con' se tiene lo siguiente:
#con función open() a la variable file (as es el asignador)
#Con el resultado de la función open como variable file
    file.write('Este es el primer contenido\n')
#No es necesario que haga close por que cuando termine de hacer la acción 
#Automáticamente se cierra