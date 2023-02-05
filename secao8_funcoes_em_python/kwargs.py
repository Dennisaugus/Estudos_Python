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
Nas nossas funções podemos ter:

- Parametros obrigatorios;
- *args;
- Parametros default (não obrigatorio)
- **kwargs

"""