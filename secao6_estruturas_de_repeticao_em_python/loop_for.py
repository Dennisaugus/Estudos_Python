""" 
Loop for 

Loop -> Estrutura de repetição
For (para) -> Uma dessas estruturas 

C ou Java

for(int i = 0; i < 10; i ++){
    //execução do loop
}

#Em Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou valores interáveis (interagir)

Exemplos de interaveis:
- String
   nome = 'Dennis Augusto'
- Lista
   lista = [1, 3, 5, 6,]
- Range 
    numero = range(1, 10)    
"""

nome = 'Dennis Augusto'
lista = [1, 3, 5, 6,]
numeros = range(1, 10) #Temos que transformar em uma lista 
#Exemplo de for 1
for letra in nome: # for (cada) in (dentro)
    print(letra)

#Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobre uma range)
""" 
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive 
1
2
3
4
5
6
7
8
9
10 - não é inclusive
"""
for numero in range(1,10):
    print(numero)
    
""" 
Enumerate:
(0, 'D', (1, 'e', (2, 'n')...)
"""    
for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome):
    print(letra)
    
#Descartando o indice  
#OBS: quando não precisarmos de um valor, podemos descartá-lo utilizando um underline (_) 
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

#Mostrando apenas os indices/posicao
for valor in enumerate(nome):
    print(valor[0])

#Mostrando apenas as letras
for valor in enumerate(nome):
    print(valor[1])
    
qtd = int(input('quantas vezes esse loop deve rodar:'))
#de  1 até a qtd
for n in range(1, qtd):
    print(f'Imprimindo {n}')
#de 1 até a qtd + 1     
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
    
qtd = int(input('Quantas vezes esse loop deve rodar:'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informa o {n}/{qtd} valor:'))
    soma += num
    print(f'A soma é {soma}')
              
#exibe o resultado na mesma linha 
nome = 'Dennis Augusto Gusmao'
for letra in nome:
    print(letra, end='')
    
    
""" 
Exemplos na console do python:
Concatena
>>> nome = 'Dennis'
>>> nome + ' Augusto'
'Dennis Augusto'

Imprime o valor da variavel numas determinadas vezes 
>>> nome = 'Dennis'
>>> nome * 3
'DennisDennisDennis'
>>> nome * 34

"""

#Brincando com emojis
#Original U+1F680
#Modificado U0001F680
for num in range(1, 11):
    print('\U0001F680' * num)
    
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F680' * num)