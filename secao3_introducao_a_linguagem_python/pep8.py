"""
PEP8 - Python Enhacement Proposital

São propostas de melhorias para a linguagem python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos python de forma pythonica

[1] - Utilize Canel Case para nomes de classes;

class Calculadora:
    pass


class Calculadora_Cientifica:
    pass


[2] - utilize nomes em minusculo, separados por underline para funções ou varivaveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 3


[3] - utilize 4 espaços para identação!

if 'a' in 'banana' :
    print('temm')


[4] - Denifa 2 linhas em branco
- Separar funções e definições de classes com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco;


[5] - Imports:

#Import Errado
import sys,os

#Import Correto
import sys
import os

#Não ha problemas em utilizar

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se usar:

from types import {
    StringType,
    ListType,
    SetType,
    OutroType
}

#Imports devem ser colocados no topo do arquivo. Logo depois de quaisquer comentarios ou docstrings
# antes de constantes ou variaveis globais.


[6] - Espaços em expressões e instruções

#Não faça:
funcao(_algo[_1_], {_outro: 2_}_)

# Faça:
funcao(algo[1], {outro: 2})

#Não Faça:
algo_(1)

#Faça:
algo(1)

#Não faça:
dict ['chave'] = lista[indice]

#Faça:
dict['chave'] = lista[indice]

#Não faça
x                = 1
y                = 2
varaivel_longa   = 3

#Faça:
x = 1
y = 2
variavel_longa = 3


[7] - Termine sempre uma instrução com uma nova linha em branco


"""

'''
pode-se fazer mais utilize com aspas duplas
'''





