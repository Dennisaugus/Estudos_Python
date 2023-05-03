""" 
Entendo o *args

- o *args é um parametro, como outro qualquer, isso significa que você poderá 
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mais oque é o *args ?

O parametro *args utilizado em uma função, coloca os valores extras informados como 
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

#Exemplo não legal

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4,5,9))
print(soma_todos_numeros(4,6))
print(soma_todos_numeros(4,6,7,8))

"""

# Entendendo os args

def soma_todos_numeros(*args):
   return sum(args)
   """ total = 0
    for numero in args:
        total += numero
    return total 
    """
print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2,3))
print(soma_todos_numeros(4,5,6))
print(soma_todos_numeros(1,2,3,4,6))

# Outro exemplo 

def aluno(nome, email, *args):
    return sum(args)

print(aluno('Dennis', 'dennisasg@outlook.com', 23.4))
print(aluno('Maria','mariaasg@outlook.com'))
print(aluno('Jose','joseasg@outlook.com',2 ,3 ,5 ,6)) 

# Mais um exemplo utilizando o *args

def verifica_info(*args):
    if 'Dennis' in args and 'Gusmão' in args:
        return 'Bem-vindo Dennis'
    return 'Eu não tenho certeza de quem é você...'

print(verifica_info())
print(verifica_info(1, True, 'Gusmão', 'Dennis'))
print(verifica_info(1, 'Gusmão', 3.453))


def soma_todo(*args):
    return sum(args)

print(soma_todo())
print(soma_todo(1,2,3,4,5,6,))

numeros = [ 1, 5, 184, 53]

# Desempacotador

print(soma_todo(*numeros)) 

# OBS: O asterisco server para que informemos ao Python que estamos 
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.

