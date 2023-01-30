"""
Módulo Collections: Ordered Dict

https://www.geeksforgeeks.org/ordereddict-in-python/

# Em um dicionario, a ordem de inserção dos elementos não é garantida
dicionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5} 

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
# Ordered Dict -> é um dicionário que nos garante a ordem de inserção dos elementos
    
from collections import OrderedDict

dicionario = OrderedDict({'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 })

for chave,valor in dicionario.items():
    print(f'chave={chave} : valor={valor}')

# Entendo a diferença entre Dick e Ordered Dict

# Dicionários comuns 

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'b' : 2, 'a' : 1}
print(dict1 == dict2) # True -> já que a ordem dos elementos não importa para o dicionário 

# Ordered dict
odict1 = OrderedDict({'a' : 1, 'b' : 2})
odict2 = OrderedDict({'b' : 2, 'a' : 1})

print(odict1 == odict2) # False -> já que a ordem dos elementos importa para o OrderedDict