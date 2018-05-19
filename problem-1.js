var i = 1;
var sum = 0;
var limit = 1000;

while (i < limit) {
    if (((i % 3) === 0) || ((i % 5) === 0)) {
        sum += i;
    }
    i++;
}

console.log('sum = ' + sum);
