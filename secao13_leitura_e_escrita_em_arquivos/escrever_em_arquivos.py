""" 
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso teremos um TypeError

Só podemos passar strings dentro do write.


Abrindo um arquivo para escrita com o modo 'w' se o arquivo não existir, será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo 
o conteúdo no arquivo anterior é perdido.

"""

# Exemplo de escrita - modo 'w' 
 
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Escriver dados em arquivo é muito facil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Ultima linha')

# Forma não pythonica - Forma tradicional de escrita 

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.\n')

arquivo.close()


with open('dennis.txt','w') as arquivo:
    arquivo.write('dennis\n' * 1000)

# recebendo dados do usuário:

with open('frutas.txt', 'w') as arquivo:
    while True:
        frutas = input('Informe uma fruta ou digite sair:')
        if frutas != 'sair':
            arquivo.write(frutas + '\n')            
        else:
            break

