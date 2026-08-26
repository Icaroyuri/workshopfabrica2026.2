class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar (self):
        return f"Sou {self.nome} e tenho {self.idade}"
        