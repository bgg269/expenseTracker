# -*- coding: cp1252 -*-
# -*- coding: UTF8 -*-

import errorCheck

def main():
    muistio = 'muistio.txt'
    while True:
        uusiMuistio = errorCheck.virheCheck(muistio)
        print("\n(1) Lue\n(2) Lis�� merkint�\n(3) Muokkaa merkint��\n(4) Poista merkint�\n(5) Tallenna ja lopeta")
        answer = int(input("Mit� haluat tehd�?: "))
        if answer == 1:
            #Lue
            print('i')
        elif answer == 2:
            #Lis�� merkint�
            print('i')
        elif answer == 3:
            #muokkaa
            print('i')
        elif answer == 4:
            #poista
            print('i')
        elif answer == 5:
            #lopeta
            print('Lopetetaan.')
            break
        else:
            print("Valintaa ei tunnistettu.")
        
if __name__ == "__main__":
    main()
