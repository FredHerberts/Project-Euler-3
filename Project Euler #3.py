import math
import time

primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
primelist2 = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
Factors = []

number = int(600851475143)

start = time.time()

for x in primelist:
    factor = True
    while factor == True:
        if number % x != 0:
            factor = False
            break
        Factors.append(x)
        number = number / x

def primefinder(number):
    for y in range(103, number + 1,2):
        prime = True
        for x in primelist2:
            if y % x == 0:
                prime = False
                break
            if x > math.sqrt(y):
                break
        if prime == True:
            primelist2.append(y)
            factor2 = True
            while factor2 == True:
                if number % y != 0:
                    factor2 = False
                    break
                Factors.append(y)
                number = number / y
                if y > number+1:
                    break
            if y > number + 1:
                break
        if y > number + 1:
            break


primefinder(int(number))
end = time.time()
print(Factors)
print(end - start)


