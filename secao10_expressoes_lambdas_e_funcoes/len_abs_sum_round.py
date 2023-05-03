""" 
Len, Abs, Sum, Round

# Len:
len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
print('Dennis Augusto'.__len__()) # Toda função que começa com __ e termina com __ é chamado de Dunder (funções especiais)


# Abs
abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.


# Sum
sum() -> Recebe como parametro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial
#PBS: O valor inicial default = 0


# Round
round() -> Retorna um número arredondado para n digito de precisão após a casa decimal.
Se a precisa não for informada retorna o inteiro mais próximo da entrada 



"""
# Exemplos de len
print(len('Dennis Augusto'))
print(len([1,2,3,4,5]))
print(len({'a':1,'b':2,'c':3}))
print(len(range(0,10)))

# Exemplos abs
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
# não podemos usar o abs em string (apenas inteiro ou real)


# Exemplos Sum
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,6], 5))
print(sum([1,2,3,4,5], -5))

print(sum([3.145, 5.837]))
print(sum((1,2,3,4,5)))
print(sum({1,23,4,5,6}))
print(sum({'a':2,'b':3,'c':5}.values()))

# Exemplos Round
print(round(10.2))
print(round(12.5))
print(round(1.21212121, 2))
print(round(129.99999, 2))