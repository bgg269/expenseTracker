# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-

def virheCheck(muistio):
    try:
        f = open(muistio)
    except IOError:
        print("Virhe tiedostossa, luodaan uusi muistio.txt")
        f = open(muistio,'a')
        f.close()
        return muistio
    else:
        return muistio

        
if __name__ == "__main__":
    main()
