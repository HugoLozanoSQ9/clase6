def modify_file(file_name, content, overwrite=False):
    file = open(file_name, "a")
    file.write(content)
    file.close()
    if overwrite in ['y','yes','s','si']:
        file = open(file_name,'w')
        content1 = str(input("Podrías indicarme el contenido por favor? "))
        file.write(content1)
        file.close()

name = str(input("Hola podrías darme el titulo de tu archivo con todo y la extención "))
content = str(input("Podrías indicarme el contenido por favor? "))
overwrite=str(input("deseas sobreescribir contenido? y/n "))

modify_file(name,content,overwrite.lower())
