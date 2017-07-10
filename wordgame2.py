import random
result = random.randint(1,10)
#result = 5
guess = 0
time = 3
print('请输入一个1到10之间的整数：' , end = ' ')
while guess != result and time > 0:
#    guess = int(input())
    temp = input()
    if not temp.isdigit():
        print('输入的不是整数！')
        print('请重新输入：' , end = ' ')
    else:
        guess = int(temp)
        if not (guess > 0 and guess < 11 ):
                print('输入的整数超出范围！')
                print('请重新输入：' , end = ' ')
        else:
                if guess == result:
                    print('猜对了！')
                else:
                    if guess > result:
                        print('大了！')
                    else:
                        print('小了!')
                    time = time - 1
                    if time == 0:
                        print('三次机会都猜错了！')
                    else:
                        print('请再次输入：' , end = " ")
print('游戏结束！')
    
