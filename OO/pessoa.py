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