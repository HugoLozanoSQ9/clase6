def create_file(file_name, content=None):
    mode = 'w' if content else 'x'
    file = open(file_name,mode)
    if content:
        file.write(content)


def modify_file(file_name, content, overwrite=False):
    mode = 'w' if overwrite else 'a'

    file = open(file_name,mode)
    file.write(content)
    file.close()