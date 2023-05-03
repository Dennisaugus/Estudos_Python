def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total

#utilizando o dunder 

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7]
    print(soma_impares(lista))

    tupla = (1,2,3,4,5,6,7)
    print(soma_impares(tupla))
else:
    print('O módulo funções com parametro foi importado')