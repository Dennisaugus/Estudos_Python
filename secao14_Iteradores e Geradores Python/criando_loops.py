"""
Criando sua própria versão de loop


"""

#Exemplo de for simples 
for numero in [1,2,3,4,5,6]:
    print(numero)

for letra in 'Dennis Augusto':
    print(letra)

iter([1,2,3,4,5,6])

iter('Dennis Augusto')

#Criando seu próprio for 

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Dennis Augusto Gusmão')


numeros = [1,2,3,4,5,6,7,8]
meu_for(numeros)

