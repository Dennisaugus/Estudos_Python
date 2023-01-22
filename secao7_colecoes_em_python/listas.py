"""
Listas:

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença 
de serem  dinâmicas e também de podermos colocar QUALQUER tipo de dado.

Liguagens C ou Java:
    - Possuem tamanho e tipo de dado fixo;
      Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
      será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
    - Dinâmico: Não possuem tamanho fixo. Ou seja, podemos criar a lista e simplesmente ir adicionando elementos nela.
    - Qualquer tipo de dado: Não possuem tipo de dado fixo. Ou seja, podemos alocar qualquer tipo de dado na lista.

As listas em Python são representadas por colchetes: []

exemplos no terminal python:

type("a")
<class 'str'>
type(True)
<class 'bool'>
type([])
<class 'list'>
type([1, 4, 'Dennis', True])
<class 'list'>


dir(lista5) -> vai exibir todos os metodos/propriedades deste valor. 

"""

type([])

lista1 = [1, 88, 45,45.5, 3, 34, 21, 2,1]

lista2 = ['G','E','n','v','H']

lista3 = []

lista4 = list(range(11)) #armazena na lista um range de 0 a 10

lista5 = list('Dennis Augusto') # lista5 ['D', 'e', 'n', 'n', 'i', 's', ' ', 'A', 'u', 'g', 'u', 's', 't', 'o']

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

letra = input('Informe uma letra para validar se está no sistema:')
if letra in lista2:
    print(f'A letra {letra} consta no sistema')
else:
    print(f'A letra {letra} não consta no sistema')

#Podemos facilmente ordenar uma lista
print(lista1.sort())
print(lista1)
print(lista5.sort())
print(lista5)

#Podemos facilmente contar o numero de ocorrencias de um valor em uma lista 
print(lista1.count(1))
print(lista5.count('n'))

#Adicionar elementos em listas

"""
OBS: para adicionar elementos em listas, utilizamos a função append

Com o append, nós só conseguirmos adicionar 1 elemento por vez 
lista1.append(12, 3,4) #Erro
"""
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 45.5]) #Coloca a lista como elemento único (sublista)
print(lista1)
if [8, 3, 45.5] in lista1: #verifica o elemento '[8, 3, 45.5]' apenas
    print('Entontrei a Lista.')
else:
    print('Não encontrei a lista')

lista1.extend([234, 33 ,5867]) #Coloca elemento da lista como valor adicional a lista (Não aceita valor única, apenas iteraveis)
print(lista1)

#Podemos inserir um novo elemento na lista informando a posição do índice
#Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

#Podemos facilmente juntar 2 listas
lista6 = lista1 + lista2
print(lista6)
lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista
#Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#Forma 2
print(lista1[::-1])
print(lista2[::-1])


#Copiar uma lista

lista6 = lista2.copy()
print(lista6)

#Podemos verificar quantos elementos tem dentro de uma lista
print(len(lista1))
print(len(print2))
print(len(lista4))


#Podemos remover facilmente o ultimo elemento de uma lista 
#OBS: O pop não somente removo o ultimo elemento como também o retorna
print(lista5)
lista5.pop()
print(lista5)

#Podemos remover um elemento pelo indice
#OBS: os elementos á direita deste indice serão deslicados para a esquerda.
lista5.pop(2)
print(lista5)

