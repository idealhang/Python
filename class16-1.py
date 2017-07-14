list1 = [1,2,3,4,5,6.1,'a','b',7,8,9]
result = 0
for each in list1:
        if isinstance(each,int) or isinstance(each,float):
                result = result + each
print(result)


