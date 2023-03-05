"""  
Levantando os próprios erros com o Raise 

raise -> lança exceções.
OBS: O raise não é uma função, e sim uma palavra reservada assim como o def ou qualquer 
     outra em Python

Para simplificar, pense no raise sendo util para que possarmos criar nossas próprias exceções 
e mensagens de erros.

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
        raise ValueError(f'Os valores de cores precisam estar conforme esta lista: {cores}')
        # print('Depois do reise') não vai ser executo caso o raise seja acionado
    print(f'o texto é {texto} e a cor é {cor}')
    
colore('dennis', 'verde')


def user(nome,cpf,numero,sexo):
    genero = ('Masculino', 'Feminino')
    if type(nome) is not str:
        raise TypeError('é necessário passar apenas letras para o nome')
    if type(cpf) is not int:
        raise TypeError('é necessário passar apenas números para o cpf')
    if type(numero) is not int:
        raise TypeError('é necessário passar apenas números para o telefone')
    if type(sexo) is not str:
        raise TypeError('é necessário passar apenas letras para o sexo')
    if sexo not in genero:
        raise ValueError(f'é necessário que passe apenas esse dois sexos: {genero}')
    print(f'O usuário do nome: {nome} com o CPF: {cpf}, do número: {numero} e do genero: {sexo}')

user('Dennis',10311444474,948847011,'Masculino')
