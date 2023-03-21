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

