""" 
Definindo Funções 

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: se você escrever uma função que raliza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos varias funções desde que foi inicado o curso:
- print()
- len()
- max()
- min()
- count()
e muitas outras:
"""

# Exemplo de utilização de funções 

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

curso = 'Programação em Python Essencial'
print(curso)
cores.append('roxo') # é uma função que está dentro de uma lista
print(cores)
#curso.append('Mais dados...') # AttributeError 
#print(curso)


cores.clear()
print(cores)