#A - apsolutna vriednost kvadratnog korijena koristeci funkciju sqrt, NJ - vrijednost kvadratnog
#                                                       korijena dobijena koristeci Njutnovu metodu
from math import sqrt

def main():
    x = eval(input("Unesite x:"))
    n = eval(input("Unesite broj pokusaja:"))
    NJ=x/2
    for i in range(1,n+1):
        NJ=(NJ+x/NJ)/2
        if(NJ==sqrt(x)):
            break

    print("Kvadratni korijen broja x pomocu funkcije sqrt iznosi:", sqrt(x),", a kvadratni korijen dobijen Njutnovom metodom iznosi:", NJ)
    print("Broj pokusaja: ",i)

main()