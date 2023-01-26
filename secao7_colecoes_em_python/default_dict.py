"""
Módulo Collections  - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict
    
# Recaptulando o dicionário:
dicionario = {'Curso': 'Programação em Python Essencial'}
print(dicionario) #imprimi o dicionario em si
print(dicionario['Curso']) # imprimi o valor da chave
print(dicionario['outro']) # vai gerar um KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentamos acessar uma chave que não exista, essa chave será 
criada e o valor default será atribuida.  

OBS: Lambdas são funções sem nome que podem ou não receber parametros de entrada e retornar valores.  
"""

# Fazendo import 
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)
dicionario['curso'] = 'Programação em Python'
print(dicionario)

print(dicionario['outro'])
print(dicionario)

