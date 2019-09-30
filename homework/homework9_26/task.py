# 要求：
# 创建一个taskxx（xx为作业次数编号）的目录；
# 所有练习题使用一个模块；
# 模块形如：testXX
# #XX为作业次数编号
# 模块中请将题目以注释的方式放入：
# # 任务1：
# # 模仿Hello world案例，写一个方法向控制台输出字符串"Hello 大数据！"。
# print("Hello Python！")
#
# 必做任务：
# 任务1：
# 让用户输入小茗的语文和数学成绩，输出以下判断是否正确，正确输出True，错误输出False
# a、小茗的语文和数学成绩都大于90分；
# b、语文和数学有一门是大于90分的。
x = int(input("input ch score  "))
y = int(input("input math score"))
if (x > 90 and y > 90):
    print('小茗的语文和数学成绩都大于90分，True')
else:
    print('小茗的语文和数学成绩都大于90分，False')
if (x > 90 or y > 90):
    print('语文和数学有一门是大于90分的，True')
else:
    print('语文和数学有一门是大于90分的，False')
# print(x > 90 and y > 90)
# print(x > 90 or y > 90)
#
# 任务2：
# 要求用户输入两个数a、b，如果 a 被 b 整除或者a加b大于100，则输出a的值，否则输出 b 的值。
#
a = int(input("input first number"))
b = int(input("input second number"))
if b % a == 0 or a + b > 100:
    print('a')
else:
    print('b')

# 任务3：
# 让用户输入学员的成绩，然后输出学员的结业考试成绩评测结果。
# 成绩 >=90  ： A      
# 90> 成绩 >=80  ： B  
# 80> 成绩 >=70  ： C
# 70> 成绩 >=60  ： D
# 成绩 <60   ： E
#
y = int(input('input score'))
if y < 60:
    print('E')
elif y < 70 and y >= 60:
    print('D')
elif y < 80 and y >= 70:
    print('C')
elif y < 90 and y >= 80:
    print('B')
elif y >= 90:
    print('A')
else:
    print("input wrong")

# 任务4：
# 提示用户输入用户名，然后再提示输入密码，如果用户名是“admin”并且密码是“88888”，则提示正确，
# 否则，如果用户名不是admin还提示用户用户名不存在,如果用户名是admin则提示密码错误。
#
x = input('input usr name')
y = input('input passwd')
if x == 'admin' and y == '88888':
    print('right')
else:
    if x != 'admin':
        print(' user not exist')
    elif x == 'admin' and y != '88888':
        print('passwd error')

# 任务5：
# 提示用户输入用户名，然后再提示输入密码，如果用户名是“admin”并且密码是“88888”，则提示正确，
# 否则，提示用户“用户名或者密码错误”，但如果错误达到3次，则提示用户"您的账户已被冻结"，退出程序。


z = 0
while z < 3:
    x = input('input usr name')
    y = input('input passwd')
    if x == 'admin' and y == '88888':
        print('right')
        break
    else:
        print('user name or passwd error')
        z += 1
        if z == 3:
            print('can not go on')

#
# 任务6：
# 求1-100间的所有奇数和。
x = 0
for i in range(1, 101):
    if i % 2 == 1:
        x += i
print(x)

#
# 任务7：
# 求1-100间的所有能被3整除的数的和。
x = 0
for i in range(1, 101):
    if i % 3 == 0:
        x += i
print(x)

#
# 任务8：
# 编程实现如下图列出的图形。
# *
# ***
# *****
# *******
# for i in range(1, 9):
#     if i % 2 == 1:
#         for j in range(1, i + 1):
#             print('*', end='')
#     print()

for i in range(4):
    print('*' * (2 * (i + 1) - 1))

# 任务9：
# 让用户输入一个数显示下面内容。
# *******       
# ******        
# *****          
# ****           
# ***            
# **             
# *   
# x = 8
# while x > 0:
#     for i in range(1, x):
#         print('*', end='')
#     print()
#     x -= 1

for i in range(7):
    print('*' * (7 - i))
#    
# 任务10：
# 编程实现如下图列出的图形。
#
#    *              
#   ***        
#  *****    
# *******
#
# for i in range(1, 9):
#     if i % 2 == 1:
#         print(('*' * i).center(7))

for i in range(4):
    print(' ' * (3 - i), end='')
    print('*' * (2 * (i + 1) - 1))

# 任务11：
# 编程实现如下图列出的图形。
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# x = 6
# for i in range(1, 9):
#     if i % 2 == 1:
#         print(('*' * i).center(7))
# while x > 0:
#     if x % 2 == 1:
#         print(('*' * x).center(7))
#     x -= 1
for i in range(4):
    print(' ' * (3 - i), end='')
    print('*' * (2 * (i + 1) - 1))
for i in range(3):
    print(' ' * (i + 1), end='')
    print('*' * (2 * (3 - i) - 1))

# 1）在控制台上输出100~500之间的所有奇数，并计算它们的和。 
x = 0
for i in range(100, 501):
    if i % 2 == 1:
        x += i
print(x)

# （2）在控制台上输出100~200之间不能被3整除的所有数。
for i in range(100, 201):
    if i % 3 != 0:
        print(i)
# （3）统计1~1000之内既能被5整除，也能被7整除的数的个数。 
x = 0
for i in range(1, 1001):
    if i % 5 == 0 and i % 7 == 0:
        x += 1
print(x)

# （4）从300开始，找出连续100个既能被3整数又能被5整除的数。
x = 0
i = 300
while True:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        x += 1
        if x == 100:
            break
    i += 1

#
# （5）计算s = 1! + 2! + 3! + ...+ n! （其中n是用户输入的正整数）。
n = int(input('input num'))
c = 0
for i in range(n):
    x = 1
    for j in range(1, i + 2):
        x *= j
    print(x)
    c += x
