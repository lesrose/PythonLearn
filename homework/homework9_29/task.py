# 必做：
# 1、写一个方法，在方法内依次打印出列表每个元素的值。
# def  PrintAll(listA):
#     for i in listA:
#        print(i)
#
# 2、写一个方法，计算列表所有元素的和(注意返回值)。
# list1=[1,2,3,4,5]
# def sum_A(list1):
#     x=0
#     for i in list1:
#         x+=i
#     return x
# print(sum_A(list1))
# 3、写一个方法，计算列表所有奇数下标元素的和(注意返回值)。
# list1 = [1, 2, 3, 4, 5]
# def sum_A(list1):
#     x = 0
#     for i in range(len(list1)):
#         if i % 2 == 1:
#             x += list1[i]
#     return x
# print(sum_A(list1))
# 4、写一个方法，计算列表所有偶数下标元素的和(注意返回值)。
# list1 = [1, 2, 3, 4, 5]
# def sum_A(list1):
#     x = 0
#     for i in range(len(list1)):
#         if i % 2 == 0:
#             x += list1[i]
#     return x
# print(sum_A(list1))
# 5、写一个方法可以计算两个数的和，想想这个方法有哪些参数，返回值。
# def sum(a, b):
#     return a + b
#
#
# print(sum(1, 3))
# 6、写一个方法可以计算两个数的商(分母不能为0)，想想这个方法有哪些参数，返回值是什么。
# def sum(a, b):
#     if b!=0:
#         return a / b
#     else:
#         return '分母不能为0'
#
#
# print(sum(1, 0))
# 7、写一个方法将传入的天、小时、分钟、秒的总和转换为秒，比如0天、2小时、5分、7秒，他们代表的总秒数为2*3600+5*60+7=7507秒。想想这个方法有哪些参数，返回值是什么类型。
# def csec(a=0, b=0, c=0, d=0):
#     return a * 24 * 3600 + b * 3600 + c * 60 + d
#
#
# print(csec(0, 2, 5, 7))
# 8、写一个方法交换整型列表中两个指定下标元素的值。想想这个方法有哪些参数，返回值是什么类型。
# lis=[1,2,3,4,5]
# def swaps(lis, a, b):
#     lis[a], lis[b] = lis[b], lis[a]
# swaps(lis,1,2)
# print(lis)
# 9、写一个方法计算整型列表中所有能被3整除元素的个数。想想这个方法有哪些参数，返回值是什么类型。
# lis = [1, 6, 3, 4, 5]
#
#
# def cou(lis):
#     x = 0
#     for i in lis:
#         if i % 3 == 0:
#             x += 1
#     return x
#
#
# print(cou(lis))
# 10、写一个方法将整型数字(int)转换为格式化的字符串(string)，现要求如下：
# a.可以指定转换后[字符串的长度];
# b.当数字的长度不足指定的长度，让这个字符串右对齐，指定[左边补的字符(char)];
# 例如，假设现在将指定的数字转换为固定长度为8的字符串，如果长度不足，左边补'0'，那么27这个数字就会转换为字符串"00000027"。
# 根据要求，想想这个方法有哪些参数，返回值是什么类型。
# def itos(i,a):
#     return str(i).rjust(a,'0')
#
#
# print(itos(27, 8))

# a=27
# s=str(a)
# print(s.rjust(8,'0'))

# 11.用方法实现找出一个int类型列表中最大值和最小值 
#   
# def finds(lis):
#     return max(lis),min(lis)


