#Creating a function that checks if a number is even or odd

def check_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    #If the number is divisble by two return even

    else:
        return "Odd"
    #If the number isn't divisble by two return odd

#Testing an even number
test1 = 36
print(f"The number {test1} is {check_even_or_odd(test1)}")

#Testing an odd number
test2 = 47
print(f"The number {test2} is {check_even_or_odd(test2)}")