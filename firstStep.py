# Бинарные операторы:
# Сложение: +
# Вычитание: -
# Умножение: *
# Деление: /(обычное), //(целочисленное), %(вычисление остатка)


# Унарные операторы: -(4), +(4)

# Тип данных фактически задаёт множество значений объектов

# Python - динамически типизированный язык

# x = 5
# y = 10
# print((y > (x * x)) or (y >= (2 * x)) and x < y)
#
# n = int(input())
# word = "программист"
#
# if (n % 2 == 0 or n % 3 == 0 or n % 4 == 0) and (n < 5 or n > 20) and n != 0:
#     if n % 10 == 1:
#         end = ""
#     else:
#         end = "а"
# elif n == 1:
#     end = ""
# else:
#     end = "ов"
#
# print(n, word + end)

# n = input()
# e = int(n[-1])
# word = "программист"
#
# if len(n) > 2:
#     ed = n[-2:]
#     if int(ed) == 11 or int(ed) == 0:
#         end = "ов"
#
# if n == "1" or (e == 1 and int(n) != 11):
#     end = ""
#
# elif e in [0, 5, 6, 7, 8, 9] or int(n[-2:]) in [12, 13] or int(n) in [12, 13] or int(n) == 11 or int(n) == 14:
#     end = "ов"
#
# else:
#     end = "а"
#
# print(n, word + end)



# ticket = input()
#
# count_left = 0
# count_right = 0
#
# for i in ticket[0:3]:
#     count_left += int(i)
#
# for i in ticket[3:6]:
#     count_right += int(i)
#
# if count_left == count_right:
#     print("Счастливый")
# else:
#     print("Обычный")


a = int(input())
b = int(input())
i = 1

while i <= (a * b) and i != 0:
    if i % a == 0 and i % b == 0:
        print(i)
        i = 0
    else:
        i += 1