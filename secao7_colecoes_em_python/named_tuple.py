""" 
Módulo Collections - Named Tuple

# Recap Tupla
tupla = (1,2,3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas onde, especificamos um nome para a mesma e também parâmetros
"""
# Importantdo

from collections import namedtuple
# Precisarmos definir o nome e parametros
# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple 
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando 

ray = cachorro(idade=2, raca='chow-chow', nome='Ray')

print(ray)

# Acessando os dados 
# Forma 1
print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome

# Forma 2
print(ray.idade) # idade
print(ray.raca)  # raca
print(ray.nome)  # nome

print(ray.index('chow-chow')) # informe o indice do valor chow-chow
print(ray.count('chow-chow')) # conta quantos valores tem o nome chow-chow na tupla