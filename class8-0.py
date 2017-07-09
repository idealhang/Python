while 1:
    temp = input('请输入分数：')
    if temp == 'exit':
        break
    if not temp.isdigit():
        print('输入的不是分数！')
    else:
        score = int(temp)
        if 60 <= score < 80:
            print('C')
        elif 80 <= score < 90:
            print('B')
        elif 90 <= score <= 100:
            print('A')
        elif score < 60:
            print('D')
        else:
            print('输入有误，请输入一个在0到100之间的数值！')
