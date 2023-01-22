""" 
Estruturas Logicas: and (e) , or (ou) , not (nao) e is (estar)

Operadores unários:
   - not
Operadores binarios:
   - and, or, is
   
Para o 'and', ambos os valores precisam ser true 
Para o 'or', um ou outro valor precisar ser true 
Para o 'not', o valor do booleano é invetido, se for True vira False, e se for False vira True
Para o 'is', o valor é comparado com o outro
"""

ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar a sua conta, valide o seu email')
    
#exemplo usando o not     
if not ativo:
    print('Você precisa ativar a sua conta, valide o seu email')
else:
    print('Bem-vindo usuário')
    
print(not True)
print(not False)

#Exemplo de is
if ativo is False:
    print('Você precisa ativar a sua conta, valide o seu email')
else:
    print('Bem-vindo usuário') 
    
    
 #Ativo é Falso?   
print(ativo is False)


#Outros exemplos do 'is
# nome.isupper()
# nome.islower()
# nome.istitle().istitle() 
