# Teil 1: Grundlagen
# Aufgabe 1
""" print("Gib dein Namen ein.\n")

name = input()

print("Hallo " + name) """

""" # Aufgabe 2
print("Zahl 1:\n")
zahl1 = int(input())

print("Zahl 2:\n")
zahl2 = int(input())

print(zahl1 + zahl2) """

""" # Aufgabe 3
print("Gib eine Zahl ein.\n")
geradeOungerade = int(input())

print(f"geradeOungerade % 2 = {geradeOungerade % 2}")
      
if geradeOungerade % 2 == 0:
    print("gerade")
else:
    print("ungerade") """

""" # Aufgabe 4
print("Gib dein Alter ein\n")
age = int(input())

if age < 18:
    print("Minderjährig")
elif age >= 18:
    print("Volljährig") """


# Teil 2 - Bedingungen und Logik

""" # Aufgabe 5
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

""" # Aufgabe 7: Größte Zahl

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

""" # Aufgabe 8 Zahlen ausgeben
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


# Aufgabe 15

