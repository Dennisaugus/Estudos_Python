""" 
Funções com retorno 

OBS: Em Python quando não se retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada 'return'

OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dados e até mesmo multiplos valores;

"""
numero = [1, 2, 3]

ret_pop = numero.pop()
print(f'Retorno de pop {ret_pop}')

ret_pr = print(numero)

print(f'Retorno de print {ret_pr}')

# Exemplo função

def quadrado_de_7():
    print(7 * 7)
    
ret = quadrado_de_7() # O retorno vai ser none porque apenas foi mandado imprimir 

print(f'Retorno {ret}')


# Vamos refatorar a função acima para retornar o valor  (Refatorar na programação é 'Reescrivar ou Redefinir')


def quadrado_de_7():
    return 7 * 7

# Criamos uma variavel para receber o retorno da função 
returno = quadrado_de_7()

print(f'Retorno {returno}')

print(f'Retorne de 7 * 7 {quadrado_de_7()}')



# Refatorando a primeira função da primeira aula de função
def diz_oi():
    return 'oi ' # usando o return te das flexibilidade do dado na hora de usar 

print(f'Retorno {diz_oi()}')


# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_ola(): 
    print('Estou sendo executado antes do retorno...') # será exibido este print
    return 'Olá! ' # a função acaba aqui 
    print('Estou sendo executado após o retorno...') # não será exibido este print
    

print(diz_ola())


# Exemplo 2 - Podemos ter em uma função, diferentes returns;
def nova_funcao():
    varaivel = False
    if varaivel:
        return 4
    elif varaivel is None:
        return 3.2
    return 'b'
        
        
print(nova_funcao())



# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dados e até mesmo multiplos valores;

def outra_funcao():
    return 1, 2, 3, 4

num1,num2,num3,num4 = outra_funcao()

print(num1, num2, num3, num4)
#print(outra_funcao()) Vai gerar uma tupla 


# Vamos criar uma função para jogar a moeda
from random import random

def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(f'A moeda caiu em: {joga_moeda()}')

# Você pode também na console python chegar o seu arquivo + a função criada com o Import
# >>> from funcoes_com_retorno import joga_moeda 


# Erros comuns na utilização do returno de uma função, mais que na verdade nem é um erro, mais sim
# codificação desnecessária

def e_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else: # é desnecessário usar o else, basta apenas colocar o return False
        return False


print(e_impar())