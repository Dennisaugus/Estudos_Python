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

Listas são mutaveis: Ou seja, podem mudar constantemente.

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

lista6 = [1,2,34, True, 'dennis', 'd', [1,2,3], 4.5664325434]
print(lista6)
print(type(lista6))

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
print(lista5.sort()) #Ordena string
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
print(len(lista2))
print(len(lista4))


#Podemos remover facilmente o ultimo elemento de uma lista 
#OBS: O pop não somente removo o ultimo elemento como também o retorna
print(lista5)
lista5.pop() #No terminal ele não somente remove o ultimo elemento, como o retorna
print(lista5)

#Podemos remover um elemento pelo indice
#OBS: os elementos á direita deste indice serão deslicados para a esquerda.
#OBS: se não houver elemento no indice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)

#Podemos remover todos os Elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)


#Podemos facilmente repedir elementos em uma lista
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)


#Podemos converter uma string em uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#OBS: por padrão o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#Convertendo uma lista em uma string 
lsita6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

curso = ' '.join(lista6) # Pega a lista6, coloca espaço entre cada elemento e transforma em uma string 
print(curso)

curso = '$'.join(lista6) # Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string 
print(curso)

#Iterando sobre lista

#Exemplo

soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

soma = ''
for elemento in lista2:
    print(elemento)
    soma += elemento
print(soma)

#Exemplo - utilizando o while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Utilizando variaveis em lista

numero = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexado inversa 
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
# print(cores[-5]) # vai gerar um erro porque temos apenas 4 elementos (0,1,2,3)


cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

#Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice,cor)


#Lista aceita valores repetidos
lista = []
lista.append(423)
lista.append(423)
lista.append(3)
lista.append(3)

print(lista)


# Outros metodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [5 ,5 ,6 ,7 ,8 ,9 ,10]
print(numeros.index(6)) #Em qual indice da lista esta o valor 6
print(numeros.index(9)) #Em qual indice da lista esta o valor 9
print(numeros.index(5)) #Retorna o indice do primeiro elemento encontrado
#OBS: caso não tenha este elemento na lista será apresentado um erro 

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1)) #buscando a partir do indice 1
print(numeros.index(5,2)) #buscando a partir do indice 2
#OBS: caso não tenha este elemento na lista será apresentado um erro 

#Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) #busca o indice do valor 9, entre os indices 3 a 6

#Revisando o slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# trabalhando com slice de lista com o parametro inicio:

lista = [1,2,3,4]
print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restantes
print(lista[::]) # pega todos os elementos 

# trabalhando com slice de lista com o parametro 'fim':
print(lista[:2]) # começa em 0, pega até o indice 2 - 1
print(lista[:4]) # começa em 0, pega até o indice 4 - 1
print(lista[1:3]) # coemça em 1, pega até o indice 3 - 1

# trabalhando com slice de lista com o parametro 'passo':
print(lista[1::2]) #começa em 1, vai até o final, de 2 em 2
print(lista[::2]) #começa em 0, vai até o final, de 2 em 2


# Invertendo valores em uma lista
nome = ['Augusto','Dennis']
nome[0], nome[1] = nome[1], nome[0]
print(nome)

#forma pythonica
nome = ['Augusto', 'Dennis']
nome.reverse()
print(nome)


# Soma*, Valor máximo*, Valor minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) #soma
print(max(lista)) # máximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista

# Transforma uma lista em uma tupla 
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]
num1,num2,num3 = lista
print(num1)
print(num2)
print(num3)

#OBS: se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados. teremos ValueError 

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

#Forma 1 - Deep Copy
lista = [1 ,2 ,3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)

#OBS: Veja que ao utilizamos lista.copy() copiamos os dados da lista para uma lista, mais elas 
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (copia profunda)

#Forma 2 - Shallow Copy

lista = [1 ,2 ,3]
print(lista)
nova = lista # cópia
print(nova)
nova.append(4)
print(nova)
print(lista)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas 
# após realizar modificações em uma das listas, essa mesma modificação se refletiu em ambas as listas.
# Isso em python é chamado do Shalow Copy.
