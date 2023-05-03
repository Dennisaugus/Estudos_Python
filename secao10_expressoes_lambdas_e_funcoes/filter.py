""" 
Filter 

filter() -> Serve para filtrar dados de uma determinada coleção.

"""

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

# Biblioteca para trabalhar com dados estatisticos
import statistics 

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Media: {media}')
# OBS: assim como a função map(), a filter() recebe 2 parametros, sendo uma função e um iteravel 
# Aplicando o filter()

res = filter(lambda x: x > media, dados)
print(list(res))
print(type(res))
print(f'Novamente: {list(res)}')

res = filter(lambda x: x < media, dados)
print(type(res))
print(list(res))
print(f'Novamente: {list(res)}')

#OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da memória.

# Exemplo de dados faltantes
paises = ['', 'Argentina','','Brasil','Chile','','Colombia','','Equador','','','Venezuela']

print(paises)

res = filter(None, paises)
print(list(res))

#lambda
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))

# A diferença entre map() e filter() é:
# map() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do iterável.
# filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a função.


# Exemplo mais complexo 

usuarios = [
    {"username": "Dennis", "tweets": ["Eu adoro bolos", "Eu adoro Pizzas"]},
    {"username": "Carla",  "tweets": ["Eu não gosto de bolos", "Eu adoro Pizzas"]},
    {"username": "Maria",  "tweets": ["Eu adoro pizza", "EU adoro sorvete"]},
    {"username": "Jose",   "tweets": ["Eu adoro cana", "Eu adoro camarão"]},
    {"username": "Alfredo", "tweets": []},
    {"username": "Catarina", "tweets": []},
    {"username": "Carlos", "tweets": ["Eu amo pitu"]}
]

print(usuarios)
# Filtrar os usuários que estão inativo no tweeter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

#Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Como combinar filter() map()

nomes = ['Vanessa', 'Ana', 'Maria'] 

# Devemos criar uma lista contendo 'sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)




