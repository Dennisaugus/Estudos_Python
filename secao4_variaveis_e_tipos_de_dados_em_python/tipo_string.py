"""
Tipo string

Em python um dade é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '2234', 'a', 'True'. '45.6'
- Estiver entre aspas duplas -> "uma string", "213", "b" , "False", "45.7"
- Estiver entre aspas simples triplas -> '''uma string''' , '''23''', '''a''', '''True'''
- Estiver entre aspas duplas triplas
"""

nome = 'Dennis'
print(nome)
print(type(nome))

nome1 = "Dennis"
print(nome1)
print(type(nome1))

nome2 = '''Dennis'''
print(nome2)
print(type(nome2))

nome3 = """Dennis"""
print(nome3)
print(type(nome3))

#Exemplos:
nome4 = "Gina's Bar"
print(nome4)

nome5 = 'Angelina \n Jolie' #pula uma linha
print(nome5)
# [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  11, 12, 13]
# ['D','e','n','n','i','s',' ','A','u','g','u','s','t','o']
nome6 = 'Dennis Augusto'
print(nome6.upper())
print(nome6.lower())
print(nome6.split()) #transforma em uma lista de string
print(nome6[0:4]) #exibe do 0 ao 4 #slice de string
print(nome6[5:13]) #Slice de string

# [    0,          1  ]
# ['Dennis', 'Augusto']
print(nome6.split()[0]) # pega a posição 0
print(nome6.split()[1]) # pega a posição 1
print(nome6[13], nome6[7])
print(nome6[::-1]) #começa do primeiro elemento, depois vá ao ultimo elemente e depois inverta
print(nome[::-1]) # Inversão da String Pythonico

print(nome6.replace(('D', 'E')))

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])