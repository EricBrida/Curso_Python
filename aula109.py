# Funções Decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açucar Sintático)

def criar_funcao(func):
    
    def interna(*args, **kwargs):
        
        print('Vou te decorar')
        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        print(f'{arg} se tornou {resultado}')
        print('Decorada')

        return resultado

    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError(f'{param} deve ser uma String')

# invertida_checa_parametro = criar_funcao(inverte_string)
# invertida = invertida_checa_parametro('123')
invertida = inverte_string('123')
print(invertida)