print(c)
#
# （6）计算出不大于1000 的10个最大的素数。
x = 0
for i in range(1000, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        x += 1
        if x == 3:
            break
# 任务12：
#  鸡兔同笼，从上面看有35个头，从下面看有94只脚，请问鸡有几只，兔有几只？
x = int(input('input head'))
y = int(input('input foot'))
z = 0
for i in range(1, x + 1):
    for j in range(1, i + 1):
        if (i + j) == 35 and ((i * 2 + j * 4) == 94):
            z = 1
            print('chicken %s' % (i))
            print('rabbit %s' % (j))
            break
    if z == 1:
        break

#
# 任务13：
# 玩家进来以后要买筹码；
# 在每次掷骰子前，
#     要下注（50~手里剩余的筹码）;
#     接着要选择买大小；
#     程序要模仿掷骰子，产生一个1~6的随机数
#     根据掷骰子的结果，判断玩家的输赢，改变玩家的手里的筹码
#         如果买大，4~6是赢，1~3是输
#         如果小，1~3是赢，4~6是输
#         如果赢了，玩家的筹码+=下注金额
#         如果输了，玩家的筹码-=下注金额    
#     提示玩家是否要退出游戏
#     玩家手里的筹码小于最小下注金额，要强制玩家退出
# 注意 ：先理清楚思路，从宏观上考虑流程，不要考虑每个步骤的细节。流程搞清楚以后，再琢磨每个步骤的细节。然后写代码。
#
import random

x = int(input('buy money'))
while x > 50:
    y = int(input('input your bets'))
    z = input('input choose')
    a = random.randint(1, 6)
    print('result is ', a)
    if 1 <= a <= 3 and z == 'xiao':
        x += y
        print('you left %s money' % x)
    elif 4 <= a <= 6 and z == 'da':
        x += y
        print('you left %s money' % x)
    else:
        x -= y
        print('you left %s money' % x)
    if x < 50:
        print('not enough money  exit')
    else:
        cho = input('is keep going')
        if cho == 'n':
            print('you left %s money,bye' % x)
            break

# 可选任务：
# 1.一个自然数与3的和是5的倍数,与3的差是6的倍数,这个自然数最小是几?
x = 3
while x:
    if (x + 3) % 5 == 0 and (x - 3) % 6 == 0:
        print(x)
        break
    else:
        x += 1
#
# 2.在400--500之间求一个数,它被2除余1,被5除余3,被9除余1,这个数是多少?
#
for i in range(400, 501):
    if i % 2 == 1 and i % 5 == 3 and i % 9 == 1:
        print(i)
        break

# 3.有一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,又能被3整除,
# 求这样的四位数中最大的和最小的两数各是几?
#
list1 = []
for i in range(1, 10):
    for j in range(0, 10):
        if (i * 1000 + 360 + j) % 6 == 0:
            list1.append(i * 1000 + 360 + j)

print(list1)
print("max:%s,min:%s" % (max(list1), min(list1)))

# 4.编程求一个四位自然数ABCD,它乘以A后变成DCBA
for i in range(1000, 10000):
    x = str(i)
    y = int(x[::-1])
    if i * (i // 1000) == y:
        print(i)

#
# 5.编程求出满足以下条件的三位数:它除以11所得的商等于它各位数字之和.
#
for i in range(100, 1000):
    x = i % 10 + i // 100 + (i // 10) % 10
    if i // 11 == x:
        print(i)

# 6.某数被80除所得的商,不但是7的倍数,而且用2,3,4,5,6去除余数都是1,求这   个自然数.  
#
x = 1
while x:
    if x // 80 % 7 == 0 and x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1:
        print(x)
    x += 1

# 7.有一种最简真分数,它们的分子与分母的乘积都是140,把所有这样的真分数从小到大打印出来
for i in range(1, 141):
    if 140 % i == 0:
        for j in range(2, i + 1):
            if i % j == 0 and 140 / i % j == 0:
                print('')
                break
            else:
                print('%s/%s' % (i, 140 / i))

#
# 8.一个五位数,若在它的后面写上一个7,得到一个六位数A,若在它前面写上一个7,得到一个六位数B,B是A的五倍,求此五位数.
#
for i in range(10000, 100000):
    if (700000 + i) / (i * 10 + 7) == 5:
        print(i)
# 9.把123456789这个数乘以一个什么数,能使它的结果不但不含零,而且仍然是   由1,2,3,4,5,6,7,8,9这九个数字组成的,只是顺序不同而已.
#


# 10.验证:任意一个大于9的整数减去它的各位数字之和所得的差,一定能被9整除.
#

x = 10
while x:
    y = 0
    for i in range(0, len(str(x))):
        y += int(str(x)[i])
    if (x - y) % 9 == 0:
        print(x)
    x += 1
# 11.今有四个人,他们得年龄各不相同,他们年龄总和是129,而其中有三个人的年龄是平方数,
# 若倒退15年,这四人中仍有三个人的年龄是平方数,求他们各自的年龄
#

# import math
#
#
# def ispow(num):
#     sq = math.sqrt(num)
#     return sq * sq == num
#
#
# for i in range(1, 101):
#     if ispow(i):
#         print(i)

# 12.如果两个素数之差为2,这样的两个素数就叫作"孪生数",找出100以内的所有"孪生数".
import math

list1 = []
for i in range(2, 101):
    s = int(math.sqrt(i))
    c = True
    for j in range(2, s + 1):
        if i % j == 0:
            c = False
            break
    if c == True:
        list1.append(i)
print(list1)
for k in range(0, len(list1) - 1):
    if list1[k + 1] - list1[k] == 2:
        print(list1[k + 1], list1[k])
