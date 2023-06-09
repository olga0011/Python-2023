'''1. Write a Python program that reads a text file called "input.txt" and counts the occurrences of 
each word in the file. Print the word and its count. Ignore case sensitivity 
(treat "Hello" and "hello" as the same word)'''

with open("input.txt", "r", encoding="utf-8") as fo:  # return a file object "fo" and close the file automatically
    dictionary = dict()
    content = fo.read()  # read all the contents of the file into a string
    words = (content.lower().split())  # convert all uppercase characters in a string into lowercase characters and return it

    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1  # add the word to dictionary with count 1

for key in list(dictionary.keys()):
    print(key, ":", dictionary[key])

'''Output:
white : 3
yellow : 2
blue : 2
red : 4
зеленый : 1
grün : 1
green : 2
black : 1
brown : 1

By using 'encoding="utf-8"', even output with an umlaut (grün) or cyrillic letters (зеленый) is also displayed correctly. 
That's not the case without using encoding'''

'''2. Write a Python lambda function that takes two parameters a and b, 
and returns the sum of their squares. Assign the lambda function to a variable 
called sum_of_squares. Test the lambda function by passing different values for a and b.'''

sum_of_squares = lambda a, b: a**2 + b**2
print (sum_of_squares(3, 1))
print (sum_of_squares(0, 1))
print (sum_of_squares(-1,-3))

'''3. Write a Python function called calculate_average that accepts a variable 
number of arguments (numbers) and returns the average of those numbers. 
Test the function with different sets of numbers.'''

def calculate_average(*args):
    sum = 0
    counter = 0
    average = 0
    for x in args:
        sum += x #sum of all arguments
        counter += 1 #number of arguments
        average = sum/counter
    print("average:", str(average))

calculate_average(1, 3, 0, 2, 4) #2.0
calculate_average(-7.5) #-7.5
calculate_average(5.0, 2, -2, 1) #1.5
