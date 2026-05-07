def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def summation(n):
    if n == 0:
        return 0
    return n + summation(n - 1)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


def product_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)


def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)


def sum_range(start, end):
    if start > end:
        return 0
    return start + sum_range(start + 1, end)


def reverse_digits(n, result=0):
    if n == 0:
        return result
    return reverse_digits(n // 10, result * 10 + n % 10)

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)





def main():
    print("1. Factorial(6)          =", factorial(6))
    print("2. Summation(7)          =", summation(7))
    print("3. Power(2, 3)           =", power(2, 3))
    print("4. Fibonacci(6)          =", fibonacci(6))
    print("5. Sum of digits(67)     =", sum_of_digits(67))
    print("6. Product of digits(67) =", product_of_digits(67))
    print("7. Multiply(6, 7)        =", multiply(6, 7))
    print("8. Sum range(60, 70)     =", sum_range(60, 70))
    print("9. Reverse digits(6741)  =", reverse_digits(6741))
    print("10. Euclid GCD(70,60))   =", gcd_recursive(70,60))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()