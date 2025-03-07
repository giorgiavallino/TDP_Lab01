class Domanda:

    def __init__(self, domanda, livello, risposta_corretta, risposte):
        self.domanda = domanda
        self.livello = int(livello)
        self._risposta_corretta = risposta_corretta
        self.risposte = risposte

    def __repr__(self):
        return f"{self.domanda}, {self.livello}, {self._risposta_corretta}, {self.risposte}"

    def __str__(self):
        return f"{self.domanda}, {self.livello}, {self._risposta_corretta}, {self.risposte}"