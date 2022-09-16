from kniffel_spieler import Spieler
from kniffel_spiel import Kniffel

     #
     ###
##########  INFO: Dieses Spiel, nutzt die "strenge" Kniffelvariante = Gestrichenes kann nicht rückgängig gemacht werden (auch nicht Kniffel), jede Option ist nur einmal auszufüllen (auch Kniffel)
     ###
     #

###MAIN:
anzahl_spieler = int(input("Bitte gib die Anzahl an Spielern ein (zwischen 2 und 10): "))

spieler_array = []
for i in range(1, anzahl_spieler+1):
    name = input("Bitte gib den Spielernamen an: ")
    sp = Spieler(name)
    spieler_array.append(sp)
    
spiel = Kniffel(spieler_array)

#spielen bis alle felder der spielstände voll:
for i in range(0, 13): 
    for sp in spieler_array:
        spiel.wuerfeln(sp)

#spielstand anzeigen:
for sp in spieler_array:
    spiel.display_spielstand(sp)

spiel.gewinner_ermitteln(spieler_array)








