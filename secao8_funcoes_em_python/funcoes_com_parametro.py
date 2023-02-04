""" 
Funções com Parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pansar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mais possuem saída;
- Possuem entrada e saída;
"""

# Refatornado uma função:

def quadrado_de_7():
    return 7 * 7
   
print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())

def quadrado(numero):
    return numero * numero
    #return numero ** 2
print(quadrado(7))
print(quadrado(3))
print(quadrado(100))

ret = quadrado(56)
print(ret)

# print(quadrado()) # TypeError

def programador(dev):
    print(f'Bem vindo Dev: {dev}')
    

programador('Dennis Augusto')


def soma(a, b): # chamado de parâmetro -> (a, b)
    return a + b

def nome_completo(nome,nomedomeio,ultnome): # chamado de parâmetro -> (nome,nomedomeio,ultnome)
    return nome + nomedomeio + ultnome


def fun_aquarela(nome,cargo,idade): #chamado de parâmetro -> (nome,cargo,idade)
    return nome + cargo + idade


print(f'a soma é {soma(2,3)}') # soma(2,3) -> Chamado de argumentos (o 2,3)
print(f'Seu nome completo é:{nome_completo("Dennis ", "Augusto ", "Gusmão")}') # nome_completo("Dennis", "Augusto", "Gusmão") -> chamado de argumentos (os nomes)
print(f'Bem vindo Funcionário: {fun_aquarela("Dennis ", "DevOps ", "28")} anos!')

# OBS: Se a gente informar um número errado de parâmetros, teremos um TypeError
# Exemplo: print(soma(2,3,5)) - Passando argumentos a mais 
# Exemplo: print(soma(2)) - Passando argumentos a menos 

# A diferença entre Parâmetros e Argumentos:
# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# Nomeando Parâmetros 

def nome_completo(nome,sobrenome):
    return f'Seu nome é : {nome} {sobrenome}'

print(nome_completo('Dennis ', 'Augusto'))

# A ordem dos parâmetros importa!
nome = 'Edgar'
sobrenome = 'Silva'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
print(nome_completo(nome='Maria', sobrenome='Cristina'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Carlota', nome='Carolina'))

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total # Não deixe o return na estrutura de linha do if 

lista = [1,2,3,4,5,6,7,8,9]
print(soma_impares(lista))

tupla = 1,2,3,4,5,6,7,8
print(soma_impares(tupla))

