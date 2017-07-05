import random
result = random.randint(1,10)
time = int(input('你觉得有需要几次机会：'))
chance = time
print('请输入一个1到10之间的整数：' , end = '')
guess = 0
while guess != result and time > 0:
    temp = input()
    if not temp.isdigit():
        print('输入的不是整数，请重新输入：' , end = '')
    else:
        guess = int(temp)
        if not  (guess >  0 and guess < 11):
            print('输入的不在1到10之间，请重新输入：' , end = '')
        else:
            time = time - 1
            if guess == result:
                print('猜对了，答案就是：'+ str(result))
            else:
                if guess > result:
                    print('大了！')
                else:
                    print('小了！')
                if time < 1:
                    print(str(chance) + '次机会都猜错了！')
                else:
                    print('请重新输入:' , end = '')
print('游戏结束！')
