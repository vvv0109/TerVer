#Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
#zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
#ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
#Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
#Полученные значения должны быть равны.
#Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.
import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

zp_mean = np.mean(zp)
ks_mean = np.mean(ks)

print("Среднее значение зп: ", zp_mean)
print("Среднее значение ks: ", ks_mean)

covariance = np.mean((zp - zp_mean) * (ks - ks_mean))
print("Ковариация: ", covariance)
std_zp = np.std(zp)
std_ks = np.std(ks)

corr = covariance / (std_zp * std_ks)
print("Коэффициент корреляции Пирсона: ", corr)
# Ковариация с помощью numpy
covariance_np = np.cov(zp, ks, ddof=0)[0][1]
print("Ковариация (numpy): ", covariance_np)

# Ковариация с помощью pandas
import pandas as pd

df = pd.DataFrame({'zp': zp, 'ks': ks})
covariance_pd = df.cov().iloc[0,1]
print("Ковариация (pandas): ", covariance_pd)

# Коэффициент корреляции Пирсона с помощью numpy
corr_np = np.corrcoef(zp, ks)[0,1]
print("Коэффициент корреляции Пирсона (numpy): ", corr_np)

# Коэффициент корреляции Пирсона с помощью pandas
corr_pd = df.corr().iloc[0,1]
print("Коэффициент корреляции Пирсона (pandas): ", corr_pd)