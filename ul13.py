# 13Naprogramuj funkciu, ktorá po zadaní troch hodnôt vypíše, či hodnoty sú stranami trojuholníka a ak áno, tak akého (pravouhlého, rovnoramenného, rovnostranného ap.
a = int(input("zadajte stranu a:"))
b = int(input("zadajte stranu b:"))
c = int(input("zadajte stranu c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Zadané strany patria rovnostrannému trojuholníku")
    elif a==b or b==c or c==a:
        print("Zadané strany patria rovnoramenného trojuholníku")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Zadané strany patria pravouhlému trojuholníku")
    else:
        print("Zadané strany patria trojuholníku")
else:
    print("Zadané strany nepatria trojuholníku")