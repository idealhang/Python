import random
result = random.randint(1,10)
temp = input("请输入一个数字：")
guess = int(temp)
chance = 0
while guess!=result and chance < 2:
    if guess > result:
        print("大了！")
        chance = chance +1
    else:
        print("小了！")
        chance = chance +1
    guess = int(input("猜错了，请再试下："))
if guess == result:
    print("猜对了！答案就是："+str(result))
else:
    print("3次机会都猜错了！")
print("游戏结束！")
