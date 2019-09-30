# year = int(input('input year'))
# month = int(input('input month'))
# if month == 2:
#     if (year % 4 == 0) or (year % 400 == 0 and year % 100 == 0):
#         print('%syear%smonth have %s day' % (year, month, 29))
#     else:
#         print('%syear%smonth have %s day' % (year, month, 28))
# elif month in (1, 3, 5, 7, 8, 10, 12):
#     print('%syear%smonth have %s day' % (year, month, 31))
# elif month in (4, 6, 9, 11):
#     print('%syear%smonth have %s day' % (year, month, 30))
# else:
#     print('input error')

# def updown(num):
#     a = num // 100
#     b = (num // 10) % 10
#     c = num % 10
#     print(c, b, a)
#
#
# x = int(input('input number'))
# updown(x)
#
#
# x = int(input('input month'))
# if x in (3, 4):
#     print('spring')
# elif x in (5, 6, 7, 8):
#     print('summer')
# elif x in (9, 10):
#     print('autumn')
# elif x in (11, 12, 1, 2):
#     print('winter')
# else:
#     print('error')

# ch = int(input('input ch'))
# math = int(input('input math'))
# eng = int(input('input eng'))
# print(ch > 85 and eng > 85 and math > 85)
# print(ch > 85 or eng > 85 or math > 85)
# print((ch > 90 or eng > 90) and math >= 80)


# x = int(input("input first number"))
# y = int(input("input second number"))
# print("%s+%s=%s" % (x, y, x + y))
# print("%s-%s=%s" % (x, y, x - y))
# print("%s*%s=%s" % (x, y, x * y))
# print("%s/%s=%s" % (x, y, x / y))

# x = int(input("input first number"))
# y = int(input("input second number"))
# if x > y:
#     print(x)
# else:
#     print(y)

# x = input('input string')
# y = len(x)
# if y <= 56 and y >= 0:
#     print('short message')
# elif y <= 128 and y >= 57:
#     print('common message')
# elif y <= 192 and y >= 129:
#     print('long message')
# elif y <= 256 and y >= 193:
#     print('super long message')
# else:
#     print('too long')

# import random
#
# a = random.randint(0, 5)
# if a == 0:
#     print('进入战斗')
# elif a == 1:
#     print('捡到宝箱')
# elif a == 2:
#     print('捡到武器')
# elif a == 3:
#     print('捡到弹药')
# elif a == 4:
#     print('踩到陷阱')
# elif a == 5:
#     print('无事件')

# x = None
# while x != 'y':
#     print('这道题你会做了吗?')
#     x = input('is can do')

# x = int(input('input your age'))
# if x >= 18:
#     print('can see')
# elif x < 10:
#     print('can not see')
# elif x >= 10 and x < 18:
#     print('is to see')
#     y = input('input ')
#     if y == 'yes':
#         print('see')
#     elif y == 'no':
#         print('quit')
#

# x = int(input('收缩压'))
# y = int(input('舒张压'))
# if (x >= 90 and x <= 140) and (y >= 60 and y <= 90):
#     print('normal')
# else:
#     print('unormal')

# x = int(input('T shirt'))
# y = int(input('pants'))
#
# if x == 1:
#     x = 35
# elif x == 2:
#     x = 35 * 2 * 0.9
# elif x >= 3:
#     x = 35 * x * 0.8
# else:
#     print('error')
#
# if y == 1 or y == 2:
#     y = 120 * y
# elif y > 2:
#     y = 120 * y * 0.9
# else:
#     print('error')
#
# print('total prince %s' % (x + y))


# x = input('input usr name')
# y = input('input passwd')
# if x == 'admin' and y == '88888':
#     print('right')
# else:
#     if x != 'admin':
#         print(' user not exist')
#     elif x == 'admin' and y != '88888':
#         print('passwd error')
#

# z = 0
# while z < 3:
#     x = input('input usr name')
#     y = input('input passwd')
#     if x == 'admin' and y == '88888':
#         print('right')
#         break
#     else:
#         print('user name or passwd error')
#         z += 1
#         if z == 3:
#             print('can not go on')


# for i in range(1,10):
#     print(i)

# x = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         x += i
# print(x)

# x = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         x += i
# print(x)

# for i in range(1, 9):
#     if i % 2 == 1:
#         for j in range(1, i + 1):
#             print('*', end='')
#     print()

# for i in range(8, 1):
#     for j in range(1, i + 1):
#         print('*', end='')
#     print()
# x = 8
# while x > 0:
#     for i in range(1, x):
#         print('*', end='')
#     print()
#     x -= 1

