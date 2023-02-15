""" 
Generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension...Porque elas se chamam Generators
"""

nomes = ['Carlos', 'Camila','Carla','Cassiano','Cristina','Vanessa']

print(any(nome[0] == 'C' for nome in nomes)) # Não é list comprehension
print(any([nome[0] == 'C' for nome in nomes])) # List comprehension
# Resultado True

# Diferença entre List comprehension e Generator

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)
# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro 
from sys import getsizeof

#Mastra quantos bytes a string 'Dennis' esta ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Dennis'))
print(getsizeof('Augusto Santos Gusmão'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(14812641469124))
print(getsizeof(True))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)]) # range 0 até 999

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)}) # range 0 até 999

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x : x * 10 for x in range(1000)}) # range 0 até 999

# Gerando uma lista de número com Generator
gen = getsizeof(x * 10 for x in range(1000)) # range 0 até 999

print('Para fazer a mesmo terafa gastamos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')


# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

