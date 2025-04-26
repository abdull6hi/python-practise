#Creating a function that reverses the order of letters in a word

def reverse_string(s):
    reversed_str = ''
    #Start with sn empty string

    for char in s:
    #Loop through each character
        reversed_str = char + reversed_str
        #Loop each character

    return reversed_str
    #return the reversed string
    
#Testing
test1 = "hello"
print(f"Reversed string of the word {test1} is {reverse_string(test1)}")

test2 = "World"
print(f"Reversed string of the word {test2} is {reverse_string(test2)}")