# 12.判断一个数是否是质数(素数)？该如何声明方法？ 
# def issu(i):
#     for j in range(2,i):
#         if i%j==0:
#             return 'no'
#         else:
#             return 'yes'
#
#
# print(issu(5))
# 13. 将指定的秒数转变为几小时几分几秒。
#
# def counts(i):
#     return i // 3600, (i - (i // 3600)*3600) // 60, i % 60
#
#
# print(counts(450))
# 14.使用Random类给一个数组的所有元素赋随机初值（不重复）。
# import  random
# def intt(lis,a):
#     for i in range(a):
#         lis[i]=random.randint(1,100)
# 15.判断一个整型list是否是对称的。所谓对称就是第一个元素等于最后一个元素，第二个元素等于倒数第二个元素
# ，依次类推，例如【7，3，1，3，7】就是对称的。 
# def jug(lis):
#     x=len(lis)//2
#     c=True
#     for i in range(x):
#         if lis[i]!=lis[-(i+1)]:
#             c=False
#             break
#     return c
#
# lis=[7,3,1,1,3,7]
# print(jug(lis))
# 16.打印一个元组的所有值。
# def printos(tup):
#     for i in tup:
#         print(i)
# 17.查找一个元组中某个值是否存在，如果存在返回这个值的索引，否则返回-1。 
# def fins(tup, s):
#     if s in tup:
#         return tup.index(s)
#     return -1
#
#
# tup = (1, 11, 2, 6)
# print(fins(tup, 2))
# 18.将一个列表反转过来，比如【2，3，1，4，7】转换为【7，4，1，3，2】 
# 19.求一个列表的最大值。 
# 20.求一个列表的最小值。 
# 21.写一个方法，实现在列表中指定的的位置前插入一个值。 
# 22.写一个方法，删除列表中指定位置的元素。 
#
# 23.猜数游戏 （1-100）
# 1.随机出现一个数(范围自定义) 作为答案
# 2.提示用户输入并根据答案和用户输入的大小关系输出大了? 小了?
# 3.5次机会
# 4.可以重复玩
# 5.根据猜对的次数进行评价
# 6.无论对错 请告知答案
# import random
#
# while True:
#     x = random.randint(1, 100)
#     z = 0
#     while True:
#         y = int(input('input your num'))
#         if x > y:
#             z += 1
#             print('小了,第%s次' % z)
#         elif x < y:
#             z += 1
#             print('大了,第%s次' % z)
#         else:
#             z += 1
#             print('you win')
#             if z == 1:
#                 print('你的得分：100 ')
#             elif z == 2:
#                 print('你的得分：80 ')
#             elif z == 3:
#                 print('你的得分：60 ')
#             elif z == 4:
#                 print('你的得分：40 ')
#             elif z == 5:
#                 print('你的得分：20 ')
#             break
#         if z == 5:
#             print('game over 原数：', x)
#             print('你的得分：0 ')
#             break
#     cho=input('是否继续 y / n ')
#     if cho =='y':
#         pass
#     else:
#         break
# 1、编写函数，用户输入三个整数，将最大数和最小数输出
# def mina():
#     lisr = []
#     x = int(input('fir'))
#     lisr.append(x)
#     y = int(input('sec'))
#     lisr.append(y)
#     z = int(input('thr'))
#     lisr.append(z)
#     print(max(lisr), min(lisr))
# 2、编写函数将1~200末位数为5的整数求和返回
# def suma():
#     list1 = []
#     for i in range(1, 201):
#         if i % 10 == 5:
#             list1.append(i)
#     return sum(list1)
# 3、编写函数将24的所有因子求积、求和
# def jihe():
#     list1=[]
#     x=1
#     for i in range(1,25):
#         if 24%i==0:
#             if i not in list1:
#                 list1.append(i)
#     for i in range(len(list1)):
#         x*=list1[i]
#     print(sum(list1),x)
# jihe()
# 4、输入学员的语文、数学和英语三门课的成绩，计算平均成绩输出。
#
# 5、输入一个圆的半径(int),并且输出这个圆的面积。
#
# 6、企业发放的奖金根据利润提成。利润(I)低于或等于1万元时，奖金可提10%；
# 利润高于1万元，低于2万元时，低于1万元的部分按10%提成，
# 高于1万元的部分，可提成7.5%；2万到4万之间时，高于2万元的部分，可提成5%；
# 4万到6万之间时高于4万元的部分，可提成3%；6万到10万之间时，高于6万元的部分，可提成1.5%，
# 高于10万元时，超过10万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？编写相应的函数？

