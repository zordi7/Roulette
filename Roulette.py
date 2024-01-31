import random

Budget = float(input("Inserisci Budget: "))
Budget_iniziale = Budget

def Spazi(n):
    for i in range(n):
        print()

def Estrazione():
    esiti = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']
    risultato = random.choice(esiti)
    return risultato

def Fine_partita(Budget):
    Spazi(1)
    print("Partita finita")
    print("Riepilogo")
    Spazi(1)
    while True :
        if Budget > Budget_iniziale:
            gaudagno = Budget - Budget_iniziale
            print(f"Il tuo Budget è di {Budget}, hai guadagnato {gaudagno} €")
            break
        elif Budget_iniziale > Budget:
            perdita = Budget_iniziale - Budget
            print(f"Il tuo Budget è di {Budget}, hai perso {perdita} €")
            break
        else:   
            print(f"Il tuo Budget è di {Budget}, sei rimasto in pari") 
            break




def Puntata_gioco():
    print("Scegli su cosa puntare:")
    print("Digita un numero da 0 a 36 per il numero specifico,\n'p12' per la prima dozzina, 's12' per la seconda, 't12' per la terza,\n'p' per i numeri pari, 'd' per i dispari,\n'r' per i rossi, 'n' per i neri,\n'c1' per i numeri (1,4,7,10,13,16,19,22,25,28,31,34),\n'c2' per i numeri (2,5,8,11,14,17,20,23,26,29,32,35),\n'c3' per i numeri (3,6,9,12,15,18,21,24,27,30,33,36),\n'1-18' per i primi 18 numeri, '19-36' per i secondi 18 numeri")
    puntata = str(input())
    return puntata

def verifica_vincita():
    r = Estrazione()
    p = Puntata_gioco()
    Puntata = float(input("Inserisci la puntata: ")) 
    
    Budget -= Puntata
    vincita2 = Budget + Puntata * 2
    vincita3 = Budget + Puntata * 3
    vincita36 = Budget + Puntata * 36
    
    
    Spazi(1)

    if r == '0':
        if p == '0':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '1':
        
        if p == '1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '2':

        if p == '2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '3':

        if p == '3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '4':
        
        if p == '4':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '5':

        if p == '5':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '6':

        if p == '6':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '7':

        if p == '7':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '8':

        if p == '8':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
            Spazi(1)
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '9':

        if p == '9':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '10':

        if p == '10':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '11':

        if p == '11':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '12':

        if p == '12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 'p12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '13':

        if p == '13':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '14':

        if p == '14':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '15':

        if p == '15':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '16':

        if p == '16':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '17':

        if p == '17':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '18':

        if p == '18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '1-18':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '19':

        if p == '19':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '20':

        if p == '20':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget) 
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '21':

        if p == '21':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '22':

        if p == '22':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3        
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2         
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)       
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '23':

        if p == '23':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36        
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3          
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3          
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2          
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2          
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2          
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)         
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '24':

        if p == '24':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36      
        elif p == 's12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3        
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3       
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2         
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)          
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '25':

        if p == '25':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36      
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3          
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3         
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2          
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)     
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '26':

        if p == '26':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36         
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3         
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3        
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2         
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)      
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '27':

        if p == '27':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36        
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3          
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3       
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)       
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '28':

        if p == '28':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36     
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3          
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3         
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)       
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '29':

        if p == '29':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36       
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3    
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3        
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)        
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '30':

        if p == '30':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36      
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3       
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3          
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)        
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '31':

        if p == '31':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36      
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3       
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3     
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2     
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)    
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '32':

        if p == '32':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36    
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3      
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3       
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2     
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)      
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '33':

        if p == '33':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36        
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3      
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3        
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)      
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '34':

        if p == '34':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36     
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3  
        elif p == 'c1':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3         
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2        
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2     
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)       
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '35':

        if p == '35':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36 
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3         
        elif p == 'c2':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3       
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'd':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        elif p == 'n':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2       
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)      
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)
    elif r == '36':

        if p == '25':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita36)
            Budget = vincita36
        elif p == 't12':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3        
        elif p == 'c3':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita3)
            Budget = vincita3      
        elif p == '19-36':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        elif p == 'p':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2     
        elif p == 'r':
            print("Hai vinto!")
            print(f'Il tuo Budget è di ', vincita2)
            Budget = vincita2      
        else:
            print("Hai perso")
            print(f'Il tuo Budget è di ', Budget)        
        Spazi(1)
        nuova_partita = str(input("Vuoi giocare ancora:  [s/n]  "))
        if nuova_partita == 's':
            verifica_vincita()
        else:
            Fine_partita(Budget)


verifica_vincita()
