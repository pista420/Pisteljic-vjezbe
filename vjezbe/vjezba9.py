def main():

    # cijena kafe je 105rsd/kg, dostava je 18rsd/kg+15rsd fiksni troskovi
    n = eval(input("Unesite koliko kg kafe je naruceno:"))
    u = n*105+n*18+15
    print("Ukupna cijena kucne narudzbe je:" ,u)

main()