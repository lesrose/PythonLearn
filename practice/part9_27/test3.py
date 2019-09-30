# 1、分别定义int型列表、bool型列表、str型列表
# x=[1,2,3,4]
# y=[True,False]
# z=['a','v']
# 2、定义列表，并赋初值["hello","qikuedu"]，打印出这个列表的长度。
# list1=["hello","qikuedu"]
# print(len(list1))
# 3、定义一个列表，并赋初值["u","n","i","t","y"]，打印出这个列表最后一个元素的值。
# list1=["u","n","i","t","y"]
# print(list1[len(list1)-1])
# 4、定义一个列表，并赋初值[5, 3, 7, 6, 8]，将第4个元素的值修改为原来的2倍，然后分别打印第2个和第4个元素的值。
# list1=[5, 3, 7, 6, 8]
# list1[3]=2*list1[3]
# print(list1[1],list1[3])
# 5、定义一个int型列表，并赋初值[3,2,5,8,4]，打印第3个和第5个元素的值，然后将第3个元素的值与第5个元素的值做交换，再打印这两个元素的值。
# list1=[3,2,5,8,4]
# print(list1[2],list1[4])
# list1[2],list1[4]=list1[4],list1[2]
# 6、定义一个整型列表，使用循环语句(for)给它每个元素赋值，值依次为0,1,2,3,4,... 要求100个元素。
# list1=[]
# for i in range(100):
#     list1.append(i)
# 7.一次语文测试后,老师让班长统计每一个学生的成绩并计算全班(全班共3人)的平均成绩、最好成绩、总成绩,然后把所有成绩显示出来.
# 好的解决方法：使用列表.
# list1=[95,96,87]
# x=0
# for i in range(len(list1)):
#     x+list[x]
# print('平均成绩%s、最好成绩%s、总成绩%s'%(x/len(list1),max(list1),x))
# 8.列表里面都是人的名字,以“|”连接:例如:老杨|老苏|老邹…
# (“老杨”,“老苏”,“老邹”,“老虎”,“老牛”,“老蒋”,“老王”,“老马”)
# list1 = ['老杨|老苏|老邹']

# 9.将一个整数列表的每一个元素进行如下的处理：如果元素是正数则将这个位置的元素的值加1，如果元素是负数则将这个位置的元素的值减1,如果元素是0,则不变。
# list1=[99,-1,0]
# for i in  range(len(list1)):
#     if list1[i]>0:
#         list1[i]+=1
#     elif list1[i]<0:
#         list1[i]-=1
#     else:
#         pass
# print(list1)
# 10.将一个字符串列表的元素的顺序进行反转。{“我”,“是”,”好人”} {“好人”,”是”,”我”}。
# list1=['i','is','good man']
# list1.reverse()
# print(list1)

# 1、现有列表[1, 2, 3, 4, 5, 6, 7],编写代码使得列表变为[2, 4, 6, 8, 10, 12, 14]，打印列表的所有元素
# x = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(x)):
#     x[i] = 2 * x[i]
# print(x)
# 2、现有列表[1, 2, 3, 4]和列表[4, 3, 2, 1]，编写代码使得两个列表对应索引的
# 元素相加，并赋值给一个新的列表，打印新列表的所有元素。
# x = [1, 2, 3, 4]
# y = [4, 3, 2, 1]
# z = []
# for i in range(len(x)):
#     z.append(x[i] + y[i])
# print(z)

# 3、输入5个数，求其中最小值，打印出来。
# lis1 = []
# for i in range(5):
#     x = input('input %s number' % (i + 1))
#     lis1.append(x)
# print(min(lis1))
# 4、让用户输入长方形的长和宽，然后显示出此长方形的周长
# length = input('input chang')
# width = input('input kuan')
# print('周长 ', 2 * width + 2 * length)

# 5、编写一个程序，判断用户输入的a、b、c值，能否构成一个三角形？
# list1 = []
# a = int(input('input a'))
# list1.append(a)
# b = int(input('input b'))
# list1.append(b)
# c = int(input('input c'))
# list1.append(c)
# if a + b > c and a + c > b and b + c > a:
#     print('it is ok')
# else:
#     print('no can')
# 6、打印输出1000以内可被3整数除的正整数，每行显示10个数
# list1 = []
# for i in range(1, 1001):
#     if i % 3 == 0:
#         list1.append(i)
# for i in range(len(list1)):
#     print(list1[i], end=',')
#     if (i + 1) % 10 == 0:
#         print()

# 7、循环接收N个整数，直到用户输入0结束。打印出这些数里的最大数和最小数。
# list1 = []
# x = int(input('input int '))
# while x != 0:
#     list1.append(x)
#     x = int(input('input int '))
# print('最大数%s和最小数%s' % (max(list1), min(list1)))

# 8、接收学生分数判断区间，学生分数必须在0-100之间，如果不满足，则提醒用户输入，直到输入一个正确的分数为止。
# x = int(input('input int '))
# while x < 0 or x > 100:
#     print('不满足,重新输入分数')
#     x = int(input('input int '))
# 9、接收10个整数，计算其中正整数的总和，如果其中用户输入999则循环结束。
#
# list1 = []
# x = 0
# for i in range(10):
#     x = int(input('input int'))
#     if x == 999:
#         break
#     else:
#         list1.append(x)
# for i in range(len(list1)):
#     if list1[i] > 0:
#         x += list1[i]
# print(list1)
# print(x)

