# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-

import errorCheck
import time

def lueTiedosto(newMuistio):
    file = open(newMuistio,"r")
    list = []
    while True:
        try:
            read = file.read()
        except Exception:
            break
        else:
            list.append(read)
    file.close()
    return list

def main():
    muistio = input("Mink� nimist� tiedostoa k�ytet��n? ")
    while True:
        newMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n(4) Poista merkint�\n(5) Tallenna ja lopeta")
        answer = int(input("Mit� haluat tehd�?: "))
        if answer == 1:
            #Lue
            file = open(newMuistio,"r")
            read = file.read()
            file.close()
            print(read)
        elif answer == 2:
            #Lis�� merkint�
            file = open(newMuistio,"a")
            text = input("Kirjoita uusi merkint�: ")
            timeText = text + " ::: " + time.strftime("%x") + "\n"
            file.write(timeText)
            file.close()
        elif answer == 3:
            #muokkaa
            file = open(newMuistio,"r")
            list = []
            for i in file:
                list.append(i)
            file.close()
            print("Listalla on", len(list), "merkint��.")
            luku = int(input("Mit� niist� poistetaan?: ")) - 1
            print("Poistettiin merkint�", list[luku])
            list.pop(luku)
            file = open(newMuistio,"w")
            for i in list:
                file.write(i)
            file.close()
        elif answer == 4:
            #poista
            print('i')
        elif answer == 5:
            #lopeta
            print('Lopetetaan.')
            break
        else:
            print("Valintaa ei tunnistettu.")
        
if __name__ == "__main__":
    main()
