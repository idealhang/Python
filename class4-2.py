# editor Idealhang
temp = int(input('请输入一个整数：'))
while temp > 0:
    i = temp -1
    j = temp
    while i > 0:
        print(' ' , end = '')
        i = i -1
    while j > 0:
        print('*' , end = '')
        j = j - 1
    print()
    temp = temp -1
