import json,os,time

#definesc o functie care citeste fisierul de tip json si afiseaza detalii despre angajati!
#deschid fisierul si il numesc jsonfile , continutul lui il depozitez in variabnila angajati
#apoi cu un for iau fiecare angajat in parte si afisez detaliile sale
CALE_DIR = "temacurs16/"
def afisare_angajati(file):
    with open(CALE_DIR+file,"r") as jsonfile:
        angajati = json.load(jsonfile)
        for angajat in angajati:
            print(f'Angajat: {angajat["Nume"]}  {angajat["Prenume"]} || Salariu: {angajat["Salariu"]}')
            
#afisare_angajati("angajati.json")

#definec o functie care adauga angajati in lista de angajati
#pun utilizatorul aplicatiei sa introduca datele despre angajat apoi deschid fisierul json pentru a-l 
#putea citi ,continutul lui il depozitez in variabnila angajati,apoi intr-o variabila depozitez informatiile 
#despre noul angajat ,adaug noul datele noului angajat in lista de angajati si afisez un mesaj
#deschid din nou fisierul pentru a putea scrie noua lista de angajati 

def adaugare_angajat(file):
    nume =  input("Intoduceti numele angajatului: ")
    prenume = input("Intoduceti prenumele angajatului: ")
    salariu = input("Intoduceti salariul angajatului: ")
    with open(CALE_DIR+file,"r") as jsonfile:
        angajati = json.load(jsonfile)
        angajat_nou = {
            "Nume": nume,
            "Prenume":  prenume,
            "Salariu": salariu
        }
        angajati.append(angajat_nou)
        print(f'Avem un nou angajat: {angajat_nou["Nume"]} {angajat_nou["Prenume"]}')
    with open(CALE_DIR+file,"w") as jsonfile:
        json.dump(angajati,jsonfile)
    
        
adaugare_angajat("angajati.json")