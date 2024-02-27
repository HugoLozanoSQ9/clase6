"""
CRUD

CREATE
READ - TAREA
UPDATE
DELETE

investigar el modulo os 

"""

import files

files.create_file('sample1.txt','contenido del archivo')
files.create_file('sample2.txt')

files.modify_file('sample1.txt', 'Este contenido fue sobreescrito',overwrite=True)
files.modify_file('sample2.txt', 'Este contenido fue adicionado')