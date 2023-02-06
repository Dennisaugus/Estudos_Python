""" 
**kwargs

Poderiamos chamar este parametro de **xis, mais por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parametros nomeados, e transforma esses 
parametros extras em um dicionário.
"""

# Exemplo 

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A Cor favorita da Pessoa: {pessoa.title()} é {cor.title()}')
    
cores_favoritas(dennis='verde', julia='rosa', marta='preto', flavio='vermelho')


def salario_fun(**kwargs):
    for fun, sala in kwargs.items():
        print(f'O funcionário: {fun.title()}, recebe o salário de: {sala} R$')
    
salario_fun(dennis=7500.0, julia=6800.0, marta=8700.0, flavio=10000.0)

# OBS: Os parametros *args e **kwargs não são obrigatórios.
cores_favoritas()
cores_favoritas(Catarina='azul')


# Exemplo mais complexo 

def comprimento_especial(**kwargs):
    if 'dennis' in kwargs and kwargs['dennis'] == 'Python':
        return 'Você recebeu um comprimento Pythonico Dennis!'
    elif 'dennis' in kwargs:
        return f"{kwargs['dennis']} Dennis!"
    return 'Não tenho certeza quem você é...'

print(comprimento_especial())
print(comprimento_especial(dennis='Python'))
print(comprimento_especial(dennis='Oi'))
print(comprimento_especial(dennis='especial'))

""" 
Nas nossas funções podemos ter (NESTA ordem):

- Parametros obrigatorios;
- *args;
- Parametros default (não obrigatorio)
- **kwargs

"""

def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    
minha_funcao(8, 'Julia')
minha_funcao(18,'Felicity', 4,5,6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla',9,4,5,java=False, python=True)

# Entenda por que é importante manter a ordem dos parametros na declaração

#Função com a ordem correta de parametros 
def mostra_info(a,b,*args, instrutor='Dennis', **kwargs):
    return [a,b,args,instrutor,kwargs]

#Função com a ordem incorreta de parametros 
#def mostra_info(a,b, instrutor='Dennis',*args, **kwargs):
#    return [a,b, args, instrutor, kwargs]

""" 
a = 1
b = 2
args = (3,)
instrutor = 'Dennis'
kwargs = {'sobrenome': 'Augusto', 'cargo': 'Instrutor'}
"""


print(mostra_info(1,2,3,sobrenome='Augusto', cargo='Instrutor'))
# Resultado: [1,2, (3,), 'Dennis', {'sobrenome': 'Augusto', 'cargo': 'Instrutor'}]
# Resultado da forma incorreta: [1,2, (), 3, {'sobrenome':'Augusto', 'carg':'Instrutor'}]


# Desempacotar com kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Dennis', 'sobrenome': 'Augusto'}

print(mostra_nome(**nomes))


def soma_multiplos_numeros(a,b,c, **kwargs):
    print(a + b + c)
    
lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
# OBS: Os nomes da chave em um dicionario devem ser os mesmos dos parametros da função
dicionario = dict(a=1,b=2,c=3)

soma_multiplos_numeros(**dicionario)
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario, lang='Python')

