"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas deiferenças básicas:

1 - As tuplas são representadas por parametros ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla
gera uma nova tupla.
"""

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1,2,3,4,5,6) #processo de criação da tupla
print(tupla1)
print(type(tupla1))

tupla2 = 1,2,3,4,5,6,7, #processo de criação da tupla
print(tupla2)
print(type(tupla2))


# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla 
print(tupla4)
print(type(tupla4))

tupla5 = 3,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela virgula e não pelo uso do parênteses 

# (4) -> Não é tupla 
# (3,)-> é uma tupla
# 4, -> é uma tupla

#Podemos gerar uma tupla dinamicamento com o range(inicio,fim,passo)
tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))

#Desempacotamento de tupla

tupla7 = ('Dennis Augusto', 'Programação em Python')

nome, curso = tupla7
print(nome)
print(type(nome))
print(curso)
print(type(curso))
print(type(tupla7))

#OBS: gera ValueError se colocarmos um número diferente de elementos para desempacotar

#Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis.
# Soma*, Valor Máximo*, Valor Minimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla8 = (1,2,3,4,5,6)

print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

#Concatenação de tuplas

tupla9 = (1,2,3)
print(tupla9)
tupla10 = (4,5,6)
print(tupla10)
soma = tupla10 + tupla9
print(soma)
print(tupla10)
print(tupla9)
#Lembrando que tuplas são imutaveis 
#caso queira alterar o conteudo
tupla9 += tupla10
print(tupla9)


# Verificar se determinado elemento está contido na tupla:

tupla11 = (1,2,3)
print(3 in tupla11)

#Iterando sobre uma tupla 

tupla12 = (1,2,3)
for n in tupla12:
    print(n)

for indice, valor in enumerate(tupla12):
    print(indice,valor)

# Contando elementos dentro de uma tupla:

tupla13 = ('a','b','c','d','a','b')
print(tupla13.count('a'))
print(tupla13.count('c'))

tupla14 = ('Dennis', 'Augusto','Jose','dos','Santos','Gusmao')
print(tupla14.count('u'))

# Dicas na utilização de tuplas 
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

# O acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual indice um elemento está na tupla 
print(meses.index('Junho')) #caso tenha 2 'Junho' na tupla, o mesmo ira retornar o primeiro conforme a lista faz também
print(meses.index('Dezembro'))

# OBS: Caso o elemento não exista, será gerado ValueError

#Slicing

# tupla[incio:fim:passo]
print(meses[::])
print(meses[5:9])
print(meses[::-1])

# Por que utilizar tuplas:
# - Tuplas são mais rapidas doque as listas
# - Tuplas deixam seu código mais seguro
# - Isso porque trabalhar com elementos imutaveis traz segurança para o código.

# Copiando uma tupla para outra tupla 

tuplacopy = (1,2,3)
print(tuplacopy)
nova = tuplacopy
print(nova)
print(tuplacopy)

outra = (4,5,6)
nova += outra
print(nova)
print(tuplacopy)

dir(tupla) #verifica os metodos das tuplas que são poucas.