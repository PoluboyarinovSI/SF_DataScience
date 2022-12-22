import sys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

print(sns.__version__)

while True:
    try:
        mean = input('Введите среднее для нормального распределения:')
        mean = float(mean)
        break
    except:
        print('Это не число')


while True:
    try:
        deviation = input('Введите стандартное отклонение для нормального распределения:')
        deviation = float(deviation)
        break
    except:
        print('Это не число')


distribution_n1 = np.random.normal(0,1,1000)            
distribution_n2 = np.random.normal(mean,deviation,1000)*2 

sns_plot  = sns.histplot(distribution_n1, kde=True, color="orange")
sns_plot  = sns.histplot(distribution_n2, kde=True, color="skyblue")
plt.savefig('./output/plot.png')

print('Файл успешно сохранен')