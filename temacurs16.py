import json

def citeste_angajati():
    try:
        with open('angajati.json', 'r') as file:
            angajati = json.load(file)
    except FileNotFoundError:
        angajati = []
    return angajati

def scrie_angajati(angajati):
    with open('angajati.json', 'w') as file:
        json.dump(angajati, file)

def adauga_angajat():
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    salariu = float(input("Salariu: "))

    angajat_nou = {"Nume": nume, "Prenume": prenume, "Salariu": salariu}

    angajati = citeste_angajati()
    angajati.append(angajat_nou)
    scrie_angajati(angajati)
    print("Angajat adăugat cu succes!")

def sterge_angajat():
    nume = input("Introduceți numele angajatului de șters: ")

    angajati = citeste_angajati()
    angajati_nou = [angajat for angajat in angajati if angajat["Nume"] != nume]
    
    if len(angajati) == len(angajati_nou):
        print(f"Angajatul cu numele {nume} nu a fost găsit.")
    else:
        scrie_angajati(angajati_nou)
        print(f"Angajatul cu numele {nume} a fost șters cu succes!")

def afiseaza_angajati():
    angajati = citeste_angajati()
    if not angajati:
        print("Nu există angajați.")
    else:
        for angajat in angajati:
            print(f"Nume: {angajat['Nume']}, Prenume: {angajat['Prenume']}, Salariu: {angajat['Salariu']}")

def meniu():
    while True:
        print("\n1. Adăugare angajat")
        print("2. Ștergere angajat")
        print("3. Afișare toți angajații")
        print("4. Ieșire")

        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            adauga_angajat()
        elif optiune == "2":
            sterge_angajat()
        elif optiune == "3":
            afiseaza_angajati()
        elif optiune == "4":
            break
        else:
            print("Opțiune invalidă. Reîncercați.")

if __name__ == "__main__":
    meniu()