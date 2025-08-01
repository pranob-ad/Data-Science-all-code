import math

def f(x):
    return math.sqrt(25- x**2)

def f_prime(x):
    if x < -5 or x > 5:
        return -x / math.sqrt(25 - x**2)
    else:
        return 0 

def numerical_derivativetive(x,y,h):
    n = len(x)
    v = [0] * n
    for i in range(n):
        #v[i] = (f(x[i] + h) - f(x[i] - h)) / 2* h
        if i == 0:
            # Forward difference
            v[i] = (y[i+1] - y[i]) / h
        elif i == n-1:
            # Backward difference
            v[i] = (y[i] - y[i-1]) / h
        else:
            # Central difference
            v[i] = (y[i+1] - y[i-1]) / (2 * h)
    return v

def estimate_error(v,z):
    return sum(abs(vi - zi) for vi, zi in zip(v,z)) / len(v)

def merge_everything(h):
    x = [-5 + i * h for i in range(int((5-(-5))/h)+1)]
    y = [f(xi) for xi in x]
    z = [f_prime(xi) for xi in x]
    v = numerical_derivativetive(x, y, h)
    error = estimate_error(v, z)
    return x, y, z, v, error

#h = float(input("Enter the value of h: "))
h_values = [0.1, 0.05, 0.02, 0.01]  # You can add more or take user input
errors = []

for h in h_values:
    x, y, z, v, error = merge_everything(h)
    errors.append(error)
    print("Values of x:", x)
    print(f"For h = {h:.2f}, E(h) = {error:.5f}")

print("All errors:", errors)