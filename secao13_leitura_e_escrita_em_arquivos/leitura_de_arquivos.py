""" 
Leitura de Arquivos:

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significar 'abrir'.

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

http://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/texto.txt' mode='r' encoding='UTF-8'>

mode r -> Mode de Leitura. r -> read() -> Ler


"""

#Exemplo

arquivo = open('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteudo de um arquivo, após sua abertura, devemos utilizar a função read()

retorno = arquivo.read()
print(type(retorno ))
print(retorno)

#print(arquivo.read())


# OBS: O python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor 
# funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())
# OBS: a função read() lê todo o conteudo do arquivo.


