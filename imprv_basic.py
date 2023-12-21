# Print a message
print("Hello user")

# Get user input
user_ans = input("Enter a number: ")

# Print a message using user input
print("Hello, your number is " + user_ans + "!")

# Check conditions based on user input
if user_ans == '0':
    print("Be more creative.")
elif user_ans == '69':
    print("Noice!!!!!")
elif user_ans == '420':
    print("Meet me at 4:20 tomorrow behind campus.")
elif int(user_ans) > 100:
    print("You are generous with numbers.")
else:
    print("Be more generous.")

# Loop through a list of numbers
number_list = [1, 2, 3, 4, 5]
print("Iterating through a list of numbers:")
for num in number_list:
    print(num)

# Define and call functions for simple arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

# Call arithmetic functions
result_add = add(5, 3)
result_subtract = subtract(8, 4)
result_multiply = multiply(2, 6)
result_divide = divide(10, 2)

print("Arithmetic results:")
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)

# Import the math module and use its functions
import math

# Calculate the square root
sqrt_result = math.sqrt(25)
print("Square root of 25:", sqrt_result)
