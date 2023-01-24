"""
Dicionários:

OBS: Em algumas linguagens de programação, os dicionários são conhecidos por 'Mapas'.

Dicionários são coleções do tipo chave/valor.

[0, 1, 2] -> chave
[1, 2, 3] -> valor

Dicionários são representados por chaves {}

OBS: Sobre dicionários:
    - chave e valor serparados por dois pontos 'chave':'valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados: 
"""
print(type({}))

#Criação de Dicionários:
#Forma 1 -> Mais comum
paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#Forma 2 -> Menos comum
paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))