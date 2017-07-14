while 1:
        password = input('请输入需要检查的密码：')
        length = len(password)
        num = 0
        string1 = r'~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
        warning1 = '''请按以下方式提升您的密码安全级别：
                1.密码必须由数字、字母及特殊字符三种组合
                2.密码只能由字母开头
                3.密码长度不能低于16位'''
        
        if password == '退出程序':
                break
        
        for i in range(length):
                if password[i].isalpha():
                        num += 1
                        break
                
        for i in range(length):
                if password[i].isdigit():
                        num += 1
                        break

        for i in range(length):
                if password[i] in string1:
                        num += 1
                        break
                
        if length >= 16 and password[0].isalpha() and num == 3:
                print('您的密码安全级别评定为：高')
                print('请继续保持')
        elif length >= 8 and num >= 2:
                print('您的密码安全级别评定为：中')
                print(warning1)
        else:
                print('您的密码安全等级评定为：低')
                print(warning1)

