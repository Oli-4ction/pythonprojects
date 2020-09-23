eingabe = 1
summe = 0
anzahl_eingaben = 0

minimum = float("inf")
maximum = float("-inf")

while eingabe != 0:
    eingabe = int(input("Bitte geben Sie die " +str(anzahl_eingaben + 1) + " . Zahl ein: "))
    if eingabe != 0:
        if eingabe < minimum:
            minimum = eingabe
        if eingabe > maximum:
            maximum = eingabe
        anzahl_eingaben = anzahl_eingaben + 1
        summe = summe + eingabe

if anzahl_eingaben != 0:
    mittelwert = summe / anzahl_eingaben
    print("Sie haben", anzahl_eingaben, "Werte eingegeben.")
    print("Die Summe der Werte ist:", summe)
    print("Das Minimum ist:", minimum)
    print("Das Maximum ist:", maximum)
    print("Der Mittelwert ist:", mittelwert)
