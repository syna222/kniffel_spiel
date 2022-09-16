import random as rd

class Kniffel:
    def __init__(self, spieler_array):
        self.spieler_array = spieler_array
        
    #private methode, nur aus __wuerfeln() erreichbar!: 
    def __checkfield(self, spieler, wertungs_option):
        for i in spieler.letzter_spielstand:
            #wenn wertungs_option auftaucht, nicht kniffel ist und schon belegt, wird False ausgegeben, ansonsten weitergemacht
            if i == wertungs_option and wertungs_option != "kniffel" and spieler.letzter_spielstand[i] != 0:    
                return False
            else:   
                pass
        return True
        
    #private methode, nur aus wuerfeln() erreichbar!: 
    def __auswerten(self, spieler, wertungs_option, wurf_array, streichen_bool):
        #elemente des wurf_array in ints konvertieren:
        wurf_array = list(map(int, wurf_array))
        summe = 0
        auswertung_funktioniert = True
        #kategorie zur wertungs_option finden:
        if wertungs_option == "1en":
            summe = int(wurf_array.count(1) * 1)
        elif wertungs_option == "2en":
            summe = int(wurf_array.count(2) * 2)
        elif wertungs_option == "3en":
            summe = int(wurf_array.count(3) * 3)
        elif wertungs_option == "4en":
            summe = int(wurf_array.count(4) * 4)
        elif wertungs_option == "5en":
            summe = int(wurf_array.count(5) * 5)
        elif wertungs_option == "6en":
            summe = int(wurf_array.count(6) * 6)
        ###
        elif wertungs_option == "dreier":
            #rausfinden, welche art von dreier:
            for i in range(1, 7):
                if wurf_array.count(i) == 3:
                    summe = i * 3
                    #zwei anderen zahlen aus wurf zum dreier addieren:
                    for j in wurf_array:
                        if j != i:
                            summe = summe + j   
        elif wertungs_option == "vierer":
            #rausfinden, welche art von vierer:
            for i in range(1, 7):
                if wurf_array.count(i) == 4:
                    summe = i * 4
                    #andere zahl aus wurf zum vierer addieren:
                    for j in wurf_array:
                        if j != i:
                            summe = summe + j  
        elif wertungs_option == "kleine":
            summe = 30
        elif wertungs_option == "große":
            summe = 40
        elif wertungs_option == "fullhouse":
            summe = 25
        elif wertungs_option == "kniffel":
            summe = 50
        elif wertungs_option == "chance":
            summe = sum(wurf_array)
        else:
            print("Fehler in der Wertung")
            auswertung_funktioniert = False
            
        ##falls streichen:
        if streichen_bool == True:
            spieler.letzter_spielstand[wertungs_option] = "X"
        else:
            #punktestand beim user updaten:
            spieler.letzter_spielstand[wertungs_option] = summe 
        #damit methode erneut ausgeführt wird, falls falsche wertung ausgegeben wird
        return auswertung_funktioniert
            
    def display_spielstand(self, spieler):
        print("Dein Spielstand, ", spieler.name, ":")
        for i in spieler.letzter_spielstand:
            print(i, spieler.letzter_spielstand[i])
        print("\n")
        
    #private methode, nur aus __check_behaltformat() erreichbar!:
    def __int_check(self, wurf_array, teil_string):
        try:
            int(teil_string)
        except Exception as message:
            print("Exception! Falsches Format, ist keine Integer!", message)
            return False
        if str(teil_string) in wurf_array:
            return True
        else:
            print("\nFehler, deine Angabe war nicht im Wurf enthalten!")
            return False
        
        
    #private methode, nur aus wuerfeln() erreichbar!:
    def __check_behaltformat(self, wurf_array, behalt_string):
        if behalt_string == "":
            return True
        #ansonsten commata zählen:
        comma_count = behalt_string.count(",")
        #fall 1: kein comma
        if comma_count  >= 0 and comma_count <= 4:
            #string mittels commas zerlegen und für einzelteile checken, ob int und aus wurf_array:
            behalt_liste = behalt_string.split(",")
            for string in behalt_liste:
                okay = self.__int_check(wurf_array, string) #hier?
                if okay == False:
                    #print("self.__int_check(wurf_array, string) returned an error")
                    return False
            return True
        #fall 2: zu viele commata
        else:
            return False
        
        
    def wuerfeln(self, spieler):
        print("\n\n\n", spieler.name.upper(), " würfelt:\n")
        self.display_spielstand(spieler)   
        wuerfel_anzahl = 5  #initially
        wurf_array = []
        #dreimal würfeln:
        for runde in range(0, 3):
            for i in range(0, wuerfel_anzahl):
                wuerfel = str(rd.randint(1, 6))
                wurf_array.append(wuerfel)
            wurf_array.sort()  #optional
            print("Wurf ", str(runde+1), ": ", wurf_array)
            #abbruchbedingung für 3.runde:
            if runde == 2:
                #user fragen, als was ergebnis gewertet werden soll:
                streichen_bool = False
                while True:
                    while True:
                        optionen = ["1en", "2en", "3en", "4en", "5en", "6en", "dreier", "vierer", "große", "kleine", "fullhouse", "kniffel", "chance", "streichen"]
                        wertungs_option = input("Gib an, in welcher Sparte das Ergebnis gewertet werden soll (1en/2en/3en/4en/5en/6en/dreier/vierer/große/kleine/fullhouse/kniffel/chance/streichen):")
                        if wertungs_option in optionen:
                            break
                    #im falle von kategorie streichen:
                    if wertungs_option == "streichen":
                        streichen_bool = True
                        wertungs_option = input("Gib an, welche Sparte gestrichen werden soll (1en/2en/3en/4en/5en/6en/dreier/vierer/große/kleine/fullhouse/kniffel):")
                    print(wertungs_option)
                    #CHECKEN, ob wertungs_option schon belegt im spielstand des spielers:
                    if self.__checkfield(spieler, wertungs_option) == False:
                        print("Wertungsoption ungültig, gib eine andere Kategorie an!")
                        pass
                    else:
                        break
                #ÜBERGABE VON wertungs_option UND wurf_array:...
                #bei auswerten bool zurückgeben, ob erfolgreich, sonst kein break!!
                auswertung_erfolgreich = self.__auswerten(spieler, wertungs_option, wurf_array, streichen_bool)
                if auswertung_erfolgreich:
                    break
            #solange eingabe (was behalten werden soll für nächsten wurf) falsch ist, solange wird eingabe wiederholt:
            while True:
                #user gibt an, welche zahlen aus wurf er für nächsten wurf behalten will:
                behalt_string = input("Gib an, welche Zahlen für den nächsten Wurf behalten werden sollen (falls mehrere, mit Komma bitte):")
                #CHECKEN, ob behalt_string richtig ist (nur zahlen aus vorherigem wurf oder ""), wenn richtig, geht's weiter nach schleife:
                if self.__check_behaltformat(wurf_array, behalt_string) == True:
                    break                                            #PROBLEM! nach erst falscher, dann richtiger eingabe, geht es nicht mehr weiter...
                #zusätzlich, nur für test:
                else:
                    print("Deine falsche Eingabe war: ", behalt_string, "/der wurf_array: ", wurf_array, "\n")
            #falls keine zahl behalten werden soll:
            if behalt_string == "":
                behalt_array = []
            else:
                behalt_array = behalt_string.split(",")
            #anzahl der zu behaltenden würfel gibt an, wie viele zahlen neu zu würfeln sind:
            wuerfel_anzahl = 5 - len(behalt_array)
            wurf_array = []
            #zu behaltende zahlen an wurf_array anhängen:
            for i in behalt_array:
                wurf_array.append(i)

    def gewinner_ermitteln(self, spieler_array):
        for spieler in spieler_array:
            #gestrichene kategorien durch 0 ersetzen:
            for i in spieler.letzter_spielstand:
                if spieler.letzter_spielstand[i] == "X":
                    spieler.letzter_spielstand[i] = 0
            #oberteil ermitteln:
            obersumme = 0
            ober_keys = ["1en", "2en", "3en", "4en", "5en", "6en"]
            for key in spieler.letzter_spielstand.keys():
                if key in ober_keys:
                    obersumme = obersumme + spieler.letzter_spielstand[key]
            #bonus ermitteln:
            if obersumme >= 63:
                obersumme = obersumme + 35
            #unterteil ermitteln
            untersumme = 0
            unter_keys = ["dreier", "vierer", "kleine", "große", "fullhouse", "kniffel", "chance"]
            for key in spieler.letzter_spielstand.keys():
                if key in unter_keys:
                    untersumme = untersumme + spieler.letzter_spielstand[key]
            #addieren:
            endsumme = obersumme + untersumme
            spieler.letzter_spielstand["gesamt"] = endsumme
            print(spieler.name, " hat die endsumme: ", endsumme)