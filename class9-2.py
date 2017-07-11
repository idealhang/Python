num = 0
for red in range(0,4,1):
        for yellow in range(0,4,1):
                for blue in range(0,7,1):
                        if red + yellow + blue == 8:
                                num += 1
                                print('第' + str(num) + '种情况为：' , end = ' ')
                                print(str(red) + '个红球，' + str(yellow) + \
                                      '个黄球，' + str(blue) + '个蓝球')
