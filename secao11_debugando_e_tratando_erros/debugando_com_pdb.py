""" 
Debugando com PDB

PDB -> Python Debugger

Bug -> Inseto  (vida de inseto -> Life's Bug)

"""

# OBS: A utilização do print() para debugar código é uma prática ruim.
def dividir(a,b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'
    
print(dividir(4,7))


# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em python, podemos fazer isso em diferentes IDEs, como o Pytcharm ou utilizando 
# o PDB - Python Debugger 

# Exemplo utilizando o PyCharm

def devidir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4,7))   

# Exemplo com PDB - Python Debugger

# Para utilizar o python debugger, precisarmos* importar a biblioteca pdb e então utilizar 
# a função set_trace()

# Comando básicos do pdb
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

# Exemplo 1 
import pdb 

nome = 'Dennis'
sobrenome = 'Gusmao'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python '
final = nome_completo + 'faz o curso' + curso
print(final) 

# Exemplo 2
nome = 'Dennis'
sobrenome = 'Gusmao'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python '
final = nome_completo + 'faz o curso' + curso
print(final) 

# Porque as vezes utilizar este formato 
# O debugger é utilizado durante o desenvolvimento. Costumamos realizar os imports de 
# bibliotecas no inicio do arquivo. Por isso, ai invés de colocarmos o import do pdb no 
# inicio do arquivo, nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos
# a remoção 

# Exemplo 3 

# * A partir do python3.7 não é mais necessário importar a bibliotec pdb, pois o comando
# de debug foi incorporado como função built-in (integrada) chamada breakpoint()

nome = 'Dennis'
sobrenome = 'Gusmao'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python '
final = nome_completo + 'faz o curso' + curso
print(final) 

# OBS: Cuidade com conflitos entre nomes de variaveis e os comandos do pdb

def soma(l,n,p,c):
    breakpoint()
    return l + n + p + c

print(soma(1,3,4,5))

# (Pdb) p l -> imprime o valor da variavel
# (Pdb) p p -> imprime o valor da variavel
# (Pdb) p n -> imprime o valor da variavel

""" 
Como os nomes das varaiveis são os mesmos dos comandos do pdb, devemos utilizar
o comando p para imprimir as varaiveis. Ou seja, p nome_da_variavel
"""

# Nda de colocar nomes não representativos em variáveis. Sempre optar por nomes signifacitos.

def soma(num1,num2,num3,num4):
    breakpoint
    return num1 + num2 + num3 + num4

print(soma(1,34,67,54))