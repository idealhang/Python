string1 = input('请输入目标字符串：')
string2 = input('请输入子字符串（两个字符）：')

def newfun1(string1,string2):
        time = 0
        for i in range(len(string1)-1):
                if string1[i] == string2[0] and string1[i+1] == string2[1]:
                        time += 1
        return time

print(newfun1(string1,string2))
                
