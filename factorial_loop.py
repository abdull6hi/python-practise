#Creating a function calculates the factorial of a number using for loop

def factorial_loop(n):
    result = 1
    #Start with 1
    for i in range(1,n+1):
    #Loop from 1 to n

        result *= i
        #Multiply result by current i to build factorial
    
    return result
    #return factorial

#Testing
test1 = 3
print(f"Factorial of the number {test1} is {factorial_loop(test1)} ")

test2 = 5
print(f"Factorial of the number {test2} is {factorial_loop(test2)} ")