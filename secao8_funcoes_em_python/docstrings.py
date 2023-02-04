""" 
Documentando funções com Docstrings

print(help(print))

"""

# Exemplos

def diz_oi():
    """ Uma função simples que retorna a string Oi! """
    return 'Oi'

#Execute no terminal python 
# from docstrings import diz_oi
# diz_oi()
# help(diz_oi)
# print(diz_oi.__doc__)

print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)

# OBS: Podemos ter acesso a documentação de uma função em Python 
# utilizando a propriedade especial __doc__
# Podemos ainda fazer acesso a documentação com a função help()

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

# Execute no terminal python
# from docstrings import exponencial
# exponencial.__doc__
# help(exponencial)

