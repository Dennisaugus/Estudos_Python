""" 
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package
Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

pip install --upgrade pip -> atualiza os pacotes do pip

colorama -> é utilizado para permitir impressão de textos coloridos no terminal.
"""
#Utilizando o pacote instalado 
# pip install colorama
from colorama import init,Fore 
init()
print(Fore.BLACK + 'Dennis')
print(Fore.BLUE + 'Dennis Augusto')

import pydf
pdf = pydf.generate_pdf('<h1> Dennis</h1>')
with open('test_doc.pdf','wb') as f:
    f.write(pdf)