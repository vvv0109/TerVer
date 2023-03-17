from math import factorial
a=52 #карт всего
c=4 #карт достаём
b=int(a/c) # карт одной масти
f=(factorial(a)/(factorial(c)*(factorial(a-c))))
d=(factorial(b)/(factorial(c)*(factorial(b-c))))
P=d/f
print(f'Вероятность достать 4 карты крести равна {round(P*100,2)}%')
a=52-c #карт всего без тузов
d=(factorial(a)/(factorial(c)*(factorial(a-c))))
P=1-(d/f)
print(f'Вероятность достать хотя бы 1 туз {round(P*100,2)}%')