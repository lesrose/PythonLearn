# x = 0
# for i in range(100, 501):
#     if i % 2 == 1:
#         x += i
# print(x)

# for i in range(100, 201):
#     if i % 3 != 0:
#         print(i)

# x = 0
# for i in range(1, 1001):
#     if i % 5 == 0 and i % 7 == 0:
#         x += 1
# print(x)

# n = int(input('input num'))
# c = 0
# for i in range(n):
#     x = 1
#     for j in range(1, i + 2):
#         x *= j
#     print(x)
#     c += x
# print(c)

# x = 0
# for i in range(1000, 1, -1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#         x += 1
#         if x == 10:
#             break

# x = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(x)):
#     x[i] = 2 * x[i]
# print(x)

# x=[1, 2, 3, 4]
# y=[4, 3, 2, 1]
# z=[]
# for i in range(len(x)):
#     z.append(x[i]+y[i])
# print(z)

# lis1 = []
# for i in range(5):
#     x = input('input %s number' % (i + 1))
#     lis1.append(x)
# print(min(lis1))

# list1 = []
# for i in range(1, 1001):
#     if i % 3 == 0:
#         list1.append(i)
# for i in range(len(list1)):
#     print(list1[i], end=',')
#     if (i + 1) % 10 == 0:
#         print()

# list1 = []
# x = int(input('input int '))
# while x != 0:
#     list1.append(x)
#     x = int(input('input int '))
# print('最大数%s和最小数%s'%(max(list1),min(list1)))

#
# x = int(input('input int '))
# while x<0 or x>100:
#     print('不满足,重新输入分数')
#     x = int(input('input int '))

# list1=[]
# x=0
# for i in range(10):
#     x=int(input('input int'))
#     if x==999:
#         break
#     else:
#         list1.append(x)
# for i in range(len(list1)):
#     if list1[i]>0:
#         x+=list1[i]
# print(x)

#
# list1 = []
# x=0
# for i in range(1, 101):
#     if i % 3 != 0 and i % 10 != 2 and i % 10 != 3 and i % 10 != 4 and i % 10 != 7:
#         list1.append(i)
# for i in range(len(list1)):
#     x+=list1[i]
# print(list1)
# print(x)

# import  calendar
# list1 = []
# for i in range(1900,2020):
#     if calendar.isleap(i):
#         list1.append(i)
# print(len(list1))
# print(list1)

# list1=[1,2,34,5,6,7,8]
# print(list1[::-1])


# list1 = [1, 2, 34, 5, 6, 7, 8]
# x = list1.index(max(list1))
# list1[0], list1[x] = list1[x], list1[0]
# y = list1.index(min(list1))
# list1[len(list1) - 1], list1[y] = list1[y], list1[len(list1) - 1]
# print(list1)
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

list1 = [1, 2, 4, 4, 5, 7, 8]
for i in list1:
    if i == 4:
        list1.remove(i)
print(list1)
