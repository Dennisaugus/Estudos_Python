""" 
Try, Except, Else, Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.
"""

#num = int(input('Informe um número:'))
#print(f'Você digitou {num}')

#Exemplo de try/except:
try:
    num1 = int(input('informe um número:'))
except ValueError:
    print('Valor incorreto')
print(f'você digitou {num1}')

#Exemplo de else: Executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Exemplo de Finally
try:
    num2 = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor valido!')
else:
    print(f'você digitou o número {num2}')
finally: 
    print('Executando o finally')

#OBS: o bloco finally sempre é executado. Independente se houve exceção ou não.
# O finally geralmente é utilizado para fechar ou desalocar recursos.
# Finally é mais usado para finalizar uma seção de banco de dados ou de leitura de arquivos


# Exemplo mais complexo ERRADO:

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor errado!')


# Exemplo mais complexo CORRETO:
# OBS: Vocễ é responsavel pela entrada das funções. Então trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'
    

num1 = input('Informe o primeiro valor: ')
num2 = input('Informe o segundo valor: ')

print(dividir(num1,num2))


# Exemplo mais complexo - Generico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'
    
# Exemplo mais complexo - Semi-Generico
def dividir(a, b):
    try:    
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o seguinte erro: {err}'
