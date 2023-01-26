"""
Módulo Collections - Counter (COntador)

Collection -> High-performance Container Datetypes

Counter -> Recbe um interável como parametro e cria um objeto do tipo Collections Counter que é parecido 
com um dicionário, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrências desse elemento.

"""

# Utilizando o Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
from collections import Counter
list = [11,1,1,1,2,34,4,555,555,67,8,8,5,3,1]
# Counter({1: 4, 555: 2, 8: 2, 11: 1, 2: 1, 34: 1, 4: 1, 67: 1, 5: 1, 3: 1})
# o Counter validar quantas ocorrências tem em cada elemento da lista (criando chave)

# Utilziando o counter
res = Counter(list)
print(type(res))
print(res)

# Exemplo 2

print(Counter('Dennis Augusto'))
# Para cada caractere ele cria uma chave com os seus valores a quantidade de ocorrências 
# (repetições que aquele caractere tem )
# Counter({'n': 2, 's': 2, 'u': 2, 'D': 1, 'e': 1, 'i': 1, ' ': 1, 'A': 1, 'g': 1, 't': 1, 'o': 1})

# Exemplo 3
texto = """
Database management via a command-line interface can be nerve-racking. To solve this issue, 
we can use a tool with an interface. The pgAdmin solves this problem. Moreover, Docker makes 
the entire process smoother. Also, you can use the test data I’ve provided to play around with 
PostgreSQL queries. I hope this will help you get started with PostgreSQL, pgAdmin, and Docker. 
Happy coding!
"""

palavras = texto.split()
res = Counter(palavras)
print(res)

# Encontrando as 3 palavras com mais ocorrências no texto
print(res.most_common(3))
