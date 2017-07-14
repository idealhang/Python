def power(x,y):
        if (isinstance(x,int) or isinstance(x,float)) and \
           (isinstance(y,int) or isinstance(y,float)):
                return x ** y
        else:
                return ('输入有误！')
        
