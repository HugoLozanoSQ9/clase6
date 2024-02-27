file = open("texto.txt")

for line in file:
    print(line)

#Si quisieramos omitir el salto de linea entonces sería así :
    
file.close()


"""
for line in file:
    for char in line:
        if not char.isprintable():
            line=line.replace(char,'')    
    print(line)
"""