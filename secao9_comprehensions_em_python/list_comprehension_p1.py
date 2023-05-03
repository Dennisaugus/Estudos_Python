""" 
List Comprehension 

- Utilizando List comprehension nós podemos gerar novas listas com dados processados a partir de outro 
iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]
"""

# Exemplos

numeros = [1,2,3,4,5]

res = [numero * 10 for numero in numeros]

print(res)

""" 
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""

res = [numeros * 2 for numero in numeros ]

print(res)

def funcao(valor):
    return valor * valor 

res = [funcao(numero) for numero in numeros]

print(res)


# List Comprehension versos Loop

# Loop
numeros = [1,2,3,4,5]
numeros_dobrados = []

for numero in numeros: # for numero in [1,2,3,4,5]:
    numeros_dobrados.append(numero * 2)
    
print(numeros_dobrados)

#List Comprehension
print([numero * 2 for numero in numeros]) 
#print([numero * 2 form numero in [1,2,3,4,5]]) 


# Outros Exemplos 
# exemplo 1

nome = 'Dennis Augusto'

print([letra.upper() for letra in nome])

# exemplo 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())

amigos = ['maria', 'julia', 'pedro','guilherme','vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# exemplo 3

print([numero * 3 for numero in range(1, 10)])


# exemplo 4

print([bool(valor) for valor in [0, [], '', True,1, 3.15]])

# exemplo 5

print([str(numero) for numero in [1,2,3,4,5]])

