num = 0
n = 1
while n == 1:
    if (num % 2 == 1) and (num % 3 ==2) and (num %5 == 4) and (num % 6 == 5) and (num % 7 == 0):
        print(num)
        n = 0
    else:
        num += 1
