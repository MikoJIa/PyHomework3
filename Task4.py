# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число - '))
fibb1 = fibb2 = 1
for i in range(2, n):
    fibb1,fibb2 = fibb2, fibb1 - fibb2
    print(fibb2, end=' ')