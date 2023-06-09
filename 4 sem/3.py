#Непрерывная случайная величина X распределена нормально и задана плотностью распределения
#f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
#а). M(X) б). D(X) в). std(X) (среднее квадратичное отклонение)
import math

# параметры нормального распределения
mu = -2
sigma = math.sqrt(32)

# ожидаемое значение (M(X))
mean = mu

# дисперсия (D(X))
variance = sigma ** 2

# среднее квадратическое отклонение (std(X))
std_dev = sigma

print("M(X) = ", mean)
print("D(X) = ", variance)
print("std(X) = ", std_dev)
