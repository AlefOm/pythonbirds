class Pessoa:
    
    # Cria os atributos de dados (features, campos):
    def __init__(self, nome = None, idade = 44):

        # Podemos garantir a existencia do campo sem ter valor para ele atribuindo
        # o valor None:
        self.nome = None
    
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':

    # No momento da construcao da classe, a funcao __init__ eh passada. Logo,
    # eh possivel atribuir valores aos atributos de dados nesse momento.
    p = Pessoa('Carlos Augusto')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

    # Eh possivel acessar os atributos criados atraves do proprio objeto:
    print(p.nome)