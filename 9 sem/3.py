import numpy as np

# Задаем данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# добавление столбца единиц к признакам
X = np.column_stack((np.ones(len(zp)), zp))
y = ks.reshape(len(ks), 1)  # приведение целевой переменной к нужному виду

alpha = 5e-05  # скорость обучения
iterations = 1000000  # количество итераций

# начальные коэффициенты
b = np.zeros((2, 1))

# градиентный спуск
for i in range(iterations):
    b = b - alpha * (2/len(X)) * X.T.dot(X.dot(b) - y)

print("Коэффициенты линейной регрессии с intercept:", b.flatten())
