import random

print('welcome to this game'.center(50, '*'))
x = random.randint(1, 3)
pc = ''
if x == 1:
    pc = '剪刀'
elif x == 2:
    pc = '石头'
elif x == 3:
    pc = '布'

user = input('剪刀，石头，布，请出示')
if user not in ('剪刀', '石头', '布'):
    print('input error')
else:
    if user == pc:
        print('pc: %s,user: %s same' % (pc, user))
    elif user == '剪刀':
        if pc == '石头':
            print('pc: %s,user: %s you lose' % (pc, user))
        else:
            print('pc: %s,user: %s you win' % (pc, user))
    elif user == '石头':
        if pc == '剪刀':
            print('pc: %s,user: %s you win' % (pc, user))
        else:
            print('pc: %s,user: %s you lose' % (pc, user))
    elif user == '布':
        if pc == '剪刀':
            print('pc: %s,user: %s you lose' % (pc, user))
        else:
            print('pc: %s,user: %s you win' % (pc, user))
