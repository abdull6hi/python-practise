#Creating a function that sums all the digits in a number

def sum_of_digits(n):

    sum = 0
    #Start with zero as the sum

    while n > 0:
    #Loop through all digits

        sum += n % 10
        #add the last digit

        n = n // 10
        #remove the last digit
    return sum
    #Return the sum

test1 = 123
print(f"The sum of the digits in the number {test1} is {sum_of_digits(test1)}")

test2 = 46
print(f"The sum of the digits in the number {test2} is {sum_of_digits(test2)}")