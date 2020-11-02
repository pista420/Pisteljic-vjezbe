import math
def main():
    #unesi vrijednost cijele ploce
    cp =eval(input("Unesite cijenu pice: "))
    #unesi vrijednost za r
    r =eval(input("Unesite r: "))
    #izracunati povrsinu pice
    a = 4 * math.pi * r ** 2
    #izracunaj cijenu centrimetra pice formula
    ccm = cp/a
    #ispis cijene kvadratnog centrimera cm pice
    print("Cijena kvadratnog centimetra = ", ccm)
main()