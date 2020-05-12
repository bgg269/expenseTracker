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
      date = " ::: " + time.strftime("%x") + '\n'

      package = expense()
      package.name = name
      package.cost = cost
      package.date = date
      return package
    
def main():
    muistio = input("Mink� nimist� tiedostoa k�ytet��n? ")
    while True:
        newMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue tiedostosta\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n(4) Poista merkint�\n(5) Tallenna ja lopeta")
        answer = input("\nMit� haluat tehd�?: ")
        if answer == '1':
            #Lue
            print('A n�ytt�� koko historian \nB n�ytt�� tietyn kuukauden\nC n�ytt�� yhteenvedon')
            while True:
                txt = input("\nMit� haluat tehd�?: ")
                if txt.lower() == 'a' or txt.lower() == 'b' or txt.lower() == 'c':
                    list = readFiles.findDate(txt, newMuistio)
                    break
                else:
                    print('Virheellinen valinta')
            
            total= 0
            if txt == 'a' or txt == 'b':
                total = 0
                for i in list:
                    print(i)
                    nameCost = i.split('�')
                    costs = nameCost[0].split(': ')
                    amount = int(costs[1])
                    total = total + amount
            elif txt == 'c':
                print('\nKuukausien kulutukset:')
                num_dict = {}
                for t in list:
                    if t[0] in num_dict:
                        num_dict[t[0]] = num_dict[t[0]]+t[1]
                    else:
                        num_dict[t[0]] = t[1]
                for key,value in num_dict.items():
                    print(str(key)+'.', value, '�')
                    total = total + value
            
            print('Kulutus yhteens�:', total,'�')
        elif answer == '2':
            #Lis�� merkint�
            bought = []
            file = open(newMuistio,"a")
            num = int(input("Kuinka monta ostosta?:"))
            for i in range(0,num):
                text = addExpense()
                while True:
                    if text.cost.isnumeric():
                        bought.append(text)
                        file.write(bought[i].name+": "+bought[i].cost + '�' +bought[i].date)
                        break
                    else:
                        print('Virheellinen arvo')
                        text = addExpense()
            file.close()
        elif answer == '3':
            #muokkaa
            list = readFiles.readFile(newMuistio)
            print("Listalla on", len(list), "merkint��.\n")
            luku = int(input("Mit� niist� muutetaan?: ")) - 1            
            print(list[luku])
            date = list[luku].split('::: ')
            text = addExpense()
            while True:
                if text.cost.isnumeric():
                    list[luku] = text.name+": "+ text.cost + '� ::: ' + date[1]
                    break
                else:
                    print('Virheellinen arvo')
                    text = addExpense()
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
