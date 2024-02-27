file = open("texto.txt",'r') # modo r
content = file.read()
# content = file.read(5) (el 5 representa la cantidad de caracteres que se desean leer en este caso serían los primeros 5)
print(content)

