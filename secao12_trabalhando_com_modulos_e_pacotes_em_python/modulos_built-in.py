""" 
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)

------------------------
|Python|Módulos builtin|
------------------------
import random # não é legal pois o fazer o módulo completo, traz muito recurso pra memoria

https://docs.python.org/3/py-modindex.html
"""
# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
print(random())

# Importando todo o módulo
import random
print(random.random())

# Utilizando alias (apelidos) para funções 
from random import randint as rdi, random as rdm

print(rdi(5,89))
print(rdm())

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random, 
    randint, 
    shuffle, 
    choice
    )

print(random()) 
print(randint(4,34))
lista = ['Dennis','Augusto','Gusmao']
shuffle(lista)
print(lista)
print(choice('Dennis'))










