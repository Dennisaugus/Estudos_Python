"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(receita)
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} : Recebi {receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys(): # Forma pythonica 
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

#Desempacotamento de dicionários:
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

#Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reias

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
