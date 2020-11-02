def vjezba2():
    from math import sin, cos, sqrt
    q = (3 + 4) * 5
    print(q)
    n =eval(input("Unesite vrijednost:  "))
    m = n * (n-1)/2
    print(m)
    r =eval(input("r "))
    print(4 != r*r)
    a =eval(input("a"))
    p =eval(input("p"))
    t =sqrt(p*cos(a)*cos(a)+p*sin(a)*sin(a))
    print(t)
    y1 =eval(input("y1"))
    y2 =eval(input("y2"))
    x1 =eval(input("x1"))
    x2 =eval(input("x2"))
    z = (y2 - y1) / (x2 - x1)
    print(z)
vjezba2()
