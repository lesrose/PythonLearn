import os

# x=input('input something')
# x = 'asd asdaf   asdarwqrs eqqq'
# print(x.replace(' ', ''))
# print(''.join(x.split()))

# x='‪D:\resource\py入门.pdf'
# (filepath,tempfilename)=os.path.split(x)
# (shotname,extension)=os.path.splitext(tempfilename)
# print(shotname)
# print(extension)
# print(filepath)
# print(tempfilename)

# x='ASDFGHJKWdfer2415161ERTYUKzxc'
# print(x.lower())

# x='Z:\share\Python人工智能1909\part_1第一阶段\随堂录屏\2019.9.26\2019.9.26_4循环控制.mp4'
# for i in x:
#     if 0x4e00<=ord(i)<=0x9fa5:
#         print(i,end='')

# x='Z:\share\Python人工智能1909\part_1第一阶段\随堂录屏\2019.9.26\2019.9.26_4循环控制.mp4'
# for i in range(len(x.split('.'))) :
#     print(x.split('.')[i])


# list1=['af asdeww','arqwe we rq']
# for i in range(len(list1)):
#     list1[i]=list1[i].replace(' ','')
# print(list1)

# x=input('book name')
# print('它的字符串长度%s'%(len(x)))

# x=input('game name1')
# y=input('game name2')
# if x==y or x.lower() == y.lower():
#     print('你们俩喜欢相同的游戏')
# else:
#     print('你们俩喜欢不相同的游戏')

# x=input('input date like 2008/08/08')
# print(x.replace('/','-'))

# 12.接收用户输入的字符串，将其中的字符进行排序（升序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。
# s = 'cabed'
# list1=[]
# for i in s:
#     list1.append(i)
# for i in range(len(list1)):
#     for j in range(len(list1) - 1):
#         if ord(list1[j]) > ord(list1[j + 1]):
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
# print(list1)
# list1.reverse()
# print(''.join(list1))
#
# s='hello c sharp'
# list1=s.split(' ')
# list1.reverse()
# print(' '.join(list1))

# s='呵的位置呵的位置呵的'
# for i in range(len(s)):
#     if s[i]=='呵':
#         print(i)

# s='aa老牛很邪恶'
#
#
# if s.find('邪恶'):
#     s=s.replace('邪恶','**')
# print(s)

# x='ab'
# y='yabc'
# if y.find(x)>0:
#     print('yes')
# else:
#     print('no')

# 23.如何判定一个字符串中既有数字又有字母
# x = 'aderty'
# a = False
# b = False
# for i in x:
#     if 48 <= ord(i) <= 57:
#         a = True
#     elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
#         b = True
# if a and b:
#     print('既有数字又有字母')

# 24.字符串内的字符排序（只按字母序不论大小写）

# s = 'aABFGTcd'
# list1 = []
# for i in s:
#     list1.append(i)
# # for i in range(len(list1)):
# #     for j in range(len(list1) - 1):
# #         if ord(list1[j]) == ord(list1[j + 1]) or abs(ord(list1[j]) - ord(list1[j + 1])) == 32:
# #             continue
# #         if ord(list1[j]) > ord(list1[j + 1]):
# #             list1[j], list1[j + 1] = list1[j + 1], list1[j]
# # print(list1)
# list1.sort()
# print(list1)
# a=''
# x=0
# list2=[]
# for i in range(len(list1)):
#     if ord(list1[i]) >= 97:
#         list2 = list1[:i]
#         break
#         # a=list1[i]
#         # print('list',list2)
#         # # list1.pop(i)
#         # for j in range(len(list2)):
#         #     if ord(a)-32>=ord(list2[j]):
#         #         list2.insert(j,a)
#         #         break
# list3=[]
# for i in range(len(list1)):
#     if list1[i] not in list2:
#         list3.append(list1[i])
# print(list2)
# print(list3)
# list4=[]
# for i in range(len(list3)):
#     for j in range(len(list2)):
#         if ord(list3[i])>=ord(list2[j]):
#             list2.insert(j,list3[i])
#
# print(list2)
# s = 'aABFGTcd'
# s=s.lower()
# print(s)
# # list1=s.split('')
# list1=list(s)
#
# list1.sort()
# print(list1)
# s = 'aABFGTcd'
# list1=list(s)
# list2=[(x.lower(),x)for x in list1]
# list2.sort()
# print(list2)
# list3=[x[1] for x in list2]
# print(list3)

s=''
list1=list(s)
if len(s)==2:
    list1.insert(0,'0')
elif len(s)==1:
    list1.insert(0, '0')
    list1.insert(1, '0')
elif len(s)==0:
    list1.append(0)
    list1.append(0)
    list1.append(0)
else:
    pass
print(list1)