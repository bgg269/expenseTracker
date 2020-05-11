# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-


import time
import readFiles
import errorCheck

def main():
    muistio = input("Mink� nimist� tiedostoa k�ytet��n? ")
    while True:
        newMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n(4) Poista merkint�\n(5) Tallenna ja lopeta")
        answer = input("\nMit� haluat tehd�?: ")
        if answer == '1':
            #Lue
            text = readFiles.findDate(newMuistio)
            for i in text:
                print(i)
        elif answer == '2':
            #Lis�� merkint�
            file = open(newMuistio,"a")
            text = input("Kirjoita uusi merkint�: ")
            timeText = text + " ::: " + time.strftime("%x") + "\n"
            file.write(timeText)
            file.close()
        elif answer == '3':
            #muokkaa
            list = readFiles.readFile(newMuistio)
            print("Listalla on", len(list), "merkint��.")
            luku = int(input("Mit� niist� muutetaan?: ")) - 1
            print(list[luku])
            text = input("Anna uusi teksti: ")
            list[luku] = text + " ::: " + time.strftime("%x")+ "\n"
            readFiles.listToFile(list, newMuistio)
        elif answer == '4':
            #poista
            list = readFiles.readFile(newMuistio)
            text = errorCheck.wrongInput(list)
            print("Poistettiin merkint�", list[text-1])
            list.pop(text-1)
            readFiles.listToFile(list, newMuistio)
        elif answer == '5':
            #lopeta
            print('Lopetetaan.')
            break
        else:
            print("Valintaa ei tunnistettu.")
        


        
if __name__ == "__main__":
    main()
