#Заявляется, что партия изготавливается со средним арифметическим
#2,5 см. Проверить данную гипотезу, если известно, что размеры изделий
# подчинены нормальному закону распределения. Объем выборки 10,
# уровень статистической значимости 5%
#2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
import numpy as np

#входные данные
x = 2.5
y = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
#вычисление необходимых статистик
mean_y = np.mean(y)
var_y = np.var(y)
std_y = np.sqrt(var_y)
n = len(y)
#вычисление статистики t-критерия
t_stat = (x - mean_y) / (std_y / np.sqrt(n))
#проверка гипотезы
crit_val = 2.8 # значение из таблицы
if crit_val > abs(t_stat):
 print("Значение H0 верно: партия получена со средним значением 2,5 см")
else:
 print("H1: партия не производится со средним размером 2,5 см")