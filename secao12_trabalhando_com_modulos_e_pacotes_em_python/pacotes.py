""" 
Pacotes

Módulo -> é apenas um arquivo python que pode ter diversas funções para utilizarmos; 
Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote python deveria conter dentro dele um arquivo chamado
__init__.py

Nas versões do python 3.x, não é mais obrigatória a utilização deste arquivo, mas
normalmente ainda é utilizdo para manter compatibilidade.

"""

from dennis import dennis1, dennis2
#acesso a um sub-modulo
from dennis.augusto import dennis3,dennis4
print(dennis1.pi)

print(dennis1.funcao1(4,6))

print(dennis2.curso)
print(dennis2.funcao2())

print(dennis3.funcao3())
print(dennis4.funcao4())

# Importando apenas a funcao 
from dennis.dennis1 import funcao1
print(funcao1(4,7))