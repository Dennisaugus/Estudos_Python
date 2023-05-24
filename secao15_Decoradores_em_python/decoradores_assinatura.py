"""
Decoretors com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto chamado: Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

"""

# Relembrando Decorators 

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento} por favor'

# Testar

# print(saudacao('Dennis'))

# print(ordenar('Ovo cozido', 'Pão integral'))



# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor!'

print(saudacao('Dennis'))

print(ordenar('Ovo cuzido', 'pão integral'))


@gritar
def lol():
    return 'lol'

print(lol())


# OBS: vale lembrar que podemos utilizar parâmetros nomeados 

print(ordenar(acompanhamento='Ovo Cuzido', principal='Pão Integral'))



# Decorator com argumentos 

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10,12)) # 22

print(soma_dez(1,21)) # Valor incorreto! Primeiro argumento precisa ser 10

print(comida_favorita('pizza', 'churrasco')) # pizza churrasco

print(comida_favorita('lazanha', 'pizza')) # Valor incorreto! Primeiro argumento precisa ser pizza