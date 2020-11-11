class Getraenkeautomat:
    def init(self):  #method1( function within class ) total 4 methods
        self.getraenk = [] #attribute1 ( for init ) //// getraenk alleine ist nur eine lokale Variable - 
                           # - und wäre nur in dieser Funktion bekannt. Deshalb muss "self"-
                           # - davorgesetzt werden

        self.anzahl_flaschen = [] #attribute2

        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        self.anzahl_flaschen.append(10) #index 0
        self.anzahl_flaschen.append(10) #index 1
        self.anzahl_flaschen.append(10) #index 2

        self.kuehlung = False #attribute3

    def getraenke_waehlen(self):  #method2
        print("Bitte wählen Sie ein Getraenk:")
        print("Es gibt folgende Auswahl:")
        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl, getraenk)
            anzeige_auswahl = anzeige_auswahl + 1

        auswahl = int(input("Geben Sie die gewünschte Nummer ein:"))

        if self.anzahl_flaschen[auswahl-1] != 0:
            auswahl = auswahl - 1
        else:
            print("Das gewaehlte Getränk ist leider nicht mehr vorhanden.")
            auswahl = 1

        return auswahl

    def getraenk_ausgeben(self, anzahl, getraenke_index):  #method3
        if anzahl <= self.anzahl_flaschen[getraenke_index]:
            print("Sie erhalten", anzahl, "Flasche(n)", self.getraenk[getraenke_index])
            self.anzahl_flaschen[getraenke_index] = self.anzahl_flaschen[getraenke_index] - anzahl
        else:
            print("Es sind nur noch", self.anzahl_flaschen[getraenke_index], "Flaschen",
            self.getraenk[getraenke_index], "vorhanden.")
            print("Sie erhalten den Rest.")
            self.anzahl_flaschen[getraenke_index] = 0

    def kuehlen(self, an_aus): #method4
        self.kuehlung = an_aus
        if self.kuehlung == True:
            print("Die Kühlung ist eingeschaltet.")
        else:
            print("Die Kühlung ist ausgeschaltet.")

automat = Getraenkeautomat()
automat.init()

auswahl = -1
while auswahl == -1:
    auswahl = automat.getraenke_waehlen()

automat.kuehlen(True)

anzahl = int(input("Wie viele Flaschen mochten Sie?"))
automat.getraenk_ausgeben(anzahl, auswahl)

automat.kuehlen(False)










