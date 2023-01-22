"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula
"""

ativo = True
print(ativo)

"""
Operações Básicas:
"""
# Negação (not):
"""
OBS: Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
     Fazendo a negação, se o valor booleano for falso o resultado será verdadeiro.
"""
print(not ativo)

logado = False
# Ou (or):
"""
É uma operação binária, depende de dois valores. Ou um ou o outro deve ser verdadeiro.
Exemplo:
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores 
devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

5 > 6
5 < 6
5 == 6
6 == 6
4 <= 5
num1 = 6
num2 = 8
num1 >= num2
num1 >= num2 or num1 > 3
num1 == num2 and num2 < 5

