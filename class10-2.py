member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print('---------方法一---------')
for each in member:
        if isinstance(each,int):
                print(each)
        else:
                print(each , end = ' ')
print('---------方法二---------')
i = 0
for each in member:
        i += 1
        if i % 2 != 0:
                print(each , end = ' ')
        else:
                print(each)
        
