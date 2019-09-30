import random

money = 0
print('welcome to this game'.center(50, '*'))
while True:
    while True:
        buy = int(input('请购买筹码，50起'))
        if buy < 50:
            print('购买太少')
        else:
            if money > 0:
                money += buy
                print('购买成功，你的余额为：', money)
                break
            else:
                money = buy
                print('购买成功，你的余额为：', money)
                break
    while True:
        while True:
            out_money = int(input('请下注，50起'))
            if out_money < 50 or out_money > money:
                print('下注金额，50-全额')
            else:
                money -= out_money
                break
        while True:
            user_end = input('买大买小，买定离手')
            if user_end not in ('大', '小'):
                print('选择有误')
            else:
                break
        x = random.randint(1, 7)
        if x <= 3:
            pc_end = '小'
        else:
            pc_end = '大'
        if user_end == pc_end:
            print('pc point:%s,%s,your:%s,你赢了' % (x, pc_end, user_end))
            money += 2 * out_money
            print('你的剩余金额：', money)
        else:
            print('pc point:%s,%s,your:%s,你输了' % (x, pc_end, user_end))
            print('你的剩余金额：', money)
        cho = input('是否继续，y / n')
        if cho == 'y':
            if money <= 49:
                print('余额不足，请充值')
                break
        else:
            print('欢迎下次再来'.center(50, '*'))
            exit()
