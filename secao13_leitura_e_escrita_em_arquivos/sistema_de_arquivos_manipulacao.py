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

# Removendo arquivos
os.remove('novo.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você tera um erro.
# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretorio ao invés de um arquivo, teremos um IsADirectoryError


# Removendo diretorios vazios
os.rmdir('templates')

# OBS: Se o diretorio tiver qualquer conteúdo, teremos um OSError
# OBS: Se o diretorio não existir teremos um FileNotFoundError

# Removendo uma arvore de diretorios    
os.removedirs('templates/outro/mais')

# Se algum dos diretorios contiver arquivos ou outros diretórios, o processo para.

#ATENÇÃO: Ao remover arquivos e deretórios com Python eles não vão para a lixeira. Eles vão embora.

# Instalando bibliotecas de terceiros 
# sudo apt-get install lsb-core
# pip install send2trash

from send2trash import send2trash
os.remove('arquivo1.txt') # não vai para a lixeira. É deletado imediatamente

send2trash('arquivo2.txt') # Vai para lixeira. Pode ser restaurado 
# Se o arquivo não existir, teremos OSError

# Removendo diretorio 
send2trash('teste') # vai para a lixeira 

# Trabalhando com arquivos e diretorios temporários
import tempfile
import os

# Criando um diretorio temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('dennis\n')
    input()

# Estamos criando um diretorio temporario, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando
# o windows. Por conta desse sistema trabalhar de forma diferente com arquivos
# temporários.


# Criando um arquivo temporário 
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'dennis\n') # b -> converte uma string para binários 
    tmp.seek(0)
    print(tmp.read())

# OBS: em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''

# Pode ser feito desta forma também:
arquivo = tempfile.TemporaryFile()
arquivo.write(b'dennis augusto\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'dennis\n')
print(arquivo.name)
input()
arquivo.close()