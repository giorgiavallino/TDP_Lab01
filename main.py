from game import Game

livello_corrente = 0
punteggio = 0

game = Game()
game.lettura_domande()
game.definizione_domanda()

livello_massimo = game.massimo_livello()
continuo = True

while livello_corrente <= livello_massimo and continuo == True:
    game.lettura_domande()
    game.definizione_domanda()
    game.scelta_domanda(livello_corrente)
    game.mescolamento_risposte()
    game.seleziona_domanda()
    game.stampa_domanda_selezionata()
    risposta = game.inserimento_input()
    continuo = game.controllo_risposta(risposta)
    if continuo == True:
        livello_corrente = livello_corrente + 1
