# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

# import array

import random
from unittest import result


numbers = [random.randint(1, 9) for i in range(15)]
print(numbers)

num = input("Введите трехзначное натуральное число: ")

# num = input("Введите трехзначное натуральное число: ")
# numbers = array.array('i',[1,2,3,4,5,6,7,8,9,0,9,8,7,6,5])
# print(numbers)
count = 0

num = list(num)
for i in range(len(numbers) - 2):
    if numbers[i] == int(num[0]) and numbers[i+1] == int(num[1]) and numbers[i+2] == int(num[2]):
        print('Да')
        count = 0
        break
    else:
        count = 1

if count == 1:
    print('Нет')
