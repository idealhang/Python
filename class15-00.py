while 1:
        print('请输入一个整数(输入Q结束程序)：' , end='')
        temp = input()
        if temp == 'Q':
                break
        elif not temp.isdigit():
                print('您输入的不是整数！')
#        else:
#                num = int(temp)
#                print('十进制 -> 十六进制：' , num , '->' + '%x' % num)
#                print('十进制 ->   八进制：' , num , '->' + '%o' % num)
#                print('十进制 ->   二进制：' , num , '->' + bin(num))

        else:
                num = int(temp)
                print('十进制 -> 十六进制：' + '%d -> 0x%x' % (num,num) )
                print('十进制 ->   八进制：' + '%d -> 0o%o' % (num,num)  )
                print('十进制 ->   二进制：' , num , '->' + bin(num) )
