class Pessoa:
    
    # ATRIBUTO DE CLASSE
    # Quando um atributo pode ser considerado padronizado para todas as instancias
    # de uma classe, como a quantidade de 'orelhas' para pessoas, por exemplo, eh boa
    # pratica para gestao de memoria criar um atributo de classe:

    orelhas = 2

    # Quando chamamos um atributo, o python procura primeiro o atributo de instancia.
    # Em sua ausencia, buscara o atributo de classe.


    # ATRIBUTO DE INSTANCIA
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

    # Existem os metodos de Classe que sao inseridos com o 'decorator' arroba (@),
    # Esses metodos, em suas instrucoes, devem ser independentes da classe e do objeto.
    # Esses metodos podem ser chamados tanto pela classe quanto pelo objeto.

    @staticmethod
    def metodo_estatico():
        return 42
    
    # Com o decorator @classmethod temos acesso ao noe e aos atributos de classe.

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - orelhas {cls.orelhas}'
    


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

    # Para consultar todos os atributos de instancia, tanto os comuns (criados com __init__)
    # quanto os dinâmincos, existe o atributo especial '__dict__'.

    print(luciano.__dict__)

    # Podemos também excluir dinamicamente qualquer dos tipos de atributo.
    # Para isso, usamos a palavra reservada 'del'.

    del luciano.filhos

    # Podemos alterar o atributo de classe para cada instancia, sem que isso afete
    # o valor para as demais instancias:

    luciano.orelhas = 3

    print(luciano.orelhas)

    del luciano.orelhas

    # Quando recriado dinamicamente, o atributo de classe se torna atributo de instancia

    luciano.orelhas = 3

    luciano.__dict__

    # Aqui, chamamos o metodo de classe metodo_estatico():
    print(Pessoa.metodo_estatico())
    print(luciano.metodo_estatico())

    # Aqui, chamamos o metodo de classe nome_e_atributos_de_classe():
    print(Pessoa.nome_e_atributos_de_classe())
    print(luciano.nome_e_atributos_de_classe())