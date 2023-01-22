'''
Tipo float (Tipo real ou decimal)

Casas decimais 

OBS: o separador de casas decimais na programação é o ponto e não a virgula 

#Errado
valor = 1,54 (o python vai achar que essa variavel é uma tupla)

#Certo do ponto de vista do float
valor = 1.54
'''

# é possivel fazer dupla atribuição 
valor1, valor2 = 1, 45
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int 
#OBS: ao converter valores de float para inteiros, perdemos precisação no resultado
valor = 1.44
res = int(valor)
print(type(valor))


#Podemos trabalhar com numereos complexos 
1j
type(1j) 