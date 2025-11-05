class Pessoa:
    
    # O metodo especial '__init__' cria os atributos de instancia, objetos, ou
    # dados (features, campos).
    # Os atributos de uma instancia, assim como as listas, podem receber quaisquer
    # objetos python.
    def __init__(self, *filhos, nome = None, idade = 44):

        # Podemos garantir a existencia do campo sem ter valor para ele atribuindo
        # o valor None:
        self.nome = None
        self.idade = idade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    # No momento da construcao da classe, a funcao __init__ eh passada. Logo,
    # eh possivel atribuir valores aos atributos de dados nesse momento.
    p = Pessoa('Carlos Augusto')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    # Podemos usar atributos complexos. Por exemplo, uma instancia:
    renzo = Pessoa(nome = 'Renzo') # Renzo, aqui, eh uma instancia
    luciano = Pessoa('Renzo', nome = 'Luciano', idade = 40) # Renzo, aqui, é um atributo

    # Eh possivel acessar os atributos criados atraves do proprio objeto:
    print(p.nome)
    print(p.idade)


    # Atributos dinamicos sao atributos passados sem ue antes tenham sido criados. Esse tipo de operacao
    # afeta apenas o objeto a que diz respeito, e nao cria o mesmo atributo para nenhuma dos
    # demais participantes da classe.

    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)

    # Para conferir todos os atributos de instancia, tanto os comuns (criados com __init__)
    # quanto os dinâmincos, existe o atributo especial '__dict__'.

    print(luciano.__dict__)

    # Podemos também excluir dinamicamente qualquer dos tipos de atributo.
    # Para isso, usamos a palavra reservada 'del'.

    del luciano.filhos



