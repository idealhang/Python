def myfun1(string):
        if len(string) > 1:
                for each in range(len(string) // 2):
                        if string[each] == string[-(each+1)]:
                                result = '是'
                        else:
                                result = '不是'
        else:
                print('您输入的太短，没有意义！')
                result = None
        return result
        

string1 = input('请输入一句话：')
if myfun1(string1) != None:
        print(myfun1(string1)+'回文联！')
