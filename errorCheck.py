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

        
if __name__ == "__main__":
    main()
