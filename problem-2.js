function calcEvenFibs(prev, curr, sum, limit) {
    if (curr >= limit) {
        return sum;
    }    
    if ((curr % 2) === 0) {
        sum += curr;
    }
    var tmp = prev;
    prev = curr;
    curr += tmp;
    return calcEvenFibs(prev, curr, sum, limit);
}

var max = 4000000; // 4 million
var sum = calcEvenFibs(0, 1, 0, max);
console.log('sum = ' + sum);
