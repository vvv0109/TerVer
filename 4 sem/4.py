#Рост взрослого населения города X имеет нормальное распределение.
#Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
import math
# Заданные параметры нормального распределения
mu = 174    # Среднее значение
sigma = 8   # Среднее квадратичное отклонение

# Функция для вычисления вероятности по z-оценке
def z_probability(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# a) Вероятность роста больше 182 см
z = (182 - mu) / sigma
p_a = 1 - z_probability(z)
print("a) Вероятность роста больше 182 см: {:.2%}".format(p_a))
# в) Вероятность роста больше 190 см
z = (190 - mu) / sigma
p_a = 1 - z_probability(z)
print("в) Вероятность роста больше 190 см: {:.2%}".format(p_a))
# Вероятность роста от 166 см до 190 см
z_lower = (166 - mu) / sigma
z_upper = (190 - mu) / sigma
p_b = z_probability(z_upper) - z_probability(z_lower)
print("г) Вероятность роста от 166 см до 190 см: {:.2%}".format(p_b))
# Вероятность роста от 158 см до 190 см
z_lower = (158 - mu) / sigma
z_upper = (190 - mu) / sigma
p_d = z_probability(z_upper) - z_probability(z_lower)
print("д) Вероятность роста от 166 см до 190 см: {:.2%}".format(p_b))
# е) Вероятность роста не выше 150 см или не ниже 190 см
z_lower = (150 - mu) / sigma
z_upper = (190 - mu) / sigma
p_e = z_probability(z_lower) + (1 - z_probability(z_upper))
print("е) Вероятность роста не выше 150 см или не ниже 190 см: {:.2%}".format(p_e))

# ё) Вероятность роста не выше 150 см или не ниже 198 см
z_lower = (150 - mu) / sigma
z_upper = (198 - mu) / sigma
p_yo = z_probability(z_lower) + (1 - z_probability(z_upper))
print("ё) Вероятность роста не выше 150 см или не ниже 198 см: {:.2%}".format(p_yo))

# ж) Вероятность роста ниже 166 см
z = (166 - mu) / sigma
p_zh = z_probability(z)
print("ж) Вероятность роста ниже 166 см: {:.2%}".format(p_zh))

# Отклонение роста человека, равного 190 см, от математического ожидания
mu_x = 178
sigma_x = math.sqrt(25)
z = (190 - mu_x) / sigma_x
print("Отклонение роста 190 см от математического ожидания: {:.2f} сигм".format(z))