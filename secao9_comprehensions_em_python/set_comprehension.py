""" 
Set  Comprehension

Lista = [1,2,3,4]
Set = {1,2,3,4}
"""

numeros = {num for num in range(1,7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# OBS: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set 
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Pra finalizar trabalhando com strings

letras = {letra for letra in 'Dennis Augusto'}
print(letras)