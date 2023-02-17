""" 
Reversed

OBS: Não confunda com a função reverse() que estudamos em listas.
# Relembrando o reverse()
lista = [1,2,3,4,5]
print(lista)
print(lista.reverse())
print(lista)

# A FUNÇÃO reverse() só funciona em listas.

Já a função reversed() funciona com qualquer interável

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

# Exemplos

lista = [1,2,3,4,5]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto.

# Lista
print(list(reversed(lista)))
# Tupla 
print(tuple(reversed(lista)))
# Conjunto (Set)
print(set(reversed(lista))) # não vem de forma inverser (o Set não defini a ordem dos elementos)

# Podemos iterar sobre o reversed
for letra in reversed('Dennis Augusto'):
    print(letra, end='')
print('\n')
# Podemos fazer o mesmo sem o uso do for:
print(''.join(list(reversed('Dennis Augusto'))))

# Já vimos como fazer isso mais facil com o slice de strings
print('Dennis Augusto'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0,10)):
    print(n)
    
# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
    
