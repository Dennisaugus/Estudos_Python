""" 
Usando o continue no loop

A instrução continue dá a opção de ignorar a parte de um loop onde uma condição externa é acionada, 
mas continuar e completar o resto do loop. Ou seja, a iteração atual do loop será interrompida, 
mas o programa retornará ao topo do loop.

"""

# Exemplo do continue 
number = 0
for number in range(20):
    if number == 10:
        continue
    print(f'Number is {str(number)}')
print('Out of loop')

""" 
Resultado: 
Number is 0
Number is 1
Number is 2
Number is 3
Number is 4
Number is 5
Number is 6
Number is 7
Number is 8
Number is 9   
Number is 11 #Não executa a linha 10
Number is 12
Number is 13
Number is 14
Number is 15
Number is 16
Number is 17
Number is 18
Number is 19
Out of loop
"""