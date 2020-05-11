# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-


import time
import readFiles
import errorCheck

def main():
    muistio = input("Minkä nimistä tiedostoa käytetään? ")
    while True:
        newMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta")
        answer = input("\nMitä haluat tehdä?: ")
        if answer == '1':
            #Lue
            text = readFiles.findDate(newMuistio)
            for i in text:
                print(i)
        elif answer == '2':
            #Lisää merkintä
            file = open(newMuistio,"a")
            text = input("Kirjoita uusi merkintä: ")
            timeText = text + " ::: " + time.strftime("%x") + "\n"
            file.write(timeText)
            file.close()
        elif answer == '3':
            #muokkaa
            list = readFiles.readFile(newMuistio)
            print("Listalla on", len(list), "merkintää.")
            luku = int(input("Mitä niistä muutetaan?: ")) - 1
            print(list[luku])
            text = input("Anna uusi teksti: ")
            list[luku] = text + " ::: " + time.strftime("%x")+ "\n"
            readFiles.listToFile(list, newMuistio)
        elif answer == '4':
            #poista
            list = readFiles.readFile(newMuistio)
            text = errorCheck.wrongInput(list)
            print("Poistettiin merkintä", list[text-1])
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
