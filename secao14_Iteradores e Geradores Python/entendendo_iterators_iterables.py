""" 
Entendendo Iterators e Iterables

Iterator -> 
    - Um objeto que pode ser iterado;
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable ->
    - Um ojbeto que irá retornar um iterator quando a função iter() for chamada.



"""

nome = 'Dennis' # É um iterable, mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6] # É um iterable, mas não é um iterator.
 
# tornando iteraveis:
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1)) # vai imprimir a primeira letra da varaivel 

print(next(it2)) # vai imprimir o primeiro numero da lista 


nome1 = 'Dennis'
for letra in nome1:
    print(f'{letra}')

    