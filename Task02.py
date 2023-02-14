# Задача 2

# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

import random
bushes = int(input('Введите количество кустов: '))
berries = list(random.randint(1, 20) for i in range(bushes))
max_berries = []
a = 0
total = 0
print(berries)

while(a < bushes):
    if (a == bushes - 1):
        total = berries[a] + berries[a - 1] + berries[0]
    else:
        total = berries[a] + berries[a - 1] + berries[a + 1]
        max_berries.append(total)
        max_berries.sort()
    a += 1

print(max_berries[-1])