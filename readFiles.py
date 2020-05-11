# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-



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

def findDate(newMuistio):
    re = []
    print('A näyttää koko historian, B näyttää tietyn kuukauden')
    while True:
        txt = input("\nMitä haluat tehdä?: ")
        if txt.lower() == 'a':
            print('koko lista:\n')
            list = readFile(newMuistio)
            re = list
            break
        elif txt.lower() == 'b':
            answer = input("\nMonesko kuukausi? (vaatii 0:n eteen)")
            answer2 = input("Mikä vuosi? (esim. 2020 = 20)")
            file = open(newMuistio,"r")
            list = []
            for i in file:
                date = i.split('::: ')
                months = date[1].split('/')
                month = months[0]
                year = months[2].rstrip('\n')
                if month == answer and year == answer2:
                    list.append(i)
            file.close()
            re = list
            break
        else:
            print('Valintaa ei tunnistettu')
    if len(re) == 0:
        print('Listalla ei ole merkintöjä tälle ajalla')
    return re
