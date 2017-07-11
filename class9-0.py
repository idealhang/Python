print('请输入密码：' , end = '')
rightpassword = 'FishC.com'
chance = 3
while chance > 0:
        password = input()
        if '*' in password:
                print('密码中不能含有\"*\"号！您还有 ' + str(chance) + \
                      ' 次机会！请输入密码：' , end = '')
                continue
        else:
                chance -= 1       
                if password == rightpassword:
                        print('密码正确，正在进入程序。。。')
                        break
                elif chance == 0:
                        print('您已输错3次密码，程序退出！')
                        break
                else:
                        print('密码错误！您还有 ' + str(chance) + \
                              '次机会！请输入密码：' , end = '')

