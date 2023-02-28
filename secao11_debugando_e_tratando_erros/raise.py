"""  
Levantando os próprios erros com o Raise 

raise -> lança exceções.
OBS: O raise não é uma função, e sim uma palavra reservada assim como o def ou qualquer outra em Python

Para simplificar, pense no raise sendo util para que possarmos criar nossas próprias exceções e 
mensagens de erros.

A forma geral de se utilizar é:

raise TipoDoError('Mensagem de erro')

# Exemplo:
raise ValueError('Valor incorreto')

"""

# Exemplo real:

def colore(texto, cor):
    cores = ('verde','amarelo','azul','vermelho')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser declarado como uma string')
    if type(cor) is not str:
        raise TypeError('A Cor precisa ser decalarada como uma string')
    if cor not in cores:
        raise ValueError(f'Os valores de cores precisam estar com forme esta lista: {cores}')
        # print('Depois do reise') não vai ser executo caso o raise seja acionado
    print(f'o texto é {texto} e a cor é {cor}')
    
colore('dennis', 'verde')