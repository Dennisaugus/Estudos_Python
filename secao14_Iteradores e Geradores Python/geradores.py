"""
Geradores 

- Geradores (Generators) são Iterators (Iteradores)

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradores utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

--------------------------------------------------------------------------------------
/ Funções                                 / Generator Functions                      /
--------------------------------------------------------------------------------------
/ utilizam return                         / utilizam yield                           /
--------------------------------------------------------------------------------------
/ retorna uma vez                         / podem utilizar yield múltiplas vezes     /
--------------------------------------------------------------------------------------
/ quando executada, retorna um valor      / quanto executada, retorna um generator   /
--------------------------------------------------------------------------------------


"""

# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # faz uma contagem de 1 em 1
        contador += 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok ?

gen = conta_ate(5)

#print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen1 = conta_ate(10)

for num in gen1:
    print(num)

print(next(gen1)) # começa do 1

print('---------------------')

for num in gen1: # começa do 2 
    print(num) 

gen = list(conta_ate(10))
print(gen)

