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


# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

# Mas então, como definir funções?
""" 
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entradas -> São opicionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opicionais ou não:
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que 
estamos definindo uma função. Também abrimos o bloco de código com o já cenhecimento dois pontos :
que é utilizado em Python para definir blocos.

"""

# Definindo a primeiro função:

def diz_oi():
    print('oi')
    
""" 
Obs:
1 - Veja que, dentro da nossa função podemes utilizar outra função;
2 - Veja que nossa função executa uma tarefa, ou seja a única coisa que ela faz é dizer oi;
3 - Veja que está função não recebe nenhum parametro de entrada;
4 - Veja que está função não retorna nada;

"""
# Utilizando funções:
# chamada de execução
diz_oi()
# OBS: ATENÇÃO, nunca esqueca de utilizar o parenteses ao executar uma função.


# Exemplo de função 2
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades para você')
    
cantar_parabens()
cantar_parabens()

for n in range(4):
    cantar_parabens()
    
# Em Python podemos incluse criar variaveis do tipo de uma função e executar está função atraves da variavel 

canta = cantar_parabens # aqui é sem o parenteses

canta()


# Exemplo mais prático com funções:
def media_aluno(media):
    if media >= 7:
        print(f'aluno aprovado com a nota: {media}')
    elif media <7 and media > 5:
        print(f'aluno em recuperação com a nota: {media}')
    else:
        print(f'aluno reprovado com a nota: {media}')
        

media = float(input('Informa a nota do aluno:'))
media_aluno(media)


def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    return salario

str_horas = input('Digite as horas: ')
str_taxa = input('Digite a Taxa: ')
total_salario = calcular_pagamento(str_horas, str_taxa)
print('O valor de seus rendimentos é R$', total_salario)