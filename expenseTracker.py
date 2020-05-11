# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-


import time
import readFiles
import errorCheck

class expense:
    name = ""
    cost = 0
    date = ""

def addExpense():
      name = input("Ostettu asia: ")
      cost = input("Hinta: ")
      date = " ::: " + time.strftime("%x") + "\n"

      package = expense()
      package.name = name
      package.cost = cost
      package.date = date
      return package
    
def main():
    muistio = input("Mink� nimist� tiedostoa k�ytet��n? ")
    while True:
        newMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n(4) Poista merkint�\n(5) Tallenna ja lopeta")
        answer = input("\nMit� haluat tehd�?: ")
        if answer == '1':
            #Lue
            list = readFiles.findDate(newMuistio)
            for i in list:
                print(i)
        elif answer == '2':
            #Lis�� merkint�
            bought = []
            file = open(newMuistio,"a")
            num = int(input("Kuinka monta ostosta?:"))
            for i in range(0,num):
                toimitus = addExpense()
                bought.append(toimitus)
                file.write(bought[i].name+": "+bought[i].cost +bought[i].date)
            file.close()
        elif answer == '3':
            #muokkaa
            list = readFiles.readFile(newMuistio)
            print("Listalla on", len(list), "merkint��.")
            luku = int(input("Mit� niist� muutetaan?: ")) - 1            
            print(list[luku])
            text = addExpense()
            list[luku] = text.name+": "+ text.cost + text.date
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
