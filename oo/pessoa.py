class Pessoa:
    def __init__(self, *filhos, nome=None, idade=45):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    cristiano = Pessoa(nome='Cristiano')
    luciano = Pessoa(cristiano, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Tito'
    del luciano.filhos
    print(luciano.__dict__)
    print(cristiano.__dict__)

