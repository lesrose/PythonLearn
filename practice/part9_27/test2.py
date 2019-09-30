import random

money = 0
print('欢迎来到皇家竞猜'.center(50, '*'))
while True:
    while True:
        temp = int(input('请购买筹码'))
        if temp < 50:
            print('购买筹码50起')
        else:
            if money > 0:
                money += temp
                print('购买成功，余额：', money)
                break
            else:
                money = temp
                print('购买成功，余额：', money)
                break
    while True:
        while True:
            out_money = int(input('请下注'))
            if out_money < 50 or money > money:
                print('下注金额 50-全部')
            else:
                print('下注成功')
                money -= out_money
                break
        while True:
            user_end = input('买大买小，买定离手')
            if user_end not in ('大', '小'):
                print('买大买小，买定离手')
            else:
                break
        x = random.randint(1, 6)
        if x <= 3:
            pc_end = '小'
        else:
            pc_end = '大'
        if pc_end == user_end:
            print('pc:%s,you:%s,你赢了')
            money += 2 * out_money
            print('剩余金额：', money)
        else:
            print('pc:%s,you:%s,你输了')
            print('剩余金额：', money)
        cho = input('是否继续 y / n')
        if cho == 'y':
            if money < 50:
                print('剩余不足，少于50')
                break
        else:
            print('欢迎下次再来'.center(50, '*'))
            exit()
