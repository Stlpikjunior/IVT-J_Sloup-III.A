# 8Zisti, či je súčet dvoch posledných cifier párny
x = int(input("Zadaj číslo: "))
print(x % 10 + x % 100 // 10)
if (x%10+x%100//10)%2 ==0:
    print("súčet posledmých dvoch cifier čísla",x,"je párny")
else:
    print("súčet posledmých dvoch cifier čísla",x,"je nepárny")
