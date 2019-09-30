# 1.去掉字符串中的所有空格
x = input('input something')
print(x.split(' '))
# 2.根据完整的路径从路径中分离文件路径、文件名及扩展名
x = '‪D:\resource\py入门.pdf'
print(x.split('.'))

# 3.获取字符串中汉字的个数
x = 'Z:\share\Python人工智能1909\part_1第一阶段\随堂录屏\2019.9.26\2019.9.26_4循环控制.mp4'
for i in x:
    if 0x4e00 <= ord(i) <= 0x9fa5:
        print(i, end='')
# 4.对字符串进行加密与解密

# 5.将字母全部转换为大写或小写
x = '''‪D:\resource\py入门.pdf'''
print(x.lower())

# 6.根据标点符号对字符串进行分行
x = 'Z:\share\Python人工智能1909\part_1第一阶段\随堂录屏\2019.9.26\2019.9.26_4循环控制.mp4'
for i in range(len(x.split('.'))):
    print(x.split('.')[i])

# 7.去掉字符串数组中每个字符串的空格
list1 = ['af asdeww', 'arqwe we rq']
for i in range(len(list1)):
    list1[i] = list1[i].replace(' ', '')
print(list1)

# 8.随意输入你心中想到的一个书名，然后输出它的字符串
# 长度。 （len()属性:可以得字符串的长度）
x = input('book name')
print('它的字符串长度%s' % (len(x)))

# 9.两个学员输入各自最喜欢的游戏名称，判断是否一致,如
# 果相等,则输出你们俩喜欢相同的游戏；如果不相同,则输
# 出你们俩喜欢不相同的游戏。
x = input('game name1')
y = input('game name2')
if x == y:
    print('你们俩喜欢相同的游戏')
else:
    print('你们俩喜欢不相同的游戏')
# 10.上题中两位同学输入 lol和 LOL代表同一游戏，怎么办?
x = input('game name1')
y = input('game name2')
if x == y or x.lower() == y.lower():
    print('你们俩喜欢相同的游戏')
else:
    print('你们俩喜欢不相同的游戏')
# 11.让用户输入一个日期格式如“2008/08/08”，将 输入的日
# 期格式转换为“2008年-8月-8日” 。
x = input('input date like 2008/08/08')
print(x.replace('/', '-'))

# 12.接收用户输入的字符串，将其中的字符进行排序（升序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。
s = 'cabed'
list1 = []
for i in s:
    list1.append(i)
for i in range(len(list1)):
    for j in range(len(list1) - 1):
        if ord(list1[j]) > ord(list1[j + 1]):
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)
list1.reverse()
print(''.join(list1))
# 13.接收用户输入的一句英文，将其中的单词以反序输出，“hello c sharp”→“sharp c hello”。

s = 'hello c sharp'
list1 = s.split(' ')
list1.reverse()
print(' '.join(list1))
# 14.从请求地址中提取出用户名和域名 http://www.163.com?userName=admin&pwd=123456

# 15.有个字符串数组，存储了10个书名，书名有长有短，现在将他们统一处理，若书名长度大于10，则截取长度8的
# 子串并且最后添加“...”，加一个竖线后输出作者的名字。

# 16.让用户输入一句话,找出所有"呵"的位置。
s = '呵的位置呵的位置呵的'
for i in range(len(s)):
    if s[i] == '呵':
        print(i)
# 17.让用户输入一句话,找出所有"呵呵"的位置。
# 18.让用户输入一句话,判断这句话中有没有邪恶,如果有邪恶就替换成这种形式然后输出,如:“老牛很邪恶”,输出后变
# 成”老牛很**”;
if s.find('邪恶'):
    s = s.replace('邪恶', '**')
print(s)
# 75/75
# 19.如何判断一个字符串是否为另一个字符串的子串
if y.find(x) > 0:
    print('yes')
else:
    print('no')

# 20.如何验证一个字符串中的每一个字符均在另一个字符串中出现过
x = 'ab'
y = 'yabc'
# 21.如何随机生成无数字的全字母的字符串

# 22.如何随机生成带数字和字母的字符串

# 23.如何判定一个字符串中既有数字又有字母
x = 'aderty'
a = False
b = False
for i in x:
    if 48 <= ord(i) <= 57:
        a = True
    elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        b = True
if a and b:
    print('既有数字又有字母')
# 24.字符串内的字符排序（只按字母序不论大小写）
s = 'aABFGTcd'
list1 = list(s)
list2 = [(x.lower(), x) for x in list1]
list2.sort()
print(list2)
list3 = [x[1] for x in list2]
print(list3)

# 25.字符串的补位操作
# 1 =》001
# 2 =》002
# 10=》010
s='1'
list1=list(s)
if len(s)==2:
    list1.insert(0,'0')
elif len(s)==1:
    list1.insert(0, '0')
    list1.insert(1, '0')
else:
    list1.append(000)
print(list1)