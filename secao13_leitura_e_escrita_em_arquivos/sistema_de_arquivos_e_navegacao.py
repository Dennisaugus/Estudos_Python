""" 
Sistema de arquivos e navegação 

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do modulo os.

os -> Operating System - Sistema operacional
"""

# Fazer o import 
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto 
print(os.getcwd()) # /dir1/dir1.1/dir1.1.1

# Para mudar de diretorio, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd()) # /dir1/dir1.1

os.chdir('..')
print(os.getcwd()) # /dir1 

# Podemos checar se um diretorio é absoluto ou relativo 
print(os.path.isabs('/home/aqrl-dennis-gusmao/')) # True (absoluto)
print(os.path.isabs('home/aqrl-dennis-gusmao/')) # False (relativo)

# OBS: para usuários Windows:
# Se você infelizmente, estiver utilizando um computador com windows,
# terá que ter cuidado ao verificar diretórios.

# checando em SO Windows 
print(os.path.isabs('C:\\Users\\aqrl-dennis-gusmao'))

# Podemos identificar o sistema Operacional com o modulo os 
print(os.name) # posix (Linux e Mac), nt (windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname()) 

# Fazer import
import sys
print(sys.platform)

# Processo de junção de diretorios 
print(os.getcwd()) # /dir1/dir1.1/dir1.1.1
res = os.path.join(os.getcwd(),'dir1.1.1.1')
os.chdir(res)
print(os.getcwd()) # /dir1/dir1.1/dir1.1.1/dir1.1.1.1

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro 
# o diretório atual e o segundo o diretório que será juntado ao atual.


# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir())

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()
arquivos = list(scanner)

print(os.scandir('/etc'))
print(list(os.scandir('/etc')))

print(arquivos[0].inode()) # número desse elemento na arvore de diretórios
print(arquivos[0].is_dir()) # é um diretório? false 
print(arquivos[0].is_file()) # é um arquivo? true
print(arquivos[0].is_symlink()) # é um link simbolico? false
print(arquivos[0].name) # nome do arquivo 
print(arquivos[0].path) # caminho até o arquivo 
print(arquivos[0].stat()) # Estatisticas sobre o arquivo 

#OBS: Quando utilizamos a função scandir() nós precisamos fechá-las,
# assim quando abrimos um arquivo.  