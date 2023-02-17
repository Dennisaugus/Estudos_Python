""" 
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos
"""

# Exemplos de max

lista = [1, 7 ,8 ,3, 19,124]
print(max(lista)) 

set = {1,23,564,653}
print(max(set))

tupla = (1,24,667,3314)
print(max(tupla))

dicionario = {"a": 1,"b": 7,"c": 8,"d": 3,"e": 19,"f": 124}
print(max(dicionario.values()))

print(max(3, 21)) # entre 2 valores 

# Faça um programa que receba dois valores do usuário e mostre o maior 

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informa o segundo valor: '))
print(max(val1, val2))

print(max(1,3,4,2,6))
print(max('a','b','cde')) #cde
print(max('a','b','g')) #g

print(max(3.145, 5.678))
print(max('Dennis Augusto'))


# Exemplos de min

lista = [1, 7 ,8 ,3, 19,124]
print(min(lista)) 

set = {1,23,564,653}
print(min(set))

tupla = (1,24,667,3314)
print(min(tupla))

dicionario = {"a": 1,"b": 7,"c": 8,"d": 3,"e": 19,"f": 124}
print(min(dicionario.values()))

print(min(3, 21)) # entre 2 valores 

# Faça um programa que receba dois valores do usuário e mostre o maior 

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informa o segundo valor: '))
print(min(val1, val2))

print(min(1,3,4,2,6))
print(min('a','b','cde')) #é o espaço (conta como uma string)
print(min('a','b','g')) # é o espaço (conta como uma string)

print(min(3.145, 5.678))
print(min('Dennis Augusto')) # é o espaço (conta como uma string)


# Outros exemplos

nomes = ['Arya', 'Maria','Dennis', 'Dora','Fernando']
print(max(nomes)) # Coleta o resultado por Ordem Alfabetica
print(min(nomes)) # Coleta o resultado por Ordem Alfebetica

# Usando o lambda
print(max(nomes, key=lambda nome: len(nomes)))
print(min(nomes, key=lambda nome: len(nomes)))


musicas = [
    {"Titulo": "Rap", "Tocou": 3},
    {"Titulo": "Rock", "Tocou": 4},
    {"Titulo": "Pegode", "Tocou": 2},
    {"Titulo": "Sertanejo", "Tocou": 1},
    {"Titulo": "Reague", "Tocou": 2}
]

print(max(musicas, key=lambda musica: musica['Tocou']))
print(min(musicas, key=lambda musica: musica['Tocou']))


# DESAFIO! Imprima somento o titulo da muscia 

print(max(musicas, key=lambda musica: musica['Tocou'])['Titulo'])
print(min(musicas, key=lambda musica: musica['Tocou'])['Titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?

max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']
        
for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['Titulo'])
        
min = 9999
for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['Titulo'])

