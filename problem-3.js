// https://stackoverflow.com/questions/24166478/efficient-ways-of-finding-the-largest-prime-factor-of-a-number
function largestPrimeFactor(val, divisor = 2) { 
    var square = (val) => Math.pow(val, 2);

    while ((val % divisor) != 0 && square(divisor) <= val) {
        divisor++;
    }

    return square(divisor) <= val
        ? largestPrimeFactor(val / divisor, divisor)
        : val;
}

var limit = 600851475143;
var largestPrimeFactor = largestPrimeFactor(limit);

console.log('largest prime factor = ' + largestPrimeFactor);