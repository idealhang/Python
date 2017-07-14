def sxh(number):
        temp = (number % 10) ** 3 + (number // 10 % 10) ** 3 \
               + (number // 100) ** 3
        if temp == number:
                return True

for number in range(100,1000):
        if sxh(number):
                print(number)
