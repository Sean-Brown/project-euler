inputs = [x + 1 for x in range(20)]

def isDivisibleByAll(number):
    isDivisible = True
    for input in inputs:
        if number % input != 0:
            isDivisible = False
            break
    return isDivisible

# start at 2 and increment by 2 since the number has to be even
start = 2520
while not isDivisibleByAll(start):
    start += 2

print("smallest number divisible by numbers 1 through 20 is", start)