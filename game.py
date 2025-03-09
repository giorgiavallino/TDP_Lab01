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

    def massimo_livello(self):
        livello_massimo = 0
        for domanda in self.domande:
            if domanda.livello > livello_massimo:
                livello_massimo = domanda.livello
            else:
                livello_massimo = livello_massimo
        return livello_massimo

    def scelta_domanda(self, livello_corrente):
        domande_possibili = []
        for domanda in self.domande:
            if domanda.livello == livello_corrente:
                domande_possibili.append(domanda)
        self.domande = domande_possibili
        return self.domande

    def mescolamento_risposte(self):
        for domanda in self.domande:
            risposte_mescolate = sorted(domanda.risposte, key=lambda k: random.random())
            domanda.risposte = risposte_mescolate
        return self.domande

    def seleziona_domanda(self):
        domanda_selezionata = random.choices(self.domande, k=1)
        self.domande = domanda_selezionata
        return self.domande

    def stampa_domanda_selezionata(self):
        for domanda in self.domande:
            print(f"Livello {domanda.livello}) {domanda.domanda}")
            for i in range(0, len(domanda.risposte)):
                print( f"{i+1}. {domanda.risposte[i]}")

    def inserimento_input(self):
        stringa = input("Inserisci la risposta: ")
        if stringa == "1" or stringa == "2" or stringa == "3" or stringa == "4":
            risposta = int(stringa)
        else:
            risposta = "La risposta inserita non è valida!"
            print(risposta)
        return risposta

    def controllo_risposta(self, risposta):
        continuo = True
        if risposta != "La risposta inserita non è valida!":
            for domanda in self.domande:
                    risposta_lettere = domanda.risposte[risposta-1]
                    if risposta_lettere == domanda._risposta_corretta:
                        print("La risposta è corretta!")
                        continuo = True
                    else:
                        print(f"La risposta è sbagliata! La risposta corretta è: {domanda._risposta_corretta}")
                        continuo = False
        return continuo