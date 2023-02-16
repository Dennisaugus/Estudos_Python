""" 
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar elementos.

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados
"""

lista = [ 4,6,1,2,5]
lista.sort()
print(lista)

# Usando o sorted()
# Lista
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros)) # Retorna em lista
print(numeros)
# OBS: o sorted() retorna uma nova lista com os elementos (a lista original se manteve intacta)

# Tupla
numeros = (6,1,8,2)
print(numeros)
print(sorted(numeros)) # Sempre vai retornar uma lista
print(numeros)

# Set 
numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros))
print(numeros)


# Adicionando parâmetros ao sorted()

numeros = [6, 1, 8, 2]
print(sorted(numeros))
print(tuple(sorted(numeros))) # convertendo em uma tupla
print(set(sorted(numeros))) # convertendo em um set
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor 

# Podemos utilizar o sorted() para coisas mais complexas
#dicionario
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": [], "cor": "amarelo"},
    {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "Gal", "tweets": [],  "cor": "preto", "musica": "rock"}
    
]

# Ordenando por tamanho do dicionário:
print(usuarios)
# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


# Ultimo exemplo 

musicas = [
    {"titulo": "abcc", "tocou": 3},
    {"titulo": "adiapfhg", "tocou": 2},
    {"titulo": "fnbcge", "tocou": 4},
    {"titulo": "asdopjefehqf", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))


