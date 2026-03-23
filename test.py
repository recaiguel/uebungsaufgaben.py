# Hier können einzelne Aufgaben getestet werden


# Aufgabe 24:  Login-System

credential = {
    'username': 'gingerninja27',
    'password': 'srspsswrd'
}

count = 0
trys = 3
while count < 3:
    userInput = input("Benutzername: \n")
    pwInput = input("Passwort: \n")

    if userInput == credential['username' and 
    pwInput == credential['password']]:
        print("Anmeldung erfolgreich!\n")
        break
    else:
        count += 1
        print("Benutzername oder Passwort falsch. Versuche es bitte erneut.\n")

print("Zu oft falsch eingegeben. Zugang gesperrt!")
