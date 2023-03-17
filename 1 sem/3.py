from math import factorial
a=15 #всего деталий
c=3 #кол-во деталий
d=9 #окрашено
f=(factorial(a)/(factorial(c)*(factorial(a-c))))
d=(factorial(d)/(factorial(c)*(factorial(d-c))))
P=d/f
print(f'Вероятность извлеченные окрашеных деталий {round(P*100,2)}%')