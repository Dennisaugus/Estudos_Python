"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos Conjuntos da Matemática

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesmo forma que na Matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Cojuntos são bons para se utiliza quando precisarmos armazenar elementos
mas não nos importamos com a cordenação deles. Quando não precisamos se preocupar 
com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em python com as chaves {}

Diferença entre conjuntos (Set) e mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.
"""

#Definindo um conjunto
#Forma 1

s = set({1,2,3,3,3,4,5,6,7,7,77,56}) # Repara que temos valores duplicados
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor existente, o mesmo 
# será ignorado sem gerar erro ou não farar parte do conjunto.

#Forma 2 -> Mais comum

s = {1,2,3,3,3,4,5,6,87,6,5,4}
print(s)
print(type(s))

#Faça na console python

s = set('Dennis Augusto')
print(s)

#podemos gerar um set de uma Lista ou tupla
lista = [1,2,2,3,4,5,6,7,7,8]
set(lista)

tupla = (1,2,2,3,4,5,6,4,2,3)
set(tupla)

#Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem.

# Lista aceitam valores duplicados, então aceitam 8 elementos
lista = [99,23,3123,556,11,1,1,99] #armazena a ordem que foi impressa
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então aceitam 8 elementos
tupla = 99,23,3123,556,11,1,1,99 #armazena a ordem que foi impressa
print(f'tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicadas, então aceitem 6 elementos
dicionario = {}.fromkeys(lista, 'dict') # armazena a ordem que foi impressa
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Sets não aceitam valores duplicados, então aceitam 6 elementos
conjunto = {99,23,3123,556,11,1,1,99} # não armazena a ordem que foi impressa
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


#Assim como todo outro conjunto Python, podemos colocar todos os tipos de dados misturados em Sets

s = {'b',1,True,12.23}
print(s)
print(type(s))

# Podemos interar em um set normalmente
for valor in s:
    print(valor)


#Usos interessantes com sets

# Imagine que fizermos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos 
# e ter repetição.

cidades = ['João Pessoa', 'Rio de Janeiro', 'São Paulo', 'Campo Grande','Belo Horizonte', 'Cuiaba','São Paulo','Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisarmos saber quantas cidades distintas, ou seja, unicas que temos na lista:

# O que você faria? faria um loop na lista...?
# PODEMOS utilizar o set para isso.

print(len(set(cidades)))


#Adicionando elementos no conjunto
s = {1,2,3}
s.add(4)
s.add(4) # Não gera duplicidade e nem gera erro, simplesmente é ignorado e não é adicionado no Set
print(s)

# Remover elementos em um conjunto

# Forma 1
s = {1,2,3}
s.remove(1) # Não é indice, informamos o valor a ser removido
print(s)

# Caso o valor não seja encontrado, será gerado um valor KeyError. Nenhum valor é retornado

# Forma 2
s.discard(2) 
print(s)
# OBS: se o valor não for encontrado, não gera erro

#Copiando um set para outro set
s = {1,2,3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2 -Shallow Copy
novo = s
novo.add(5)
print(novo)
print(s)

# Podemos remover todos elementos de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso de Puthon e um
# conjunto de estudantes de Java.

estudantes_python = {'Dennis','Caio','Sara','Michael','Mari','Marcelo'}
estudantes_java = {'Daniel','Ederley','Camila','Caio','Dennis'}

# Veja que alguns alunos que estudam Python estudam Java.
# Precisarmos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando uniom

unicos1 = estudantes_python.union(estudantes_java)
#unicos1 = estudantes_java.union(estudantes_python) -> vai gerar o mesmo resultado da expressão acima (oque vai mudar é a ordem)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe | 
unicos2 = estudantes_python | estudantes_java
print(unicos2)


# Gerar um conjunto de estudantes que estão am ambos os cursos
# Forma 1  - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos = estudantes_python & estudantes_java
print(ambos)

# Gerar um conjunto de estudantes que estão num curso e que não estou em outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

s = {1,2,34,45,6,7,78}
print(sum(s))
print(max(s))
print(min(s))
print(len(s)) #quantidade de elementos