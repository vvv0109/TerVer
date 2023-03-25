import scipy.stats as st
import numpy as np

mother_height = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
daughter_height = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

alpha = 0.05
result = st.ttest_ind(mother_height, daughter_height)

if result.pvalue < alpha:
    print("Отвергаем нулевую гипотезу: есть статистически значимые различия в росте дочерей.")
else:
    print("Не удалось отвергнуть нулевую гипотезу: статистически значимых различий в росте дочерей нет.")
