# year=0
# # money=1000
# # while money<2000:
# #     money= money+money*0.0414
# #     year+=1
# # print(year)

# for i in range(3):
#     user_name=input('input username')
#     user_pwd=input('input passwd')
#     if user_name=='admin' and user_pwd=='666666':
#         print('login')
#         break
#     else:
#         if user_name !='admin':
#             print('usrname error')
#         else:
#             print('pass error')
#         print('error time ',i+1)
#         if i==2:
#             print('error too many')

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(5):
#     for j in range(5 - i):
#         print('*', end='')
#     print()

# for i in range(3):
#     for j in range(2*(i+1)-1):
#         print('*', end='')
#     print()

# for i in range(3):
#     for j in range(2 * (3 - i) - 1):
#         print('*', end='')
#     print()
#
# for i in range(10):
#     print('*'*3)

# for i in range(5):
#     print('*'*(i+1))

# for i in range(5):
#     print('*'*(5-i))

# x = 5
# for i in range(x):
#     print(' ' * (x - i - 1), end='')
#     print('*' * (2 * (i + 1) - 1))

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%s*%s=%s \t' % (j, i, i * j), end='')
#     print('')

# for i in range(1, 10):
#     for j in range(9):
#         if (j + 1) >= i:
#             print('%s*%s=%s \t' % (i, j + 1, i * (j + 1)), end='')
#         else:
#             print(' ' * 8, end='')
#     print('')
#
# for i in range(4):
#     print('*'*(2*(i+1)-1))

# for i in range(7):
#     print('*'*(7-i))

# for i in range(4):
#     print(' '*(3-i),end='')
#     print('*'*(2*(i+1)-1))

# for i in range(4):
#     print(' '*(3-i),end='')
#     print('*'*(2*(i+1)-1))
# for i in range(3):
#     print(' '*(i+1),end='')
#     print('*'*(2*(3-i)-1))
#
# for i in range(1, 141):
#     if 140 % i == 0:
#         for j in range(2, i + 1):
#             if i % j == 0 and 140 / i % j == 0:
#                 break
#             else:
#                 if i < 140 / i:
#                     print('%s/%s' % (i, int(140 / i)))
#                     break


# for i in range(1, 141):
#     for j in range(1, 141):
#         if i * j == 140:
#             if i == 1:
#                 print('%s/%s' % (i, j))
#             else:
#                 for k in range(2, i + 1):
#                     if i % k == 0 and j % k == 0:
#                         break
#                     else:
#                         if i < j:
#                             print('%s/%s' % (i, j))
#                             break

# for i in range(10,2,-1):
#     print(i)

s='asdasfassaa'
print(s.split('a',1))