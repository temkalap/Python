# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = 5
lst = random.sample(range(100), k + 1)
lstx = ['{}x^{}'.format(lst[x], x) for x in range(0, k + 1)]
lstx.reverse()
sting = '+'.join(lstx) + '=0'

myfile = open("multipl1.txt", "w+")
myfile.write(sting)
myfile.close()
print(sting)
