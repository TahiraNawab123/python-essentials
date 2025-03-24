""" 
This program takes a string input from the user and prints it in reverse order.
It then counts the number of vowels in the string and displays the count.
"""
a = input("Please enter a string: ")        # Taking input from user
reversed_string = a[::-1]
print("The reversed string is: ", reversed_string)

# Initializing vowels and count variable
vowels = "aeiouAEIOU"
count = 0
# Looping through each character in text
for char in a:
    if char in vowels:     # Checks if character is a vowel
        count = count + 1    # Increment count if vowel found
# Printing the final count       
print("Number of Vowels are: ", count)


# This program takes an input number from the user.
# It checks whether the number is even or odd.
# If the number is divisible by 2, it prints "Even number".
# Otherwise, it prints "Odd number"

num = int(input("Please enter a number: "))
if num % 2 == 0:
    print("Number ", num, " is even" )
else:
    print("Number ", num, "is odd")
    
    
# Taking input from the user as a space-separated string of numbers
user_input = input("Please enter a list of Numbers: ")
# Converting the input string into a list of integers
num_list = list(map(int, user_input.split()))
# Sorting the list in ascending order
num_list.sort()
# Printing the sorted list
print("Sorted list: ", num_list)
