import time
import math

start = time.time()
primelist = [2]
Number = 600851475143
factors = []

if Number % 2 == 0:
    factor = True
    while factor == True:
        if Number % 2 != 0:
            factor = False
            break
        factors.append(2)
        Number /= 2

def primefinder(number, Number):
    y = 3
    prime = [True] * (number + 1)
    for y in range(3, int(math.sqrt(number + 1)), 2):
        if prime[y] == True:
            primelist.append(y)
            if Number % y == 0:
                factor = True
                while factor == True:
                    if Number % y != 0:
                        factor = False
                        break
                    factors.append(y)
                    Number /= y
                    if number > Number:
                        factors.append(int(Number))
                        return None
            for x in range(y ** 2, number + 1, y + y):
                prime[x] = False
    for x in range(y + 2, number + 1, 2):
        if prime[x] == True:
            primelist.append(x)
            if Number % x == 0:
                factor = True
                while factor == True:
                    if Number % x != 0:
                        factor = False
                        break
                    factors.append(x)
                    Number /= x
                    if number > Number:
                        factors.append(int(Number))
                        return None
    if Number > 1:
        factors.append(int(Number))

primefinder(int(math.sqrt(Number) + 1), Number)


print(factors)

end = time.time()
print(end - start)
