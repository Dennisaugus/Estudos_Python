""" 
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer em nosso código.
Previnindo que o programa pare de funcionar e o usuário receba mensagens de erro inesperados.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //O que deve ser feito em caso de problema

"""

# Exemplo 1 - tratando um erro generico
try:
    dennis()
except:
    print('Deu algum problema')

# Tente executar a função dennis(), caso vocẽ encontre erros, imprima a mensagem de erro.


# Exemplo 2 - Tratando um erro generico
try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função len(), caso você encontre erros, imprima a mesnagem de erro.

#OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE
#tratar de forma específica.


# Exemplo 3 - Tratando um erro específico

try:
    dennis()
except NameError:
    print('Você está utilizando uma função inexistente')
    
# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você esta utilizando uma função inexistente')
    
# Exemplo 5 - Com detalhes do erro 
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
    

# Exemplo 6 - Podemos efetuar diversos tratamentos de erros de uma vez
try:
    len(5)
    #dennis()
except NameError as erra:
    print('Deu NameError: {erra}')
except TypeError as errb:
    print('Deu TypeErro: {errb}')
except:
    print('Deu um erro diferente')
    

# Exemplo 7 - tratando os dados de entrada 
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'dennis'}

print(pega_valor(dic, 'maria'))