# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-

import errorCheck
import time

def listToFile(list, newMuistio):
    file = open(newMuistio,"w")
    for i in list:
        file.write(i)
    file.close()

def readFile(newMuistio):
    file = open(newMuistio,"r")
    list = []
    for i in file:
        list.append(i)
    file.close()
    return list



def main():
    muistio = input("Mink� nimist� tiedostoa k�ytet��n? ")
    while True:
        newMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n(4) Poista merkint�\n(5) Tallenna ja lopeta")
        answer1 = input("\nMit� haluat tehd�?: ")
        if answer1.isnumeric() == True:
            answer = int(answer1)
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
                list = readFile(newMuistio)
                print("Listalla on", len(list), "merkint��.")
                luku = int(input("Mit� niist� muutetaan?: ")) - 1
                print(list[luku])
                text = input("Anna uusi teksti: ")
                list[luku] = text + " ::: " + time.strftime("%x")+ "\n"
                listToFile(list, newMuistio)
            elif answer == 4:
            #poista
                list = readFile(newMuistio)
                text = errorCheck.wrongInput(list)
                print("Poistettiin merkint�", list[text-1])
                list.pop(text-1)
                listToFile(list, newMuistio)
            elif answer == 5:
            #lopeta
                print('Lopetetaan.')
                break
            else:
                print("Valintaa ei tunnistettu.")
        else:
            print('Sy�t� luku')
        
        
if __name__ == "__main__":
    main()
