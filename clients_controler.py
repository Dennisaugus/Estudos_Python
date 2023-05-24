def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('foi um prazer em conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentacao():
    print('Meu nome é Dennis')

apresentacao()