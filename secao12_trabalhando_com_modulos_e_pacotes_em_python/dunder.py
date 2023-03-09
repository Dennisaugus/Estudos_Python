""" 
Dunder Name e Dunder Main

Dunder -> 2 underline __

Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main(String[] args){

}

#Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá a variavel __name__ o valor __main__ indicando que este módulo é o 
módulo de execução principal

Main -> Signífica principal.
"""
from exemplo_funcoes_com_parametro import soma_impares

print(soma_impares([1,2,3,4,5,6]))

import primeiro
import segundo

