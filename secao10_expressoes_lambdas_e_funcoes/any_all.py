""" 
Any e All

all() -> Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio.

any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False
"""

# Exemplo all()
print(all([0,1,2,3,4,5])) # Todos os números são verdadeiros ? Resultado igual a False por causa do 0
print(all([1,2,3,4,5])) # Todos os números são verdadeiros !
print(all([])) # lista vazia 
print(all('Dennis')) # dados de strings

nomes = ['Carlos', 'Camila','Carla','Cassiano','Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou'])) 
#OBS: Um iteravel vazio convertido em boolean é False, mais o all() entende como True

print(all([num for num in [4,2,10,6,8]if num % 2 == 0])) #mesmo se solicitar numero impar, vai validar como True


# Exemplo any()

print(any([0,1,2,3,4])) # True 

print(any([0, False,{},(), []])) # False 

nomes = ['Carlos', 'Camila','Carla','Cassiano','Cristina','Vanessa']

print(any([nome[0] == 'C' for nome in nomes])) # True

print(any([num for num in[4,2,10,6,8,9] if num % 2 == 0])) # True 


