""" 
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamados de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1,2.2,'3',True,5]

"""

# Exemplos 

listas = [[1,2,3], [4,5,6], [7,8,9]] # Matriz 3 x 3 se fosse comparar 

print(listas)
print(type(listas))

print(listas[0]) # resultado [1,2,3]
print(listas[0][1]) # resultado 2
print(listas[2][-3]) # resultado 7 

# Iterando com Loops em uma lista aninhada
for lista in listas:
   for numero in lista:
       print(numero)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]


# Outros Exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

#Gerando valores iniciais 

print([['*' for i in range(1,4)] for j in range(1,4)])