""" 
Declaração Pass

Quando uma condição externa é acionada, 
a instrução pass permite lidar com a condição sem que o loop seja impactado; 
todo o código continuará sendo lido a menos que um break ou outra instrução ocorra.

"""

# Exemplo 

number = 0 
for number in range(10):
   if number == 5:
       pass
   print(f'Number is {str(number)}')
print('Out of loop') 

""" Resultado:
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
Out of loop
"""