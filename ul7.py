# 7Naprogramuj funkciu, ktorá vypíše, či dané číslo je kladné, záporné alebo nula.
x = int(input("Zadaj číslo: "))
if x<0:
    print("Číslo",x,"je záporné")
elif x==0:
    print("Číslo je nula")
else:
    print("Číslo",x,"je kladné")