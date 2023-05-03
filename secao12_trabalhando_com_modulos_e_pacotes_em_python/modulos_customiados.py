""" 
Módulos customizados

Como módulos python nada mais são do que arquivos Python, então TODOS os arquivos
que criamos neste curso são modulos python prontos para serem utilizados

"""
#Importando uma função específica do nosso módulo
from funcoes_com_parametro import soma_impares
print(soma_impares([1,2,3,4,5,6,7,8,9]))

#Importando todo o módulo (temos acessos a TODOS os elementos do módulo)
import funcoes_com_parametro as fcp
print(fcp.lista)

# Estamos acessando e imprimindo uma varaivel contida no módulo
print(fcp.tupla)
print(fcp.soma_impares(fcp.lista))