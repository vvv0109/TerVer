from math import factorial
a=10 #всего комбинаций от 0 до 9
c=3 #комбинация из 3 кнопок
d=1 #кол-во попыток
f=(factorial(a)/(factorial(c)*(factorial(a-c))))
P=d/f
print(f'Вероятность открыть замок {round(P*100,2)}%')