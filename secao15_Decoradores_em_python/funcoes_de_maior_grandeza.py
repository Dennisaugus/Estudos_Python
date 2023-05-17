"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa:

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo podemos passar funções
como argumentos para outras funçõess, e até mesmo criar variáveis do tipo de funções 
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em python as funções são Cidadões de Primeira Classe (Firts Class Citizen)
"""

# Exemplo - definindo as funções 

def somar(a,b):
    return a + b

def diminuir(a,b):
    return a - b 

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b 

def calcular(n1,n2,funcao):
    return funcao(n1, n2)


# Testando as funções 

print(calcular(4,3, somar))

print(calcular(4,3, diminuir))

print(calcular(4,3, multiplicar))

print(calcular(4,3,dividir))


# Nested Functions - Funções Aninhadas 

"""
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions 
ou também Inner Functions (Funções internas)
"""

# Exemplo 
from random import choice 

def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'suma daqui', 'gosto muito de você'))
    return humor() + pessoa

# Testando 

print(cumprimento(' Dennis'))
print(cumprimento(' Amanda'))


# Retornando funções de outras funções 

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahah', 'kkkkkkkkkkk','yayayayaya'))
    return rir

# Testando 

rindo = faz_me_rir()
print(rindo())

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('lalala','lolol','lulu'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando 

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())

