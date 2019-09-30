import calendar
import datetime

# yy=2015
# mm=6
# print(calendar.month(yy, mm))

# with open('test.txt','wt')as out_file:
#     out_file.write('该文本会写入到文件中\n看到我了吧！')
#
# with open('test.txt','rt')as  in_file:
#     text=in_file.read()
# print(text)
# mothrange=calendar.monthrange(2016,9)
# print(mothrange)


# today=datetime.date.today()
# print(today)
# print(datetime.timedelta(days=2))
# print((today - (datetime.timedelta(days=1))))

# list1 = []
# for i in range(13):
#     list1.append(i + 1)
# print(list1)
# x = 0  # 统计人数
# i = 0
# # a = 0
# while True:
#     z = 1
#     a = 0
#
#     if z == 9:
#         if i > len(list1):
#             print(list1[i])
#             list1.pop(i)
#             x += 1
#         else:
#             print(list1[i + 1])
#             list1.pop(i + 1)
#             b = list1[i + 2]
#             x += 1
#     else:
#         z += 1
#         i += 1
#     if x == 15:
#         break

# a = [x for x in range(1, 31)]  # 生成编号
# del_number = 8  # 该删除的编号
# for i in range(15):
#     print(a[del_number])
#     a.pop(del_number)
#     del_number = (del_number + 8) % len(a)
#

# a = [x for x in range(1, 31)]
# x = 9
#
# index = 0
# for i in range(30):
#     count = 0
#     while count < 9:
#         if a[index] != 0:
#             count += 1
#         if count==9:
#             print(a[index])
#             a[index]==0
#         index=(index+1)%30
# people=list(range(30))
# # while len(people)>15:
# # #     i=1
# # #     while i<9:
# # #         people.append(people.pop(0))
# # #         i+=1
# # #     print('{:2d}号下船了'.format(people.pop(0)))
# # #
# # #
# print(people.pop(0))