""" 
Funções com Parâmetros Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;
"""

# Exemplo de função onde a passagem de parâmetro sejá opcional 
print('Dennis')
print() # Na função print, passar o parametro ou não é opcional

 # Exemplo de função onde a passagem de parâmetro é obrigatório 
def quadrado(numero):
     return numero ** 2

print(quadrado(3))
# print(quadrado()) # vai dar um erro porque a função quadrado é obrigatorio passar um numero


def exponencial(numero,potencia):
    return numero ** potencia

print(exponencial(3,2)) # 2 * 2 * 2 = 8
print(exponencial(2,3)) # 3 * 3 = 9


def expo(numero1=4,potencia1=2): # Os dois parametros podem ser opcionais 
    return numero1 ** potencia1

print(expo(3)) # Vai buscar o valor opcional do parametro potencia1 que é 2 e fara: 3 ** 2
print(expo(4,5)) # Faz o processo de alteração do valor do parametro potencial1 de 2 para 5 
print(expo()) # vai coletar os valores opcionais 

# OBS: se o usuário passar somente 1 argumento, este será atribuido ao parâmetro numero, e será calculado o quadrado deste número.
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potencia. Então 
# será calculada esta potência.

""" 
# OBS: Em funções Python, os parametros com valores default (padrão) DEVEM  sempre esta no final da declaração.

# ERRO
def teste(numero=2, potencia):
    return num ** potencia

print(teste(6))

"""

# Outro exemplos 

def soma(num1,num2):
    return num1 + num2

print(soma(4,2))
# print(soma(4)) # TypeError
# print(soma())  # TypeError 


# Exemplo mais complexo 
def mostra_informacao(nome='Dennis',professor=True,curso='ADS'):
    if nome == 'Dennis' and curso == 'ADS' and professor:
        return f'Olá professor {nome}, essa é a turma de {curso}'
    elif nome == 'Dennis' and curso == 'Engenharia de Software' and professor == False:
        return f'Olá professor {nome}, essa é a turma de {curso} e o senhor não é professor dessa turma'
    return f'Opá professor {nome}, você não faz parte de nenhum curso'

print(mostra_informacao())
print(mostra_informacao(professor=False))
print(mostra_informacao('Engenharia de Software'))
print(mostra_informacao('Ozzy'))

""" 
 Por que utilizar parametros com valores defaults ?

 - Nos permite ser mais flexiveis nos Funções;
 - Evita erros com parametros incorretos;
 - Nos permito trabalhar com exemplos mais legiveis de código.


 Quais tipos de dados podemos utilizar como valores default para parametros ?
 
 - Qualquer tipo de dado:
    - Integer;
    - Strings;
    - Floats;
    - Boolean;
    - List;
    - Tuple;
    - Dict;
    - Function;
    - and etc...;
"""

# Exemplos de funções com o parametro de outra função:
# OBS: não é comum em outras linguagens de programação 

def soma(num1, num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def mat(num1,num2, fun=soma):
    return fun(num1,num2)

print(mat(2,3))
print(mat(4, 5, subtracao))


# Escopo - Evitar problemas e confusões ...

# Variaveis Globais 
# Variaveis Locais 

instrutor = 'Dennis' # Varaivel Global

def diz_oi():
    instrutor = 'Matheus' # Variavel Local
    return f'Olá {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome da variavel global, a local terá preferencia 