# for i in range(1, 9):
#     if i % 2 == 1:
#         for j in range(1, i + 1):
#             print('*'.center(7), end='')
#         print()
# x = 6
# for i in range(1, 9):
#     if i % 2 == 1:
#         print(('*' * i).center(7))
# while x > 0:
#     if x % 2 == 1:
#         print(('*' * x).center(7))
#     x -= 1


# x = int(input('input head'))
# y = int(input('input foot'))
# z = 0
# for i in range(1, x + 1):
#     for j in range(1, i + 1):
#         if (i + j) == 35 and ((i * 2 + j * 4) == 94):
#             z = 1
#             print('chicken %s' % (i))
#             print('rabbit %s' % (j))
#             break
#     if z == 1:
#         break

# import random
#
# x = int(input('buy money'))
# while x > 50:
#     y = int(input('input your bets'))
#     z = input('input choose')
#     a = random.randint(1, 6)
#     print('result is ', a)
#     if 1 <= a <= 3 and z == 'xiao':
#         x += y
#         print('you left %s money', x)
#     elif 4 <= a <= 6 and z == 'da':
#         x += y
#         print('you left %s money' % x)
#     else:
#         x -= y
#         print('you left %s money' % x)
#     if x < 50:
#         print('not enough money  exit')
#     else:
#         cho = input('is keep going')
#         if cho == 'n':
#             print('you left %s money,bye' % x)
#             break

# x = 3
# while x:
#     if (x + 3) % 5 == 0 and (x - 3) % 6 == 0:
#         print(x)
#         break
#     else:
#         x += 1


# for i in range(400, 501):
#     if i % 2 == 1 and i % 5 == 3 and i % 9 == 1:
#         print(i)
#         break

# list1 = []
# for i in range(1, 10):
#     for j in range(0, 10):
#         if (i * 1000 + 360 + j) % 6 == 0:
#             list1.append(i * 1000 + 360 + j)
#
# print(list1)
# print("max:%s,min:%s" % (max(list1), min(list1)))

# for i in range(1000, 10000):
#     x = str(i)
#     y = int(x[::-1])
#     if i * (i // 1000) == y:
#         print(i)

# for i in range(100, 1000):
#     x = i % 10 + i // 100 + (i // 10) % 10
#     if i // 11 == x:
#         print(i)


# x = 1
# while x:
#     if x // 80 % 7 == 0 and x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1:
#         print(x)
#     x += 1

# x = 10
# # while x:
# #     y = 0
# #     for i in range(0, len(str(x))):
# #         y += int(str(x)[i])
# #     if (x - y) % 9 == 0:
# #         print(x)
# #     x += 1


# import math
#
# list1 = []
# for i in range(2, 101):
#     s = int(math.sqrt(i))
#     c = True
#     for j in range(2, s + 1):
#         if i % j == 0:
#             c = False
#             break
#     if c == True:
#         list1.append(i)
# print(list1)
# for k in range(0, len(list1) - 1):
#     if list1[k + 1] - list1[k] == 2:
#         print(list1[k + 1], list1[k])

# for i in range(2,3):
#     print(i)


# import math
#
#
# def isprime(number):
#     sq = int(math.sqrt(number))
#     for j in range(2, sq + 1):
#         if number % j == 0:
#             return False
#     return True
#
#
# def printnum(num):
#     for i in range(2, num + 1):
#         if isprime(i) is True:
#             print(i)
#
# printnum(100)

# for i in range(10000, 100000):
#     if (700000 + i) / (i * 10 + 7) == 5:
#         print(i)

# x = int(input("input first number"))
# y = int(input("input second number"))
# s = input('input method')
# if s == '+':
#     print('%s+%s=%s' % (x, y, x + y))
# elif s == '-':
#     print('%s-%s=%s' % (x, y, x - y))
# elif s == '*':
#     print('%s*%s=%s' % (x, y, x * y))
# elif s == '/':
#     print('%s/%s=%s' % (x, y, x / y))
# import math
#
# list1 = []
# list2 = []
# c = 0
#
#
# def ispow2(num):
#     sq = math.sqrt(num)
#     i = 1;
#     while i < sq + 1:
#         if i * i == num:
#             return True
#         i += 1
#
#
# for i in range(1, 101):
#     if ispow2(i):
#         list1.append(i)
#         # print(list1)
# print(list1)
# for i in range(0, len(list1)):
#     if list1[i] - 15 > 0 and (list1[i] - 15 in list1):
#         list2.append(list1[i])
#         # print(list1[i])
# print(list2)
# for i in range(0, len(list2)):
#     c += list2[i]
#
# print(c)
# x = 129 - c
# print(x)
# for i in range(16, x - 15):
#     for j in range(16, x - 15):
#         if i + j == x and ((i not in list1) and (i-15 in list1)):
#             print(i, j)

i='s'
if i in 'string':
    print(i)
