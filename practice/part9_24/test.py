# print('Hello Python！')

# location = input('input your location')
# print('welcome to %s' % location)
#
# x = int(input('input first int number'))
# y = int(input('input second int number'))
# z = int(input('input third int number'))
# c = int(input('input fourth int number'))
# print('product is %s' % (x * y * z * c))

# name = input('input your name')
# ch = float(input('input your ch score'))
# math = float(input('input your math score'))
# eng = float(input('input your eng score'))
# print('{},your total score is {},avg score is {:.0f}'.format(name, ch + math + eng, (ch + math + eng) / 3))

# x = float(input("input up"))
# y = float(input("input down"))
# z = float(input("input high"))
# print('area is ', ((x + y) * z / 2))

# x = int(input('input days'))
# print('{:.0f}week,{}day'.format((x / 7), (x % 7)))

# x = 10
# y = 20
# print(x, y)
# temp = x
# x = y
# y = temp
# print(x, y)

# x = 10
# y = 20
# print(x, y)
# x = x + y
# y = x - y
# x = x - y
# print(x, y)

# x = 10
# y = 20
# print(x, y)
# x = x ^ y
# y = x ^ y
# x = x ^ y
# print(x, y)
# x = 1
# y = 2
# if x > 2 and y < 1:
#     print('aa')
# else:
#     print('vv')
#
# def leapyear(year, month):
#     big = {1, 3, 5, 7, 8, 10, 12}
#     little = {4, 6, 9, 11}
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         if month in big:
#             print('31')
#         elif month in little:
#             print('30')
#         elif month == 2:
#             print('29')
#     else:
#         if month in big:
#             print('31')
#         elif month in little:
#             print('30')
#         elif month == 2:
#             print('28')
#
#
# x = int(input('input year'))
# y = int(input('input month'))
# leapyear(x, y)

# def updown(num):
#     a =int( num / 100)
#     b = int((num / 10) % 10)
#     c = b * 100 + a * 10 + num % 10
#     print(c)
#
# # x=678
# x = int(input('input number'))
# updown(x)

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={} ".format(j, i, j * i), end='')
    print()
