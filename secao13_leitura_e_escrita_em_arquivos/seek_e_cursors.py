""" 
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.
"""

arquivo = open('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/texto.txt')

#print(arquivo.read())


"""
seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo
ela recebe um parametro que indica onde queremos colocar o cursor.
"""

# Movimentando o cursor pelo arquivo com a função seek()
#arquivo.seek(0)


#arquivo.seek(20)
#print(arquivo.read())


# readline() -> Função que lê o arquivo linha por linha (readline -> lê linha)

print(arquivo.readline())

print(arquivo.readline())

print(arquivo.readline())


# readlines() -> transforma as linhas em uma lista
linhas = arquivo.readlines()
print(len(linhas))

"""
OBS: quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. 
Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos
o função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Trabalhar o arquivo;
3 - Fechar o arquivo;
"""

# 1 - abrir o arquivo:
arquivo = open('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/texto.txt')

# 2 - Trabalhar o arquivo:
print(arquivo.read())

print(arquivo.closed) # False - verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo:
arquivo.close()

print(arquivo.closed) # True - verifica se o arquivo está aberto ou fechado

print(arquivo.read())
# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError 

# Com a funlção read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
# print(arquivo.read(50)) -> exibe apenas os 50 caracteres