# 7、超市收银系统规定，消费满500元的可以打9.8折，消费满800元可以打9.5折，
# 消费满1000元可以打9折，先要求输入消费数额，
# 显示应收金额及折扣金额——“您合计收费***元  本次收***元  为您节省***元”
#
# 8、本金10000元存入银行，年利率是千分之三。每过1年，
# 将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
#
# 9、编写一个游戏级别评分器，循环录入每一局（共10局）的游戏得分，显示输出游戏级别。
# 评分标准：10局中如果90%达到80以上，为一级，如果60%达到80之上为二级，其余为三级。
#
# 10、登录QQ时，QQ号和密码必须正确并且匹配才能够登录成功。假设最多只允许用户输入三次，
# 中间任何一次输入正确，则给出提示：登录成功。如第一次输入信息有误，则给出提示
# ：QQ号或密码输入有误，请重新输入，您还有2次机会。
# 第二次还输入有误，则给出：QQ号或密码输入有误，请重新输入，您还有1次机会。
# 第三次如输入还有误，则给出提示：您三次输入都有误，请与管理员联系。
#
# 11、编写函数从键盘输入2016年的某个月份，得到当月的天数
#
# 12、编写函数输入两个数m和n，分别输出这两个数的最大公约数和最小公倍数
# def finsd(a, b):
#     x = a * b
#     if a > b:
#         x = a
#         z = b
#     else:
#         x = b
#         z = a
#     lisr = []
#     for i in range(b, 0, -1):
#         if a % i == 0 and b % i == 0:
#             print(i)
#             break
#     for i in range(a * b - 1, 0, - 1):
#         if i % a == 0 and i % b == 0:
#             lisr.append(i)
#     if len(lisr) == 0:
#         print(a * b)
#     else:
#         print(min(lisr))
# finsd(9,6)

#
# 选作：
# 1、输入一段字符判断是大写，还是小写。若是小写，转换为大写，若是大写，转换为小写
#
# 2、一列数的规则如下: 1、1、2、3、5、8、13、21、34...... 求第30位数
# 是多少， 用递归算法实现
# def digui(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return digui(n-2)+digui(n-1)
#
#
# print(digui(9))
#
# 3、请编程实现对一个数组的排序，结果从大到小
#
# 4、接收一个整数(1-26之间),打印A-Z之间图形。如接收26，则打印如下图形
#      (char)65-->A   (char)66-->B
#      以此类推
#                                    A
#                                   BBB
#                                  CCCCC
#                                 DDDDDDD
#                                EEEEEEEEE
#                               FFFFFFFFFFF
#                              GGGGGGGGGGGGG
#                             HHHHHHHHHHHHHHH
#                            IIIIIIIIIIIIIIIII
#                           JJJJJJJJJJJJJJJJJJJ
#                          KKKKKKKKKKKKKKKKKKKKK
#                         LLLLLLLLLLLLLLLLLLLLLLL
#                        MMMMMMMMMMMMMMMMMMMMMMMMM
#                       NNNNNNNNNNNNNNNNNNNNNNNNNNN
#                      OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#                     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
#                    QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
#                   RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
#                  SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#                 TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
#                UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
#               VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#              WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#            YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
#           ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
#
def printt(n):

    for i in range(n):
        print(' '*(n-i-1),end='')
        for j in range(2*(i+1)-1):
            print(chr(65+i),end='')
        print()
printt(10)
# 5. 键盘输入一个整数(0-9之间)，显示如下图形(n=5)
#     12345
#      2345
#       345
#        45
#         5
# def prints(n):
#     for i in range(n):
#         print(' ' * i, end='')
#         for j in range(i+1,n+1):
#             print(j,end='')
#         print()
# prints(5)
# 6、输入一个奇数显示以下图型（如：num=5）
#  *****
#   ***
#    *
#   ***
#  *****
