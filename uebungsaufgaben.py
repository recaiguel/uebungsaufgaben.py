# Teil 1: Grundlagen

# Aufgabe 1
""" print("Gib dein Namen ein.\n")

name = input()

print("Hallo " + name) """

# Aufgabe 2
""" 
print("Zahl 1:\n")
zahl1 = int(input())

print("Zahl 2:\n")
zahl2 = int(input())

print(zahl1 + zahl2) """

# Aufgabe 3
""" 
print("Gib eine Zahl ein.\n")
geradeOungerade = int(input())

print(f"geradeOungerade % 2 = {geradeOungerade % 2}")
      
if geradeOungerade % 2 == 0:
    print("gerade")
else:
    print("ungerade") """

# Aufgabe 4
""" 
print("Gib dein Alter ein\n")
age = int(input())

if age < 18:
    print("Minderjährig")
elif age >= 18:
    print("Volljährig") """


# Teil 2 - Bedingungen und Logik

# Aufgabe 5
""" 
print("Gib eine Punktzahl ein:\n")
punktzahl = int(input())

if punktzahl >= 90:
    print("Sehr Gut")
elif punktzahl >= 75:
    print("Gut")
elif punktzahl >= 50:
    print("Bestanden") """

# Aufgabe 6
""" def taschenrechner():

    try:
        zahl1 = float(input("Zahl 1:\n"))
    except ValueError:
        print("Fehler: Bitte eine gültige Zahl eingeben")
        return
    
    allowedOperator = ['+', '-', '*', '/', '%']
    operator = input("Operator: -, +, *, /, %\n")
        
    if operator not in allowedOperator:
        print("Invalid operator")
        return
    
    try:    
        zahl2 = float(input("Zahl 2:\n"))
    except ValueError:
        print("Fehler: Bitte eine gültige Zahl eingeben")
        return

    if operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "%":
        ergebnis = zahl1 % zahl2
    elif operator == "/":
        if zahl2 == 0:
            print("Division durch 0 nicht möglich!")
            return
        ergebnis = zahl1 / zahl2

    print(f"Ergebnis: {zahl1} {operator} {zahl2} = {ergebnis}")

taschenrechner() """


# Aufgabe 7: Größte Zahl
""" 

zahl1 = int(input("Gebe 3 Zahlen ein.\n"))
zahl2 = int(input())
zahl3 = int(input())

if zahl1 >= zahl2 and zahl1 >= zahl3:
    print(zahl1)
elif zahl2 >= zahl1 and zahl2 >= zahl3:
    print(zahl2)
elif zahl3 >= zahl1 and zahl3 >= zahl2:
    print(zahl3)
 """


# Teil 3: Schleifen

# Aufgabe 8 Zahlen ausgeben
""" 
numbers = 100

for i in range(numbers):
    print(i + 1)
 """

# Aufgabe 9: Summe berechnen

""" n = int(input("Type a number for a range:\n"))
x = 0

for i in range(n):
    x += (i + 1)

    print(x) """


# Aufgabe 10

""" x = int(input("Gib eine Zahl für das Einmaleins ein\n"))

print(x*x)
"""


# Aufgabe 11: Passwortabfrage

""" password = "p455w0rd"

userInput = input("Passwort:\n")

while userInput != password:
    userInput = input("Passwort:\n")
else:
    print("Password korrekt!") """


# Teil 4 - Strings & Listen

# Aufgabe 12: Zeichen zählen

""" textInput = input("Geben Sie einen Text ein:\n")

count = 0

for character in textInput:
    count += 1
print(count) """


# Aufgabe 13: Vokale zählen

""" textInput = input("Geben Sie einen Text ein:\n")

vokale = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
count = 0

for i in textInput:
    if i.lower() in vokale:
        count += 1
print(count) """
    

# Aufgabe 14: Liste auswerten

""" zahlen = [3, 7, 2, 9, 12]

x = 0

for i in zahlen:
    x += 1
    average = sum(zahlen) / x

print(f'Summe: {sum(zahlen)}')    
print(f'Durchschnitt: {average}') """


# Teil 5 Funktion

# Aufgabe 15: Größtes Element

""" zahlen = [4, 12, 7, 21, 9]

maxWert = zahlen[0]

for i in zahlen:
    
    if i > maxWert:
        maxWert = i 
print(maxWert)



for i in range(len(zahlen)):
    if zahlen[i]>maxWert:
        maxWert=zahlen[i]
print(maxWert)  """  


# Aufgabe 16: Quadrat- Funktion

""" def quadrat():
    
    x = int(input("Gib eine Zahl ein um das Quadrat dieser Zahl auszugeben.\n"))
    print(x * x)

quadrat() """


# Aufgabe 17: Gerade Zahl prüfen

