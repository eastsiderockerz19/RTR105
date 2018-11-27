from math import exp

def mana_funkcija(x):
    k = 0
    a = (-1)**0*x**0/(1)
    S = a
    print("izdruka no liet.f. a0 = %6.2f SO = %6.2f"%(a, S))  
    while k < 1000:
        k = k + 1
        R = (-x)/k
        a = a * R
        S = S + a

        if k == 999:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
    print("izdruka no liet. f. a1000 = %6.2f S1000 = %6.2f"%(a, S))
    return S * (1-x)

print("Funkcija aprekinasana")
print("")


x = float(input("Lietotaj, ludzu ievadi argmentu (x): "))
#e = 2.712...
#y = (1-x) * e**x
y = (1-x) * exp(-x)


yy = mana_funkcija(x)
print("Mana funkcija:(%.2f) = %6.2f"%(x,yy))



print("                               1000  ")
print("                            ___________")
print("                            \\")
print("                             \\             k    k")
print("y = (1-x) * exp(-x)= (1-x)*    >         (-1) * x")
print("                              /          -----------")
print("                             /                k!")
print("                             ___________")
print("                               k = 0      ")
print("                              -x ")
print("rekurences reizinatajs :  ________ ")
print("                               k   ")

print("Mana funkcija:(%.2f) = %6.2f"%(x,y))
