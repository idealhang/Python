for x in range(1,10,1):
        for y in range(0,10,1):
                for z in range(0,10,1):
                        num1 = (100 * x) + (10 * y) + (z)
                        num2 = (x ** 3) + (y ** 3) + (z ** 3)
                        if num1 == num2:
                                print(str(num1)+'是水仙花数！')