""" def geradeZahl():

    #Userinput einer beliebigen Zahl
    try:
        x = int(input("Gib eie beliebege Zahl ein\n"))
    except ValueError:
        print("Fehler: Bitte eine gültige Zahl eingeben")
        return
          
        if x % 2 == 0:
            print("True")
        else:
            print("False")
            
geradeZahl() """


# Aufgabe 18: Taschenrechner als Funktion

""" def taschenrechner():

    try:
        Zahl1 = float(input("Erste Zahl\n"))
    except ValueError:
        print("Bitte gib eine gültige Zahl ein")
        return
    
    try:
        Zahl2 = float(input("Zweite Zahl\n"))
    except ValueError:
        print("Bitte gib eine gültige Zahl ein")
        return

    allowedOperator = ['+', '-', '*', '/', '%']

    operator = input()

    if operator not in allowedOperator:
        print("Ungültiger Operator")
        return
    
    if operator == '+':
        Ergebnis = Zahl1 + Zahl2
    elif operator == '-':
        Ergebnis = Zahl1 - Zahl2
    elif operator == '*':
        Ergebnis = Zahl1 * Zahl2
    elif operator == '/':
        Ergebnis = Zahl1 / Zahl2
        if Zahl2 == 0:
            print("Division durch Null nicht möglich!")
            return
    elif operator == '%':
        Ergebnis = Zahl1 % Zahl2
    
    print(f"Ergebnis: {Zahl1} {operator} {Zahl2} = {Ergebnis}")

taschenrechner() """


# Teil 6 - Anwendung
    
 # Aufgabe 19: Zahlenraten-Spiel

""" import random
def guessingGame():
    guess = 0
    randomNumber = random.randint(1, 100)

        
    while guess != randomNumber:
        
        try:
            guess = int(input("Gib eine beliebige Zahl zwischen 1 und 100 ein.\n"))
        except ValueError:
            print("Gib eine Gültige Zahl ein")
            return

        if guess <= 0 or guess > 100:
            continue

        elif guess != randomNumber:
            print("False")
            if randomNumber > guess:
                print("zu niedrig")
            elif randomNumber < guess:
                print("zu hoch")
        else:
            print("True")
guessingGame() """


# Aufgabe 20: Einkaufsliste

""" einkaufsliste = {}
ende = False

while ende is not True:

    item = input("Artikel (oder 'fertig): ")
    if item.lower() == "fertig":
        ende = True
    
    else:
        preis = float(input(f"Preis für {item}: "))
        einkaufsliste[item] = preis

# berechnung der Summe
total = 0

for einzelpreis in einkaufsliste.values():
    total += einzelpreis

print(f"Gesamtsumme: {total:.2f} Euro") """


# Aufgabe 21: Wort umdrehen

""" wort = input("Gib ein Wort ein:\n")

# Ausgabe der variable direkt umgedreht.
print(wort[::-1]) """


# Teil 7: Herausforderung

# Aufgabe 22: Primzahl prüfen

""" def primeCheck(n):

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Interaktive Part des Programms

try:
    eingabe = int(input("Gib eine Zahl die du prüfen möchtest:\n"))

    if primeCheck(eingabe):
        print(f"{eingabe} ist eine Primzahl!")
    else:
        print(f"{eingabe} ist keine Primzahl!")

except ValueError:
    print(f"Hoppla! {eingabe} ist keine gültige Ganzzahl!") """
    

# Aufgabe 23: Häufigste Zahl

# Hier können einzelne Aufgaben getestet werden


# Aufgabe 23: Häufigste Zahl
""" 
liste = [5,3,7,8,6,9,10,5,7,5,8,9,6,10,10,7,5,3]
haeufigkeiten = {}

for zahl in liste:
    if zahl in haeufigkeiten:
        haeufigkeiten[zahl] += 1
    else:
        haeufigkeiten[zahl] = 1

rekords = max(haeufigkeiten.values())

siegerliste = [zahl for zahl, anzahl in haeufigkeiten.items() if anzahl == rekords]
print(siegerliste)
 """


# Aufgabe 24: Login-System
""" 
def loginSystem():
    credential = {
        'username': 'gingerninja27',
        'password': 'srspsswrd'
    }

    count = 0
    trys = 3
    print(f"Versuche: {trys}")
    while count < 3:
        userInput = input("Benutzername: \n")
        pwInput = input("Passwort: \n")

        if userInput == credential['username'] and pwInput == credential['password']:
            print("Anmeldung erfolgreich!\n")
            break
        else:
            count += 1
            trys -= 1
            print(f"Versuche: {trys}")
            print("Benutzername oder Passwort falsch.\n")
        
        if count == 3:
            print("Zu oft falsch eingegeben. Zugang gesperrt!")

loginSystem()
 """
