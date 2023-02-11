"""
Escopo de variáveis

/       ------escopo do espaço--------           /

Dois casos de Escopo

1 - Variáveis Globais:
      - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais
      - Variáveis locais são reconnhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
        está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos
o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""
#Exemplo de variável global
numero = 42 
print(numero)
print(type(numero))
#processo de atribuição
numero = 'Dennis'
print(numero)
print(type(numero))

nao_existe = 'oi'
print(nao_existe)


numero = 42
# novo = 0
if numero > 10:
    novo = numero + 10 # A variável novo esta declarada localmente dentro do bloco do if. Portanto, é local.
    print(novo)

print(novo)