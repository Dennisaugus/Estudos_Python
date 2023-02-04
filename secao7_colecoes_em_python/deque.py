""" 
Módulo collections - Deque 

Podemos dizer que o deque é uma lista de alta performance.

"""
# Import
from collections import deque

deq = deque('dennis')
print(deq) # deque(['d', 'e', 'n', 'n', 'i', 's'])

# Adicionando elementos no deque 

deq.append('y') # adiciona no final assim como na lista
print(deq) 

deq.appendleft('k') # Adiciona no começo da lsita do deque 
print(deq)

# Removendo elementos 
deq.pop() # Remove o ultimo elemento (y)
print(deq)

deq.popleft() # Remove o primeiro elemento (k)
print(deq)