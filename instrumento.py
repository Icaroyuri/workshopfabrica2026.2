class Instrumento:
    def __init__(self, nome, som, tipo):
        self.nome = nome
        self.som = som
        self.tipo = tipo

    def reproduzir_som(self):
        print(self.som)


class Violao(Instrumento):
    def __init__(self, som, cordas):
        super().__init__("Violão", som, "Harmónico/Melódico")
        self.cordas = cordas

    def exibir_cordas(self):
        print(self.cordas)


class Bateria(Instrumento):
    def __init__(self, som, tambores):
        super().__init__("Bateria", som, "Percussivo")
        self.tambores = tambores

    def exibir_tambores(self):
        print(self.tambores)

xilophone = Instrumento("Xilophone", "tin", "Melódico")
violao = Violao("Vrem", "E, C, D, G, B, E")
bateria = Bateria("BumBu Ta", "Caixa, Bumbo, Tons, Pratos")

xilophone.reproduzir_som()

violao.reproduzir_som()
violao.exibir_cordas()

bateria.reproduzir_som()
bateria.exibir_tambores()