numbers = [x + 1 for x in range(100)]

sumOfSquares = sum([x * x for x in numbers])

squareOfSums = sum(numbers) * sum(numbers)

print("sum of squares = %s, square of sums = %s" % (sumOfSquares, squareOfSums))
print("difference", squareOfSums - sumOfSquares)