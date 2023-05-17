"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.


"""

# Problema 

def ver_log(funcao):
    def logar(*args, **kwargs):
        """ Eu sou  uma função(logar) dentro de outra """
        print(f'você está chamando: {funcao.__name__}')
        print(f'aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma 2 números"""
    return a + b

# print(soma(10,29))

print(soma.__name__) # soma 
print(soma.__doc__) # soma dois numeros 


# Resolução do problema acima 

from functools import wraps

def ver_log(funcao):
    @wraps(funcao) # aqui já resolve tudo
    def logar(*args, **kwargs):
        """ Eu sou  uma função(logar) dentro de outra """
        print(f'você está chamando: {funcao.__name__}')
        print(f'aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma 2 números"""
    return a + b

print(soma(10,29))

print(soma.__name__) # soma 
print(soma.__doc__) # soma dois numeros 
print(help(soma))