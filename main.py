import random

gracz_wygral = 0
komputer_wygral = 0
remis = 0

opcje = ["papier", "kamien", "nozyce"]
while True:
    urzytkownik_input = input("Wpisz: Papier/Kamien/Nozyce albo k zeby zakonczyc gre.\n").lower()
    if urzytkownik_input == "k":
        break
    if urzytkownik_input not in ["papier", "kamien", "nozyce"]:
        print("Wybierz jedna z opcji: Papier/Kamien/Nozyce  ")
        continue

    przypadkowy_numer = random.randint(0,2)
    komuter_gra = opcje[przypadkowy_numer]
    #kamien = 0, papier = 1, nozyce = 2
    print("Komputer wybral", komuter_gra + ".")

    if urzytkownik_input =="kamien" and komuter_gra == "nozyce":
        print("Wygrales")
        gracz_wygral += 1
    elif urzytkownik_input == "papier" and komuter_gra == "kamien":
        print("Wygrales")
        gracz_wygral += 1
    elif urzytkownik_input == "nozyce" and komuter_gra == "papier":
        print("Wygrales")
        gracz_wygral += 1

    elif urzytkownik_input == "nozyce" and komuter_gra == "nozyce":
        print("Remis")
        remis += 1
    elif urzytkownik_input == "papier" and komuter_gra == "papier":
        print("Remis")
        remis += 1
    elif urzytkownik_input == "kamien" and komuter_gra == "kamien":
        print("Remis")
        remis += 1
    else:
        print("Komputer wygral")
        komputer_wygral +=1

print("Komputer wygral", komputer_wygral,"razy. Remis byl", remis, "razy.")
print("Wygrales", gracz_wygral,"razy. Gratulacje!")
print("Do zobaczenia!")