""" 
Erros mais comuns no Python

ATENÇÃO:
É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução
do nosso codigo 

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o python encontra um erro de sintaxe. Ou seja, você escreveu algo que 
o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError
a)
def funcao:
    print('Dennis ')

b)
None = 1
def = 1

c)
return


2 - NameError -> Ocorre quando uma variavel ou função não foi definida.

# Exemplos de NameError
a)
print(dennis)

b)
funcao()

c) 
a = 18
if a < 10:
    msg = 'É maior que 10'
print(msg)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo erro 

# Exemplos de TypeError
a)
print(len(5))

b)
print('Dennis' + [])
print('Dennis' + 4)


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.

# Exemplos de IndexError 
a)
lista = ['Dennis']
print(lista[2])
print(lista[0][10])

b)
tupla = ('Dennis',)
print(tupla[0][10])


5 - ValueError -> Ocorre quando uma função ou operação built-in (integrada) recebe um argumento com o tipo
correto mas valor inapropriado.

# Exemplos de ValueError
print(int('Dennis'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
# Exemplos KeyError

a)
dict = {}  #vai dar certo (dict = {'dennis': 'meu nome'})
print(dict['Dennis'])

b)
dict = {'Python':'Console'}
print(dict['Dennis'])



7 - AttributeError -> Ocorre quando uma variavel não tem um atributo/função.

# Exemplos AtrributeError 
a)
tupla = (11,2,31,4)
print(tupla.sort())


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos IndentationError

a)
def nova():
print('Dennis')

b)
for i in range(10):
i + 1


OBS: Exceptions e Erros são sinônimos na programação.
OBS: Importante lê e prestar atenção na saída de erro.
"""




