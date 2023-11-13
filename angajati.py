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
            
afisare_angajati("angajati.json")