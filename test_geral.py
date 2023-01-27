#for num in range(45, -1, -2):
#    print(num)



#qtd = int(input('Quantas vezes esse loop sera rodado?'))
#soma = 0
#for n in range(1, qtd+1):
#    num = int(input(f'Informe o {n}/{qtd} valor: '))
#    soma = soma + num
#print(f'A soma é {soma}')
"""
#valor = range(2, 15)
nome = 'Dennis Augusto'
for _, letra in enumerate(nome):
    print(letra)

for letra in enumerate(nome):
    print(letra)

for letra in enumerate(nome):
    print(letra[0])

for letra in enumerate(nome):
    print(letra[1])

#for list in range(2, 15):
#   print(list)

#for list in range(5,10):
#    print(list)
"""
"""
print('Sistemas de carne')
nomecarne1 = input('Informe a 1º carne:')
nomecarne2 = input('Informe a 2º carne:')
pesocarne1 = int(input('informe quantos kg pesa a primeira carne:'))
pesocarne2 = int(input('informe quantos kg pesa a segunda carne:'))
valorcarne1 = float(input('informa o valor da primeira carne:'))
valorcarne2 = float(input('informe o valor da segunda carne:'))
somadascarnes = valorcarne1 + valorcarne2
somapesocarnes = pesocarne1 + pesocarne2
print(f'A carne {nomecarne1} tem o peso de {pesocarne1}kg e está no valor de {valorcarne1}R$')
print(f'A carne {nomecarne2} tem o peso de {pesocarne2}kg e está no valor de {valorcarne2}R$')
print(f'O tatol de peso das duas carnes é de: {somapesocarnes}kg')
print(f'O valor total das duas carnes é de: {somadascarnes}R$')

print('Sistemas de nota')
nomealuno = input('Informe o nome do Aluno: ')
nota1 = float(input('Informe a 1º Nota do Aluno: '))
nota2 = float(input('Informe a 2º nota do Aluno: '))
media = (nota2 + nota1) / 2
if media > 7:
    print(f'O Aluno {nomealuno} foi Aprovado! com a Nota: {media}')
else:
    print(f'O Aluno {nomealuno} foi reprovado! com a Nota: {media}')

print('Sistema de Obesidade')
nomepessoa = input('Informa o seu nome: ')
peso = float(input('Informe o seu peso'))
if peso > 89.5:
    print(f'A Pessoa: {nomepessoa} está acima do pesso')
elif (peso < 89.5) and (peso > 79.7):
     print(f'A Pessoa: {nomepessoa} está no peso ideal')
else:
    print(f'A Pessoa: {nomepessoa} está abaixo do peso')


""" 
#Exercicio 1.
#Faça um sistema de correios onde que solicite a nome do produto e o código de rastreio.
#Faça uma validação se o produto saio do Brasil ou da China ou de outro Pais.
"""

print('--------------- Sistema de restreamento dos Correios --------------------')
nomeproduto = input('Informe o nome do produto:')
codigorastreio = input('Informe as 2 ultimas letras do código de rastreio:')
cpf = int(input('Informe o seu cpf:'))
valordoproduto = float(input('Informe o valor do produto:'))
print('-----------------Cadastro realizado com sucesso -------------------------')

if codigorastreio == 'BR':
    print(f'O produto {nomeproduto} com o valor {valordoproduto}R$ saiu do Brasil.')
elif codigorastreio == 'CH':
    print(f'O produto {nomeproduto} com o valor {valordoproduto}R$ saiu da China.')
else:
    print(f'O produto {nomeproduto} veio de outro Pais e não a informação de onde veio.')


"""

















