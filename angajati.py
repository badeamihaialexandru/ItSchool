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

#definesc o functie care adauga angajati in lista de angajati
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
    
#adaugare_angajat("angajati.json")

#definesc o functie care sterge un angajat pe baza numelui si prenumelui sau
#deschid fisierul json pentru a-l putea citi ,continutul lui il depozitez in variabnila angajati
#initializez o variabila 'gasit ca fiind falsa' apoi cat timp variabila are valoarea ~False~ cer utilizatorului
#sa dea numele angajatului pe care doreste sa-l lase fara slujba ,apoi caut printre angajati angajatul cu numele si 
#prenumele introduse si daca il gasesc variabila gasit va lua valoarea ~True~. In cazul in care nu a fost gasit angajatul
#se afiseaza un mesaj si se cere utilizatorului sa reintroduca datele cerute despre angajatul pe care vrea sa-l trimita la plimbare =]]
#in cazul in care a fost gasit angajatul acesta este sters din lista de angajati 
#deschid din nou fisierul pentru a putea scrie noua lista de angajati 

def stergere_angajat(file):
    with open(CALE_DIR+file,"r") as jsonfile:
        angajati = json.load(jsonfile)
        gasit = False
        while gasit == False:
            nume_complet =  input("Intoduceti numele si prenumele angajatului pe care doriti sa-l stergeti: ")
            for angajat in angajati:
                if (angajat["Nume"] in nume_complet) and (angajat["Prenume"] in nume_complet):
                    gasit = True
                    angajati.remove(angajat)
                    print("Angajatul a fost sters cu succes!")
            if(gasit== False):
                print("Angajatul nu se afla in lista!!!")
                time.sleep(2)
                os.system("cls")
    with open(CALE_DIR+file,"w") as jsonfile: 
        json.dump(angajati,jsonfile)
        
#stergere_angajat("angajati.json")