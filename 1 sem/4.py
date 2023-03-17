from math import factorial
a=100 #всего билетов
c=2 #кол-во выигрышных
f=(factorial(c)/(factorial(c)*(factorial(c-c))))
d=(factorial(a)/(factorial(c)*(factorial(a-c))))
P=f/d
print(f'Вероятность извлеченные выигрышных билетов {round(P*100,2)}%')