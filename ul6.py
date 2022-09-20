# 6Naprogramuj funkciu, ktorá zistí, či je dané číslo párne.
x = int(input("Zadaj číslo: "))
if x%10%2 ==0:
    print("Číslo",x,"je párne")
else:
    print("Číslo",x,"je nepárne")