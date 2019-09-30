# 必做任务：
# 任务1：
# 模仿Hello world案例，写一个方法向控制台输出字符串"Hello Python！"。

import calendar
calendar.isleap()
print('Hello Python！')
#
# 任务2：
# 在你的方法中定义变量，用这些变量存储游戏中一个敌人应该有的一些属性（比如用户名，等级，经验值，血量，魔法值等），定义尽可能多的变量。
#
name = 'sada'
level = 18
exp = 2000.3
hp = 3000
mp = 500
sex = True

# 任务3：
# 提示用户输入籍贯，当用户输入籍贯后，向用户显示"欢迎您来到某某" ，某某是用户输入的籍贯地。
#
location = input('input your location')
print('welcome to %s' % location)
# 任务4：
# 编写一个控制台应用程序，要求用户输入4个int值，并显示他们的乘积。
x = int(input('input first int number'))
y = int(input('input second int number'))
z = int(input('input third int number'))
c = int(input('input fourth int number'))
print('product is %s' % (x * y * z * c))
#
# 任务5：
# 让用户分别输入姓名，语文，数学，英语 三门课的成绩，然后给用户显示：XX，你的总成绩为XX分，平均成绩为XX分。
#

name = input('input your name')
ch = float(input('input your ch score'))
math = float(input('input your math score'))
eng = float(input('input your eng score'))
print('{},your total score is {},avg score is {:.0}'.format(name, ch + math + eng, (ch + math + eng) / 3))
# 任务6：
# 编写一个程序，输入梯形的上底 下底 和高 ，计算出来梯形的面积并显示出来。
#     梯形的面积=（上底+下底）*高 /2
#
x = float(input("input up"))
y = float(input("input down"))
z = float(input("input high"))
print('area is ', ((x + y) * z / 2))
# 任务7：
# 编程实现计算指定的天数(如46天)是几周零几天。
# 由用户输入天数 
#
x = int(input('input days'))
print('{:.0f}week,{}day'.format((x / 7), (x % 7)))
# 任务8：
# 接受用户输入的两个整数，存储到两个变量里面，交换变量存储的值。
# 1.临时变量
# x = int(input('first'))
# y = int(input('second'))
x = 10
y = 20
print(x, y)
temp = x
x = y
y = temp
print(x, y)
# 2.求和法
x = 10
y = 20
print(x, y)
x = x + y
y = x - y
x = x - y
# 3.异或法 
x = 10
y = 20
print(x, y)
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)

#


# 可选任务：
# 任务9：
# 写一个方法，传递两个参数，分别代表年份和月份，计算这个月的天数（可选）。
# 注：闰年的 2 月有 29 天；能被 4 整除同时不能被 100 整除即为闰年；如果能被 400 整除的是闰年，除此两种条件，其他都是非闰年。
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

year = int(input('input year'))
month = int(input('input month'))
if month == 2:
    if (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0):
        print('%syear%smonth have %s day' % (year, month, 29))
    else:
        print('%syear%smonth have %s day' % (year, month, 28))
elif month in (1, 3, 5, 7, 8, 10, 12):
    print('%syear%smonth have %s day' % (year, month, 31))
elif month in (4, 6, 9, 11):
    print('%syear%smonth have %s day' % (year, month, 30))
else:
    print('input error')


# 任务10：
# 从键盘输入一个三位的正整数，把百分位十分位个位数字的相反顺序输出。
#
def updown(num):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    print(c, b, a)


x = int(input('input number'))
updown(x)

# 思考题:
# 如何为大小写混杂的字符串排序？
# 例如: CabD=>abCD; 
