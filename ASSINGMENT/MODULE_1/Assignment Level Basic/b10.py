#B10:- Write a Python program to get the Factorial number of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

num =int(input("enter the no:"))
print("Factorial of", num, "is",
      factorial(num)) 