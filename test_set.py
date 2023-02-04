s = set({1,2,3,5,6})
print(s)
print(type(s))
s1 = set({1,56.7,45.6,341,2189,1})
print(s1)
print(type(s1))

s = {1,2,1,3,6,3,4,}
print(s)
print(type(s))

s1 = {24.45, 34.3,1234.5,1232313,123414,24.45}
print(s1)
print(type(s1))

se = set('Dennis Augusto')
print(s)

set_string = set('Meu nome é Dennis Augusto')

#list = []
list_set = [1,2,3,3,4,5,6,4]
set(list_set)
print(list_set)

#tuple = ()
tuple_set = (1,23,4,576,5445,133,123,133)
set(tuple_set)
print(tuple_set)

valor_set = input('Informa um valor para verificar se tem no Conjunto:')
if valor_set in s1:
    print(f'O valor: {valor_set} está no Conjunto')
else:
    print(f'O valor: {valor_set} não esta no conjunto')

lista = [1,1,13,4,5,67,4,7,44422]
print(f'Lista: {lista} tem {len(lista)} elementos') #len usado para contar quantos elementos tem dentro de uma lista ou tupla

tupla = 1,2,11,1,4,564,63,74,7
print(f'tupla: {tupla} tem {len(tupla)} elementos')

dicionario = {}.fromkeys(tupla,'dict')
print(f'dicionario: {dicionario} tem {len(dicionario)} elementos')

conjunto = {1,1,2,2,4,4,5,63,7}
print(f'conjunto: {conjunto} tem {len(conjunto)} elementos')


set3 = {'Dennis', False,7868,686.6}
print(set3)
print(type(set3))

for valor in set3:
    print(valor)


cidades = ['Sao Paulo','Cuiaba','Recife','Sao Paulo','Florianopolis','Capina Grande']
print(cidades)
print(type(cidades))

print(len(set(cidades)))

lista_nomes = ['Dennis','Dennis','Ana','Maria','Jose']
print(lista_nomes)
print(f'Tinha 2 nomes na lista, então excluir um e agora está assim a lista: {len(set(lista_nomes))} ')

lista_nomes.add('Marcelo')
lista_nomes.add('Catarina')
lista_nomes.add('Pedro')

lista_nomes.remove('Dennis')
lista_nomes.remove('Ana')
lista_nomes.discard('Catarina')

#Deep Copy
nova_lista_nomes = lista_nomes.copy()
print(nova_lista_nomes)
nova_lista_nomes.add('Joselino')
print(nova_lista_nomes)

#Shallow Copy
nova_lista_nomes = lista_nomes
nova_lista_nomes.add('Marta')
print(nova_lista_nomes)

lista_nomes.clear()
