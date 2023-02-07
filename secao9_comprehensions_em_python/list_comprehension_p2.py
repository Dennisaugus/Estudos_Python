""" 
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension

"""

# Exemplo 1
numeros = [1,2,3,4,5,6,7,8]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

#Refatorando 

#Qualquer número par módulo de 2 é 0 e 0 em Python é False. net False = True
pares = [numero for numero in numeros if not numero % 2]
#Qualquer número impar módulo de 2 é 1, e 1 em Python é True 
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# Exemplo 2 

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)