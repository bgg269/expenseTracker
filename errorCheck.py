# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-

def virheCheck(muistio):
    try:
        f = open(muistio)
    except IOError:
        f = open(muistio,'a')
        print("Virhe tiedostossa, luodaan uusi tiedosto nimelt�", f.name)
        f.close()
        return muistio
    else:
        return muistio

def wrongInput(list):
    while True:
        print("Listalla on", len(list), "merkint��.")
        text = input("Mik� niist� poistetaan? ")
        try:
            luku1 = int(text)
        except ValueError:
            print('Sy�t� luku')
        except IndexError:
            print("luku ei listalla")
        else:
            return luku1

        
if __name__ == "__main__":
    main()
