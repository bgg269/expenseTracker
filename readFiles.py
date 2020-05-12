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

def findDate(txt, newMuistio):
    re = []
    while True:
        if txt.lower() == 'a':
            print('Koko historia:\n')
            list = readFile(newMuistio)
            re = list
            break
        elif txt.lower() == 'b':
            answer = input("\nMikä kuukausi? (luku): ")
            print('Kuukauden menot:\n')
            file = open(newMuistio,"r")
            list = []
            for i in file:
                date = i.split('::: ')           
                months = date[1].split('/')
                month = months[0]
                if month.strip('0') == answer:
                    list.append(i)  
            file.close()
            re = list
            break
        elif txt.lower() == 'c':
            file = open(newMuistio,"r")
            list = []
            num = 1
            total = 0
            for i in file:
                nameCost = i.split('€')
                costs = nameCost[0].split(': ')
                amount = int(costs[1])
                date = i.split('::: ')           
                months = date[1].split('/')
                month = months[0]
                month1 = int(month.lstrip('0'))
                amount1 = 0
                for num in range(1,13):
                    if num == month1 :
                        list.append((num, amount, 'e'))
                    else:
                        num = num + 1
            file.close()
            re = list
            break
        
        txt = input("\nMitä haluat tehdä?: ")
        
    if len(re) == 0:
        print('Listalla ei ole merkintöjä tälle ajalla')
    return re

