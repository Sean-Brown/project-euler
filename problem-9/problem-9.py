product = 0
a = 1
while a < 998 and product == 0:
    b = a + 1
    while b < 1000 and product == 0:
        c = ((a**2) + (b**2)) ** (1/2)
        if (c % 2 == 0) or ((c + 1) % 2 == 0):
            # it is a triplet, check that it sums to 1000
            if (a + b + c) == 1000:
                product = a * b * c
        b += 1
    a += 1

print("the product is %s" % product)