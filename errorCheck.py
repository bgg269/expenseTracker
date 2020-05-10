# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-

def virheCheck(muistio):
    try:
        f = open(muistio)
    except IOError:
        f = open(muistio,'a')
        print("Virhe tiedostossa, luodaan uusi tiedosto nimeltä", f.name)
        f.close()
        return muistio
    else:
        return muistio

def wrongInput(list):
    while True:
        print("Listalla on", len(list), "merkintää.")
        text = input("Mikä niistä poistetaan? 0 poistaa viimeisen: ")
        try:
            luku1 = int(text)
        except ValueError:
            print('Syötä luku')
        except IndexError:
            print("index out of range")
        else:
            return luku1
    
        
if __name__ == "__main__":
    main()
