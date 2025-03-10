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
    if continuo:
        livello_corrente = livello_corrente + 1

punteggio_finale = game.calcolo_punteggio(livello_corrente)
print(f"Hai totalizzato {punteggio_finale} punti!")

nome_giocatore = game.aggiunta_player()
game.creazione_player(nome_giocatore, punteggio_finale)

game.lettura_classifica()
game.ordina_giocatori()
game.riscrittura_classifica()