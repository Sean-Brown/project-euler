def isPrime(num, prevPrimes):
    if num % 2 == 0:
        return False
    isPrime = True
    for prime in prevPrimes:
        if num % prime == 0:
            isPrime = False
            break
    return isPrime

primes = [2]
start = 3
end = 2 * 1000 * 1000 # two million
sum = 2
while start < end:
    if isPrime(start, primes):
        primes.append(start)
        sum += start
    start += 2

print("sum of first 2 million primes = %s" % sum)
