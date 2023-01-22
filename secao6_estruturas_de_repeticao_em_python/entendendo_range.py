""" 
Ranges:

- Precisamos conhecer o loop for para usar o ranges.
- Precisamos conhecer o range para trabalhar melhor com o loops for.


Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira especificada.

Formas praticas:
# Forma 1 
range(valor_da_parada)
OBS: valor_da_parada não inclusive (inicio padrão 0, e passo de 1 em 1)


# Forma 2

range(valor_de_inicio, valor_da_parada)
OBS: valor_da_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1)

#Forma 3

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_da_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)


#Forma 4 Inversa
range(valor_inicio, valor_de_parada, passo)
OBS? valor_de_para não inclisuve (valor_inicio especificado pelo usuário, e passo especificado pelo usuário)


Convertendo range em lista no terminal python:
lista = range(10)
lista = list(range(10))
lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# Exemplo Forma 1 
for num in range(11):
    print(num)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Exemplo Forma 3
for num in range(1, 11, 2):
    print(num)
    
# Exemplo Forma 4 Inversa
for num in range(10, 0, -1):
    print(num)
# vai de 10 até 0:
for num in range(10, -1, -1):
    print(num)