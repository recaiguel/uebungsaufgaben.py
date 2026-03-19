# Aufgabe 1
""" print("Gib dein Namen ein.\n")

name = input()

print("Hallo " + name) """

# Aufgabe 2
""" print("Zahl 1:\n")
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
def taschenrechner():

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

taschenrechner()