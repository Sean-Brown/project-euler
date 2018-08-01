function isPrime(num, prevPrimes) {
    if (num % 2 === 0) {
        return false;
    }
    let isPrime = true;
    for (let ix = 0; ix < prevPrimes.length; ix++) {
        if (num % prevPrimes[ix] === 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

let primes = [2];
let start = 3;
for (; primes.length < 10001; start++) {
    if (isPrime(start, primes)) {
        primes.push(start);
    }
}
console.log(`10001st prime number is ${primes[10000]}`);