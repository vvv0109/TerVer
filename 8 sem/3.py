#Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности,
#равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2.
#Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import math
from scipy.stats import norm

mean = 174.2
variance = 25
n = 27
alpha = 0.05

se = math.sqrt(variance) / math.sqrt(n)
z = norm.ppf(1 - alpha / 2)

lower = mean - z * se
upper = mean + z * se

print("Доверительный интервал: ({:.2f}, {:.2f})".format(lower, upper))