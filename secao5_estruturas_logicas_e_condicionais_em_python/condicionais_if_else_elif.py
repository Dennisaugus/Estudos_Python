"""
Estruturas condicionais 
if (Se), else , elif (else if)
    
"""

"""
# Estruturas condicionais em C
if(idade < 18){
    printf("Menor de idade)
}else if(idade == 18){
    printf("Tem 18 anos)
}else{
    printf("Maior de idade)
}

"""

idade = 26

if idade < 18:
    print('menor de idade')
    print(f'{idade} anos')
elif idade == 18:
    print('tem 18 anos')
    print(f'{idade} anos')
elif idade == 26:
    print('tem 26 anos')
else:
    print('maior de idade')
    print(f'{idade} anos')
    