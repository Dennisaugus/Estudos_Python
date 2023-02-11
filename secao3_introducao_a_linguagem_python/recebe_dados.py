"""
Recebendo dados do usuário:

input -> entrada de dados

input() -> todo dado recebido via input é do tipo String 

Em python, string é tudo que estiver entre:
- Aspas simples 
- Aspas duplas
- Aspas simples triplas 
- Aspas duplas triplas
Exemplo:
- Aspas simples -> 'Dennis Augusto'
- Aspas duplas -> "Dennis Augusto"
- Aspas simples triplas -> '''Dennis Augusto'''
- Aspas duplas triplas 
"""

#Print antigo do Python
#Entrada de dados
print("Qual o seu nome?")
nome = input()

#forma mais mordena na entrada de dados
nome = input('Qual o seu nome?')
idade = int(input('Qual é a sua idade?'))


print('Seja bem vindo(a) %s' % nome)

print('Qual sua idade:')
idade = input()

#Processamento

#Saida de dados
print('A %s tem %s anos' % (nome, idade))

#Exemplo de print moderno (versão 3~>)
#Forma moderna:
print('Seja bem vundo(a) {0}'.format(nome))
print('A {0} tem {1} anos'.format(nome, idade))

#Exemplo mais moderno do print:
print(f'Seja bem vindo(a) {nome}')
print(f'A {nome} tem {idade} anos')

#Cast é a conversão de um tipo de dado para outro 
print(f'A {nome} nasceu em {2023 - int(idade)} anos')
#sem fazer o cast
print(f'A {nome} nasceu em {2023 - idade} anos ')