class Player:

    def __init__(self, nome, punteggio):
        self.nome = nome
        self.punteggio = int(punteggio)

    def __repr__(self):
        return f"{self.nome} {self.punteggio}"

    def __str__(self):
        return f"{self.nome} {self.punteggio}"