print('----此程序可以帮助你判断某年份是否为闰年！----')
temp = input('请输入年份：')
if not temp.isdigit():
    print('输入有误，这不是个年份！')
else:
    year = int(temp)
    if (year / 400) == int(year / 400):
        print(str(year) + '年是闰年！')
    else:
        if (year / 100) == int(year / 100):
            print(str(year) + '年不是闰年！')
        else:
            if (year / 4) == int(year / 4):
                print(str(year) + '年是闰年！')
            else:
                print(str(year) + '年不是闰年！')
