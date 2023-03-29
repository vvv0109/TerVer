#1) Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
#Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.
from scipy.stats import norm
import math
alpha = 0.05
z_star = norm.ppf(1 - alpha/2)
print("Значение z*:", z_star)
lower_bound = 80 - z_star * (16 / math.sqrt(256))
upper_bound = 80 + z_star * (16 / math.sqrt(256))

print("Доверительный интервал:", (lower_bound, upper_bound))