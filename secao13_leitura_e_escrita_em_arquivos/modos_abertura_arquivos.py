""" 
Modos de abertura de arquivos
http://docs.python.org/3/library/functions.html#open

r -> Abri para leitura - Padrão 
w -> Abri para escrita - sobrescreve caso o arquivo já exista
x -> Abri para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abri para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abri para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)


# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo
conteúdo será adicionado SEMPRE ao final do arquivo. Com o modo 'a' não controlamos o cursor.

"""
# Exemplo usando o 'x'
with open('novo_texto.yaml', 'x') as arquivo:
    arquivo.write('apiVersion: v1\n')
    arquivo.write('kind: Pod\n')
    arquivo.write('  metadata:\n')
    arquivo.write('name: kuard\n')

# tratando error do arquivo
try:
    with open('novo_texto.yaml','x') as arquivo:
        arquivo.write('apiVerion: v2\n')
except FileExistsError:
    print('Arquivo já existente')


# Exemplo 'a':
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair:')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

# Exemplo 'r+'
with open('frutas.txt','r+') as arquivo:
    arquivo.write('Adicionado\n')
    arquivo.seek(11)
    arquivo.write('Nova linha\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha\n')

    