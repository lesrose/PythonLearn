# 1.让用户输入一个月份，判断这个月是哪个季节？假定3到
# 4月是春季，5到8月是夏季，9到10是秋季，11、12、1、2
# 月是冬季。

x = int(input('input month'))
if x in (3, 4):
    print('spring')
elif x in (5, 6, 7, 8):
    print('summer')
elif x in (9, 10):
    print('autumn')
elif x in (11, 12, 1, 2):
    print('winter')
else:
    print('error')

# 2.让用户输入小强的语文、数学和英语成绩，输出以下判
# 断是否正确，正确输出true，错误输出false
# a.语文、英语和数学成绩都大于85分；
# b.语文、英语和数学至少有一门大于95分；
# c.语文和英语至少有一门大于90分且数学不低于80分。
ch = int(input('input ch'))
math = int(input('input math'))
eng = int(input('input eng'))
print(ch > 85 and eng > 85 and math > 85)
print(ch > 95 or eng > 95 or math > 95)
print((ch > 90 or eng > 90) and math >= 80)

# 3.使用分支语句完成一个简单的计算器程序，用户输入两
# 个数字，用四则运算符计算结果并显示在控制台上。
x = int(input("input first number"))
y = int(input("input second number"))
s = input('input method')
if s == '+':
    print('%s+%s=%s' % (x, y, x + y))
elif s == '-':
    print('%s-%s=%s' % (x, y, x - y))
elif s == '*':
    print('%s*%s=%s' % (x, y, x * y))
elif s == '/':
    print('%s/%s=%s' % (x, y, x / y))

# print("%s+%s=%s" % (x, y, x + y))
# print("%s-%s=%s" % (x, y, x - y))
# print("%s*%s=%s" % (x, y, x * y))
# print("%s/%s=%s" % (x, y, x / y))

# 4.请用户输入两次，每次输入一个数字，如果用户输入的
# 第一个数大就输出第一个数，如果用户输入的第二个数大
# 就输出第二个数。
x = int(input("input first number"))
y = int(input("input second number"))
if x > y:
    print(x)
else:
    print(y)
# 5.请用户输入一个字符串，根据这个字符串的长度得出如
# 下结果:
# s = "1234"; 字符串的长度:len(s)
# 长度：0-56之间: 输出：短消息
# 长度：57-128之间: 输出：一般消息
# 长度：129-192之间: 输出：长消息
# 长度：193-256之间: 输出：超长消息
# 长度：其他情况：长度超过可发送上限
x = input('input string')
y = len(x)
if y <= 56 and y >= 0:
    print('short message')
elif y <= 128 and y >= 57:
    print('common message')
elif y <= 192 and y >= 129:
    print('long message')
elif y <= 256 and y >= 193:
    print('super long message')
else:
    print('too long')
# 6.随机产生一个0-5之间的数：
# 随机产生的数：0：输出：进入战斗
# 随机产生的数：1：输出：捡到宝箱
# 随机产生的数：2：输出：捡到武器
# 随机产生的数：3：输出：捡到弹药
# 随机产生的数：4：输出：踩到陷阱
# 随机产生的数：5：输出：无事件
import random

a = random.randint(0, 5)
if a == 0:
    print('进入战斗')
elif a == 1:
    print('捡到宝箱')
elif a == 2:
    print('捡到武器')
elif a == 3:
    print('捡到弹药')
elif a == 4:
    print('踩到陷阱')
elif a == 5:
    print('无事件')
# 7.老师问学生,这道题你会做了吗?如果学生答"会了(y)",则
# 可以放学.如果学生不会做(n),则老师再讲一遍

x = None
while x != 'y':
    print('这道题你会做了吗?')
    x = input('is can do')

# 8.提示用户输入年龄，如果大于等于18，则告知用户可以
# 54/75
# 查看，如果小于10岁，则告知不允许查看，如果大于等于
# 10岁并且小于18，则提示用户是否继续查看（yes、
# no），如果输入的是yes则提示用户请查看，否则提示"退
# 出,你放弃查看"。

x = int(input('input your age'))
if x >= 18:
    print('can see')
elif x < 10:
    print('can not see')
elif x >= 10 and x < 18:
    print('is to see')
    y = input('input ')
    if y == 'yes':
        print('see')
    elif y == 'no':
        print('quit')
# 9.请用户输入自身的血压值（高压和低压） 请依据下面标
# 准血压 判断出用户的血压是否正常 若正常 显示血压正常
# 否则显示用户血压不正常
#  标准：成人：收缩压：90-140mmHg 舒张压：
# 60-90mmHg
x = int(input('收缩压'))
y = int(input('舒张压'))
if (x >= 90 and x <= 140) and (y >= 60 and y <= 90):
    print('normal')
else:
    print('unormal')

# 10.某商店T恤的价格为35元/件（2件9折，3件以上8折）,
# 裤子的价格为120元/条（2条以上9折）.小明在该店买了3
# 件T恤和2条裤子,请计算并显示小明应该付多少钱?
x = int(input('T shirt'))
y = int(input('pants'))

if x == 1:
    x = 35
elif x == 2:
    x = 35 * 2 * 0.9
elif x >= 3:
    x = 35 * x * 0.8
else:
    print('error')

if y == 1 or y == 2:
    y = 120 * y
elif y > 2:
    y = 120 * y * 0.9
else:
    print('error')

print('total prince %s' % (x + y))