#
# 10、求1-100之间个位数字不是2，3，4，7，并且不能被3整除的整数之和
# list1 = []
# x = 0
# for i in range(1, 101):
#     if i % 3 != 0 and i % 10 != 2 and i % 10 != 3 and i % 10 != 4 and i % 10 != 7:
#         list1.append(i)
# for i in range(len(list1)):
#     x += list1[i]
# print(list1)
# print(x)
# 11、输出1900 到今年之间所有的闰年，并且统计个数（能被 4 整除 但是不能被100整除 或者能被四百整除）
# import calendar
#
# list1 = []
# for i in range(1900, 2020):
#     if calendar.isleap(i):
#         list1.append(i)
# print(len(list1))
# print(list1)
#
# 12、将一个列表逆序输出

# list1 = [1, 2, 34, 5, 6, 7, 8]
# print(list1[::-1])
#
# 13、输入列表,元素不会重复（自定义即可），最大的与第一个元素交换，最小的与最后一个元素交换，输出列表。
# list1 = [1, 2, 34, 5, 6, 7, 8]
# x = list1.index(max(list1))
# list1[0], list1[x] = list1[x], list1[0]
# y = list1.index(min(list1))
# list1[len(list1) - 1], list1[y] = list1[y], list1[len(list1) - 1]
# print(list1)
#
# 14、青年歌手参加歌曲大奖赛，有10个评委进行打分，试编程求这位选手的平均得分（去掉一个最高分和一个最低分）。
#
# list1=[]
# c=0
# while True:
#     x=int(input('input %s '%(c+1)))
#     list1.append(x)
#     c+=1
#     if c==10:
#         break
# m=list1.index(max(list1))
# list1.pop(m)
# l=list1.index(min(list1))
# list1.pop(l)
# s=0
# for i in range(len(list1)):
#     s+=list1[i]
#
# print((s/(len(list1))))
#
# 15、定义一个列表，并赋初值[5, 3, 7, 6, 8]，将第4个元素的值修改为原来的3倍，然后分别打印下标是奇数的元素。

# list1 = [5, 3, 7, 6, 8]
# list1[4 - 1] = 3 * list1[4 - 1]
# for i in range(len(list1)):
#     if i % 2 == 1:
#         print(list1[i])
#
# 16、用户输入一个最大值n表示列表元素数,创建列表存数，数字是所有小于n的偶数
# list1 = []
# x = int(input('input n'))
# for i in range(x):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)
#
# 17、列表[1, 2, 4, 4, 5, 7, 8]，编写代码删掉列表中的所有4
# list1 = [1, 2, 4, 4, 5, 7, 8]
# for i in list1[::-1]:
#     if i == 4:
#         list1.remove(i)
# print(list1)

#
# 选做题：
# 1、将一个英文句子中的前后单词逆置（单词之间用空格隔开）。如：how old are you 逆置后为：you are old how
# s = 'how old are you'
# ss = ''
# list1 = s.split(' ')
# print(list1)
# list1.reverse()
# for i in list1:
#     i = i + ' '
#     ss += i
# print(ss)
# 2、公交报站系统，每经过一站，报出该站名称，若乘客在该站下车，在出站口提示“一共乘坐x站”。用while循环实现以上程序
# list1 = [['北京', 1], ['天津', 2], ['上海', 3], ['广州', 4], ['香港', 5]]
# while True:
#     for i in range(len(list1)):
#         print(list1[i][0])
#         cho = input('is keep y / n')
#         if cho == 'y':
#             if i == len(list1) - 1:
#                 print('终点站到了，一共乘坐%s站' % (int(list1[i][1])))
#                 break
#         else:
#             print('一共乘坐%s站' % (int(list1[i][1])))
#             break
#     break
# 3、有一电文，已按下列规律译成译码：
#               A→Z  a→z
#               B→Y  b→y
#               C→X  c→x
#               …    …


# 即第一个字母变成第26个字母，第i个字母变成第(26-i+1)个字母。非字母字符不变。编写一个程序将密码译成原文，并输出密码和原文。
# x = 'abcd123ABCD'
# list1=[]
# for i in range(len(x)):
#     if 65 <= ord(x[i]) <= 90:
#         list1.append(chr(int(155 - ord(x[i]))))
#     elif 97 <= ord(x[i]) <= 122:
#         list1.append(chr(int(219 - ord(x[i]))))
#     else:
#         list1.append(x[i])
# print(list1)
# print(''.join(list1))
# 4、计算圆周率：PI＝4/1－4/3+4/5-4/7.......
# x = 10000000
# z = 1
# y = -1
# c = 0
# while z < x:
#     y = -y
#     c += (4 / z) * y
#     z += 2
# print(c)

# 5、定义一个20*3的二维列表，用来存储某班级20位学员的3门课的成绩；
#  这3门课按存储顺序依次为：Python，Java，C#.
#  (1)循环给二维列表的每一个元素赋0~100之间的随机整数。
#  (2)按照列表的方式输出这些学员的每门课程的成绩。
#  (3)要求编写程序求每个学员的总分，将其保留在另外一个一维列表中。
#  (4)要求编写程序求所有学员的某门课程的平均分。

# list1=[]
# for i in range(20):
#     list1.append([])
# for i in range(len(list1)):
#     for j in range(3):
#         list1[i].append('')
# print(list1)
# import random
#
# list1 = [[(random.randint(1, 100)) for i in range(3)] for j in range(20)]
# print(list1)
# list2 = []
# for i in range(len(list1)):
#     x = 0
#     for j in range(3):
#         x += list1[i][j]
#     list2.append(x)
# print(list2)
# for i in range(len(list2)):
#     # print('{:0.2f}'.format(list2[i]/3))
#     print('%0.2f' % (list2[i] / 3))

# x='string'
# print(x.count('x'))