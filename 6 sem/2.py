#В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные:
#6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
#Предполагая, что результаты измерений подчинены нормальному закону распределения
#вероятностей, оценить истинное значение величины X при помощи доверительного интервала,
#покрывающего это значение с доверительной вероятностью 0,95.
import math

data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
n = len(data)
mean = sum(data) / n
std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))
t_value = 2.262  # Для 9 степеней свободы и уровня значимости 0.05 (двухсторонний)

lower = mean - t_value * std_dev / math.sqrt(n)
upper = mean + t_value * std_dev / math.sqrt(n)

print(f"Доверительный интервал: [{lower}, {upper}]")