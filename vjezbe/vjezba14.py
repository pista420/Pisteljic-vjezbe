#d - duzina merdevina, h - visina merdevina
from math import sin

def main():

    h,a = eval(input("Unesite visinu koju treba dostici i ugao kojim se meri nagib u formatu h,a:"))
    d=h/sin(a)
    print("Duzina merdevina iznosi: ", d)

main()