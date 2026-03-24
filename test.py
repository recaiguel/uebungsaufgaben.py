# Hier können einzelne Aufgaben getestet werden

daten = ["Ben,25", "Anna,30", "Tom,20"]
alterStr = []
for person in daten:
    teile = person.split(",")

    alter = teile[1]
    alterStr.append(alter)

altersListe = [int(i) for i in alterStr]

durchschnitt = int(sum(altersListe) / len(altersListe))

print(durchschnitt)