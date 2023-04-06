""" 
Sistema de Arquivos  - Manipulação

"""
import os 
# Descobrindo se um arquivo ou diretório existe:
# Path relativos
print(os.path.exists('texto.txt'))
print(os.path.exists('arquivo.txt'))

# Path absolutos
print(os.path.exists('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/frutas.txt'))

# Criando arquivos
# Forma 1
open('arquivo-test.py','w').close()

# Forma 2
open('arquivo-test2.txt','a').close()

# Forma 3
with open('arquivo-test3.txt','w') as arquivo:
    pass

# melhor forma de criar arquivos

# Caminho relativo
os.mknod('arquivo-test8.txt')

# Caminho absoluto
os.mknod('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/arquivo-test11.txt')

# OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError 
# OBS2: Criando um arquivo via mknod() se o arquivi já existir teremos o erro FileExistsError


# Criando diretórios - Únicos (um a um)
# Caminho Relativo 
os.mkdir('templates')

# Caminho Absoluto
os.mkdir('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/dir1')
# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError


# Criando mult-diretorios (árvore de diretórios):
os.makedirs('/home/aqrl-dennis/PycharmProjects/Estudos_Python/secao13_leitura_e_escrita_em_arquivos/dir1/dir1.1')

# OBS: Se já existir, teremos um FileExistsError 

os.makedirs('/home/aqrl-dennis/PycharmProjects/novo2/outro2', exist_ok=True)
# Se existir, ignora e não gera o error


# Renomear um diretorio
os.rename('templates2','dennis2')
os.rename('dennis2/dennis','dennis3')
# OBS: Se o diretorio não existir teremos um FileNotFoundError 
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomear um Arquivo
os.rename('dennis2/novo2/outro3/teste.txt','dennis.txt')

# ATENÇÃO! tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, 
# eles não vão para a lixeira. Eles somem.

os.remove('novo.txt')