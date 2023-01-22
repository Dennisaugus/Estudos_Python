"""
Saindo de loops com break

Funciona da mesmo forma que nos linguagens C ou Java

Utilizamos o break para sair dos loops de maneira projetada.

"""

#Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sair do loop')

#Exemplo 2

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break