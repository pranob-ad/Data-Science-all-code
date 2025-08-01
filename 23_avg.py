import math

def average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

numbers = [10, 20, 3, 40, 50]
avg = average(numbers)
print(f"The average of {numbers} is {avg}")

#alternative solution using ceil

def sove(arr, n):
    avg = sum(arr)/n
    result = math.ceil(avg)
    return result
arr = [10, 20, 3, 40, 50]
n = len(arr)
avg = sove(arr, n)
print(f"The average of {arr} is {avg}")