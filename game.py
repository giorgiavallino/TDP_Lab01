from domanda import Domanda
import random

class Game:

    def __init__(self, domande = []):
        self.domande = domande

    def __repr__(self):
        return f""

    def __str__(self):
        return f""

    def lettura_domande(self):
        domande_lista = []
        with open("domande.txt", "r") as file:
            linee = file.readlines()
            for linea in linee:
                linea = linea.replace("\n", "")
                domande_lista.append(linea)
            self.domande = domande_lista
        return self.domande

    def definizione_domanda(self):
        info_domande = []
        for i in range(0, len(self.domande), 7):
            risposte = []
            testo_domanda = self.domande[i]
            livello = self.domande[i+1]
            risposta_corretta = self.domande[i+2]
            risposte.append(self.domande[i+2])
            risposte.append(self.domande[i+3])
            risposte.append(self.domande[i+4])
            risposte.append(self.domande[i+5])
            domanda = Domanda(testo_domanda, livello, risposta_corretta, risposte)
            info_domande.append(domanda)
        self.domande = info_domande
        return self.domande

    def scelta_domanda(self, livello_corrente):
        domande_possibili = []
        for domanda in self.domande:
            if domanda.livello == livello_corrente:
                domande_possibili.append(domanda)
        return domande_possibili

    def mescolamento_risposte(self):
        for domanda in self.domande:
            risposte_mescolate = sorted(domanda.risposte, key=lambda k: random.random())
            domanda.risposte = risposte_mescolate
        return self.domande

g = Game()
print(g.lettura_domande())
print(g.domande)
print(g.definizione_domanda())
print(g.scelta_domanda(0))
print(g.mescolamento_risposte())