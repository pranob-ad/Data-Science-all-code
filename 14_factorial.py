def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    :param n: The number to calculate the factorial for.
    :return: The factorial of the number.
    """
    if n < 0:
        return "not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #this funtion is calling the function itself--
                                    # --until it reaches (n == 0 or n == 1).

# Test the factorial function
num = int(input("Enter a number to calculate its factorial: "))
factor = factorial(num)
print(f"The factorial of {num} is {factor}")