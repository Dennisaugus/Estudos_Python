"""
Decoradores (Decoretors)

Oque são decoretors ?

- Decoretors são funções;
- Decoretors envolvem outras funções e aprimoram seus comportamentos;
- Decoretors também são exemplos de Higher Order Functions;
- Decoretors tem uma sintaxe própria, usando o @ Syntact Sugar / Açucar Sintetico

/-----------------------------------/
/      Function Decorators         /
/---------------------------------/


/----------------------------------/
/                                  /
/        Função Decorada           /
/                                  /
/----------------------------------/

"""

# Decoradores como funções (Sintaxe não recomendada / Sem Açucar Sintatico)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer um conhecer você')
        funcao()
        print('Tenha um otimo dia ')
    return sendo

def saudacao():
    print('Seja bem vindo ao meu mundo')

# testando 

teste = seja_educado(saudacao)

teste()

# Testando 2 
def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com Syntax Sugar (Áçucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('foi um prazer em conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

# Exemplo 2
@seja_educado_mesmo
def dormir():
    print('quero dormir')

dormir()



""" 
Exemplo mais complexo do Decorators

|----------------------------------------------------|
|  HOME    | Serviços  | Produtos   | Administrativo |
|----------------------------------------------------|


http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

# OBS: Não é código funcional (Que funcione) é apenas um exemplo 

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')

        
def home(request):
    return 'Pode acessar Home'


def servicos(request):
    return 'Pode acessar Serviços'

    
def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin' 

"""

# OBS: não confunda Decorator com Decorator Function

