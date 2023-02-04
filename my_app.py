def mostra_informacao(nome='Dennis',professor=True,curso='ADS'):
    if nome == 'Dennis' and curso == 'ADS' and professor:
        return f'Olá professor {nome}, essa é a turma de {curso}'
    elif nome == 'Dennis' and curso == 'Engenharia de Software' and professor == False:
        return f'Olá professor {nome}, essa é a turma de {curso} e o senhor não é professor dessa turma'
    return f'Opá professor {nome}, você não faz parte de nenhum curso'

print(mostra_informacao())
print(mostra_informacao(professor=False))
print(mostra_informacao('Engenharia de Software'))
print(mostra_informacao('Ozzy'))


def soma(num1, num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def mat(num1,num2, fun=soma):
    return fun(num1,num2)

print(mat(2,3))
print(mat(4, 5, subtracao))