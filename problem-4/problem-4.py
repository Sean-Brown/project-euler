import numpy as np

# 999x1 column vector, from 1 to 999
inputs = np.array([[x + 1 for x in range(999)]]).T

# 999x999 matrix with identical rows [1,...,999]
matrix = np.tile([x + 1 for x in range(999)], (999, 1))

# multiply the matrix by the column vector to get all 3 digit products
output = inputs * matrix

def isPalendrome(number):
    strNum = str(number)
    left = 0
    right = len(strNum) -1
    isPalendrome = True
    while (left < right):
        if strNum[left] != strNum[right]:
            isPalendrome = False
            break
        left += 1
        right -= 1
    return isPalendrome

# iterate through the results and find the largest palendrome -- not efficient but works
largest = 0
for row in output:
    for num in row:
        if isPalendrome(num) and num > largest:
            largest = num

print("largest three digit palendrome =", largest)