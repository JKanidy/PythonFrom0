# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
#
# for i in range(c, d+1):
#     print('\t', i, end='\t')
#
# for j in range(a, b + 1):
#     print('\n', j)

#
# a = int(input())
# b = int(input())
#
# c = 0
# sum = 0
#
# for i in range(a, b+1):
#     if i % 3 == 0:
#         c += 1
#         sum += i
#
# print(sum / c)


# genom = input().lower()
# c = 0
#
# for s in genom:
#     if s == "c" or s == "g":
#         c += 1
#
# print((c / len(genom)) * 100)


# s = "abccba1"
#
# if s == s[::-1]:
#     print("yes")
# else:
#     print("no")

# s = input()
# c = 0
#
# for i in range(len(s)):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         c = 0
#
#     print(s[i],c, end ="")


# s = input()
# i = 0
# c = 1
#
# while i < len(s) - 1:
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         print(s[i], c, sep="", end="")
#         c = 1
#     i += 1


# s = input()
# i = 0
# c = 1
#
# if len(s) == 1:
#     print(s, c, sep="")
#
# while i < len(s) - 1:
#     if s[i] == s[i+1]:
#         c += 1
#         if (len(s) - 1) - i == 1:
#             print(s[i], c, sep="", end="")
#     else:
#         print(s[i], c, sep="", end="")
#         c = 1
#         if (len(s) - 1) - i == 1:
#             print(s[i+1], c, sep="", end="")
#     i += 1


# a = [int(i) for i in input().split()]
# new = [0] * len(a)
#
# for i in range(len(a)):
#     if len(a) == 1:
#         print(a[0])
#     elif i == 0:
#         new[0] = a[-1] + a[i + 1]
#     elif i == len(a) - 1:
#         new[-1] = a[-2] + a[0]
#     else:
#         new[i] = a[i+1] + a[i-1]
#
# if len(a) != 1:
#     for item in new:
#         print(item, end=' ')



# a = [int(i) for i in input().split()]
# c = 0
# new = []
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             c += 1
#             if a[i] not in new and c > 1:
#                 new.append(a[i])
#                 c = 0
#
#
# print(new)


# a = [int(i) for i in input().split()]
# new = []
#
# for i in range(len(a)):
#     if a[i] in a:
#         new.append(a[i])
# print(new)

#
# n, m = (int(i) for i in input().split())
# a = [[0 for j in range(m)]for i in range(n)]

# a = []
# inp =input()
# while inp != "end":
#     mas = [int(i) for i in inp.split()]
#     a.append(mas)
#     inp = input()
#
# n = len(a)
# m = len(a[0])
# print(f'Матрица размером {n} x {m}')
#
# a = []
# inp =input()
# while inp != "end":
#     mas = [int(i) for i in inp.split()]
#     a.append(mas)
#     inp = input()

# n = len(a)
# m = len(a[0])
# print(f'Матрица размером {n} x {m}')




# mas = [int(i) for i in input().split()]
# n = len(mas)
# res = [0 for j in range(n)]
# print(f'res: {res}')
#
# for i in range(n):
#     if i == 0:
#         res[i] = mas[i + 1] + mas[-1]
#     elif i == n - 1:
#         res[i] = mas[i - 1] + mas[0]
#     else:
#         res[i] = mas[i - 1] + mas[i + 1]
#
# print(res)
#

# --------------------------модуль основного решения-----------------------------------------------
# a = []
# inp =input()
# while inp != "end":
#     mas = [int(i) for i in inp.split()]
#     a.append(mas)
#     inp = input()
#
# n = len(a)
# m = len(a[0])
# res = [[0 for i in range(m)] for j in range(n)]
# print(f'res: {res}')
#
# for i in range(n):
#     for j in range(m):
#         res[i][j] = a[i-1][j] + a[i+1][j] + a[i][j-1] + a[i][j+1]
# -------------------------------------------------------------------------------------------
# a = []
# inp =input()
# while inp != "end":
#     mas = [int(i) for i in inp.split()]
#     a.append(mas)
#     inp = input()
#
# n = len(a)
# m = len(a[0])
# res = [[0 for i in range(m)] for j in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         res[i][j] = a[i-1][j] + a[i-m+1][j] + a[i][j-1] + a[i][j-m+1]
#
# for s in res:
#     for c in s:
#         print(c, end=' ')
#     print()

#выше решение
a = []
inp =input()
while inp != "end":
    mas = [int(i) for i in inp.split()]
    a.append(mas)
    inp = input()

n = len(a)
m = len(a[0])
res = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        res[i][j] = a[i-1][j] + a[i-n+1][j] + a[i][j-1] + a[i][j-m+1]

for s in res:
    for c in s:
        print(c, end=' ')
    print()
