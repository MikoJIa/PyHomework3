# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

lst_1 = [int(i) for i in input('Введите числа списка через пробел - ').split()]
lst_2 = []
size_lst = len(lst_1)
for i in range(len(lst_1)):
    while i < size_lst and size_lst > len(lst_1)/2:
        size_lst -= 1
        res = lst_1[i] * lst_1[size_lst]
        lst_2.append(res)
        i += 1
print(lst_2)
    

# lst_1 = [2, 3, 4, 5, 6]
# lst_2 = [2, 3, 5, 6]
# summ_lst_1 = product_numbers = []
# summ_lst_2 = product_numbers = []
# for i in range(len(lst_1)):
#     a = lst_1[i]*lst_1[len(lst_1)-i-1]
#     summ_lst_1.append(a)
# print(summ_lst_1)
    
