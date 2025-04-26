#Creating a function calculates the factorial of a number using recursion

def factorial_recursive(n):
    if n == 0 or n == 1:
    #Setting the base case for factorial lof 0 and 1 as 1
        return 1
    else:
        return n * factorial_recursive(n-1)
    #recursion call

#Testing
test1 = 3
print(f"Factorial of the number {test1} is {factorial_recursive(test1)} ")

test2 = 5
print(f"Factorial of the number {test2} is {factorial_recursive(test2)} ")