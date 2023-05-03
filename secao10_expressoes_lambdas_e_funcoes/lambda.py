""" 
Utilizando lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função em Python
def soma(a,b):
    return a + b 
    
"""
# Exemplo de Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(6))
print(funcao(7))

#Exemplo da mesma Função em Lambda
lambda x: 3 * x + 1

# E como usar a expressão lambda
calc = lambda x: 3 * x + 1
print(calc(6))
print(calc(7))


# Podemos ter expressões lambdas com múltiplas entradas
# uso do strip() -> usado para remover os espaços dentro da variavel
# Exemplo:
# nome = '  dennis augusto '
# nome.strip()
# 'dennis augusto'
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' dennis', ' AUGUSTO'))
print(nome_completo(' vera  ', 'lucia   '))


# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também 

amar = lambda: 'Como não amar Python! '
uma = lambda x: 3 ** x + 1
duas  = lambda y, z: (y ** z) ** 3
tres = lambda x1, x2, x3: x1 + x3 / x2

print(amar())
print(uma(9))
print(duas(8,10))
print(tres(40,34,10))

#OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo

autores = ['Monteiro Lobato', 'José de Alencar', 'Cecília Meireles', 'Carlos D. de Andrade','Machado de Assis'
           , 'Clarice Lispector', 'João Cabral de Melo Neto', 'Graciliano Ramos', 'Mario Quintana','Guimarães Rosa'
           , 'Ruth Rocha', 'L. F. Veríssimo','Conceição Evaristo']
#print(autores)
# Função lambda para extrassão do sobrenome:
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Função quadrática
#f(x) = a * x ** 2 + b * x + c
# Definindo a função
def geradora_funcao_quadratica(a,b,c):
    """ Retorna a função f(x) = a*x*2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2,3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3,0,1)(2))


