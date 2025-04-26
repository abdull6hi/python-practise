#Creating a function that sums all the numbers in a list

def sum_list(numbers):
    
    sum = 0 
    #start with sum as 0
    
    for num in numbers:
        sum += num
    #Add each number to the sum

    return sum
    #returns total sum
    
#Testing with normal example 1
test1 = [1,2,3,4,5]
print("sum: ", sum_list(test1))

#Testing with normal example 2
test2 = [10,20,30]
print("sum: ", sum_list(test2))

#Testing with a negative number in the list
test3 = [-10,5,20]
print("sum: ", sum_list(test3))