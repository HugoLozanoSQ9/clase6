def create_file(file_name, content=None):
    file = open(file_name, "a")
    file.write(content)
    file.close()


name = str(input("Hola podrías darme el titulo de tu archivo con todo y la extención "))
content = str(input("Podrías indicarme el contenido por favor? "))

create_file(name, content)
