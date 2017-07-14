var = 'hi'

def fun1():
        global var
        var = 'baby '
        return fun2(var)

def fun2(var):
        var += 'i love you'
        fun3(var)
        return var

def fun3(var):
        var = '小甲鱼'

print(fun1())
