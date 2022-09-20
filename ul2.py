# 2Naprogramuj funkciu, ktorá zistí, či dané číslo x patrí do intervalu <a,b>.
x = int(input("Zadaj začiatok intervalu: "))
y = int(input("Zadaj koniec intervalu: "))
z = int(input("Zadaj číslo a zisti či patrí do intervalu: "))
if x < z and z < y:
    print("Číslo", z,"patrí do intervalu")
else:
    print("Číslo", z,"nepatrí do intervalu")